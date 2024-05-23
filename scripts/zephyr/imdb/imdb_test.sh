#!/bin/bash

# default params
#SBATCH -t 05:00:00                     # est. Runtime upper limit!
#SBATCH --partition=gpu-a100
#SBATCH -G A100:1
#SBATCH --mem=40GB                      # Memory needed
#SBATCH --job-name=test_data            # name of the run
#SBATCH --output=./logs/%x-%j.out       # logging output
#SBATCH --error=./logs/%x-%j.err        # error output

# Project root dir
PATH="time-travel-in-llms/"   
CWD=$(pwd)

# Prepare the environment.
module load anaconda3
source activate time-travel-venv           # TODO edit 
cd "$PATH"
export PYTHONPATH=$PYTHONPATH:$PATH
export TOKENIZERS_PARALLELISM=true




python  src/run.py \
        --experiment gpt4/imdb/test \
        --filename data/imdb/imdb_test.csv \
        --task cls \
        --dataset IMDB \
        --split test \
        --model /scratch/usr/nimtsspi/model/ \
        --library huggingface \
        --text_column text \
        --label_column label \
        --process_guided_replication  \
        --process_general_replication \
        --bleurt_eval \
        --rouge_eval \
        --icl_eval \
