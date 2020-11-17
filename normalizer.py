import csv
import sys
from datetime import datetime, timedelta

def normalize(inFileName):
    """
    Follow the specifications outlined in the Truss CSV interview problem to
    parse a csv file and output the normalized version of that file.

    :param inFileName: Name of the file input via stdin
    :return: None (results printed to stdout)
    """
    csvFileArray = []
    try:
        with open(inFileName, 'r', encoding="utf8", errors="replace") as csvFile:
            csvReader = csv.reader(csvFile, delimiter=',')
            #Process the first row with the column headers
            csvFileArray.append(next(csvReader))
            rowNum = 0
            for row in csvReader:
                rowNum += 1 #Starts at 1, since the header row is already handled
                #Handle Timestamp Field
                try:
                    ts = handleTimestamp(row[0], rowNum)
                except Exception as e:
                    sys.stderr.write(str(e)+"\n")
                    continue
                #Handle address Field
                addr = row[1]
                #Handle Zip Code Field
                try:
                    zipcode = handleZipCode(row[2], rowNum)
                except Exception as e:
                    sys.stderr.write(str(e) + "\n")
                    continue
                #Handle Fullname Field
                fullname = handleFullNames(row[3])
                #Handle Duration Fields
                try:
                    fooDur = handleDuration(row[4], rowNum)
                except Exception as e:
                    sys.stderr.write(str(e) + "\n")
                    continue
                try:
                    barDur = handleDuration(row[5], rowNum)
                except Exception as e:
                    sys.stderr.write(str(e) + "\n")
                    continue
                totalDur = fooDur + barDur
                #Handle Notes
                notes = row[7]
                csvFileArray.append([ts, addr, zipcode, fullname, fooDur, barDur, totalDur, notes])
    except FileNotFoundError:
        sys.stderr.write("File named %s does not exist" % inFileName)
        exit()
    except:
        sys.stderr.write("Unable to read file.")
        exit()
    for row in csvFileArray:
        for el in row:
            print(el, end=' ')
        print("")

def handleTimestamp(dateStr, rowNum):
    try:
        newTime = datetime.strptime(dateStr, '%m/%d/%y %I:%M:%S %p') + timedelta(hours=3)  # Add 3 hours PST -> EST
    except:
        raise Exception("Warning: Timestamp invalid. Dropping row %s." % rowNum)
    formattedStr = newTime.isoformat()
    if not isinstance(dateStr, str):
        raise Exception
    return formattedStr

def handleZipCode(zipStr, rowNum):
    if len(zipStr) > 5:
        raise Exception("Zipcode is too long. Dropping row %s." % rowNum)
    try:
        int(zipStr)
    except ValueError:
        raise Exception("Invalid Zipcode. Dropping row %s." % rowNum)
    return zipStr.zfill(5)

def handleFullNames(nameStr):
    return nameStr.upper()

def handleDuration(timeStr, rowNum):
    try:
        y = timeStr.split(":")
        seconds = float(y[0])*3600 + float(y[1])*60 + float((y[2]))
    except:
        raise Exception("Invalid Duration. Dropping row %s." % rowNum)
    return seconds

if __name__ == '__main__':
    # if not len(sys.argv)>1:
    #     sys.stderr.write("This program expects 2 filenames: an input csv file and an output csv file.")
    if sys.argv[1][-4:] != ".csv":
        sys.stderr.write("Please input a file of type csv")
    inName = sys.argv[1]
    normalize(inName)
