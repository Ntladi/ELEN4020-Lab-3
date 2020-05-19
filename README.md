# ELEN4020 Lab 3
Mrs MapReuce is used to implement the Word-Count, Top-K and Inverted Index algorithms. The `Word_Count`, `Top-K` and `Inverted_Index` directories each contain all the source code and files for their respective algorithms and are independent of one another. Each directory has an `Input` directory, an `Output` directory, as well as a `Scripts` directory. The `Input` directory contains the three input files from Sakai. The `Output` folder contains an output for each input in `.txt` form. The `Scripts` folder contains the all the python scripts required to execute the relevant algorithm. There is also a `Execute.sh` shell script as well as `requirements.txt` file in each directory. These are used to execute the algorithm as described in  'Build Instructions'.

## Software Prerequisites
The results contained in the `Output` folder for each algorithm were generated on the Wits EIE Jaguar 1 cluster. The following software was used and may be needed to replicate said results:

* Linux Ubuntu 18.04 LTS

* Python => 3.6.x

* virtualenv with pip

## Build Instructions
1. Open a new terminal window 
1. Change the directory to that of the algorithm that is to be tested.
1. Run the `Execute.sh` shell script from with the directory as follows:
```bash
./Execute.sh
```

### Execution Procedure
* The `Execute.sh` shell script begins by deleting the old `Output` folder and replacing it with a new empty one.
* The shell script will then create a new virtual environment by running the `virtual_env.py` Python script located within the `Scripts` directory.
* Once the virtual environment is created, the shell script will start the virtual environment and install all the dependencies described in `requirements.txt` using `pip`.
* After all dependencies are installed, the script will run the relavant algorithm for the `small.txt`, `large.txt` and `very_large.txt` inputs located in the `Input` directory.
* The virtual environment is then deactivated and delated along with any cache files.
* The results can be found in the relevant `.txt` file within the newly created `Output` folder.