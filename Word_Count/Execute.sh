#!/bin/bash

# This script will create a virtual environment and execute the map reduce 
# algorithm on the given inputs within the "Inputs" folder

echo "Running MapReduce using Mrs-MapReduce for Word Count"

# Create a virtual environment if one already does not exist
python3 ../virtual_env.py

# Start the virtual environment
source Word_Count_env/bin/activate
pip install -r requirements.txt

# Run MapReduce for inputs
# python3 ./Source/run_word_count.py ./Input/text_data1.txt 
