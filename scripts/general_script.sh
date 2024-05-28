#!/bin/bash

# -- Set the variables below with appropriate values --
EXPERIMENT="Path to Your Experiment Results" 
FILENAME="Path to Your Data File" 
TASK="Task Corresponds to Your Dataset"
DATASET="Your Dataset Name" 
SPLIT="Split Corresponds to Your Data" 
MODEL="OpenAI Model Snapshot"
TEXT_COLUMN="Your Text Column Name" 
# LABEL_COLUMN="column" # Replace with the name of the label column only when your dataset comes with label
# -- End of variables --


python  ../src/run.py \
        --experiment "${EXPERIMENT}" \
        --filename "${FILENAME}" \
        --task "${TASK}" \
        --dataset "${DATASET}" \
        --split "${SPLIT}" \
        --model "${MODEL}" \
        --text_column "${TEXT_COLUMN}" \
        --should_text_split \
        --process_guided_replication  \
        --icl_eval \
        --max_p 70 \
        --min_p 40 \
        #--label_column "${LABEL_COLUMN}" \
