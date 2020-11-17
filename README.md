# CSV Normalization
A part of the Truss interview process.
## Prerequisites
To run this program, you will need to install Python3. I recommend Python 3.5 or above.
```
apt install python3
```
Note that you may need to preface the above command with "sudo".

You will also need to give execution permissions to the normalizer.sh script. This may
be accomplished with the following command.
```
chmod +x normalizer.sh
```
## Operating System
This program was tested on Ubuntu 16.04 LTS, but should work with Bash and Python on most Operating Systems.
## Run the Program
To run this program, use the following command:
```
./normalizer.sh sample.csv > out.csv
```
For ease of use, the program takes the input filename as a parameter and then outputs
the normalized csv to stdout. With the above command, it will create a file called "out.csv".
