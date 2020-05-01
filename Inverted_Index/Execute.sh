#!/bin/bash

# This script will create a virtual environment and execute the map reduce 
# algorithm on the given inputs within the "Inputs" folder
rm -rf Output
mkdir Output
# Create a virtual environment if one already does not exist
printf "Creating Virtual Environment\n\n"
python3 ./Scripts/virtual_env.py

# Start the virtual environment
printf "\n\nStarting Virtual Environment\n\n"
source Environment/bin/activate
pip install -r requirements.txt

# Run Top K Query for inputs
printf "\n\nRunning Inverted Index for the Small Input\n\n"
python3 ./Scripts/run_inverted_index.py ./Input/small.txt ./Output/small.txt 30
printf "\n\nRunning Inverted Index for the Large Input\n\n"
python3 ./Scripts/run_inverted_index.py ./Input/large.txt ./Output/large.txt 30
printf "\n\nRunning Inverted Index for the Very Large Input\n\n"
python3 ./Scripts/run_inverted_index.py ./Input/very_large.txt ./Output/very_large.txt 30
# Delete the virtual environment and cache files
rm -rf Environment
rm -rf ./Scripts/__pycache__
rm -rf Temp
