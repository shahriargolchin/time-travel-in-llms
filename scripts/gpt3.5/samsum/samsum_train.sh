#!/bin/bash

python  ../../../src/run.py \
        --experiment ../../../results/gpt3.5/samsum/train \
        --filepath ../../../data/samsum/samsum_train.csv \
        --task sum \
        --dataset SAMSum \
        --split train \
        --model gpt-3.5-turbo-0613 \
        --text_column summary \
        --process_guided_replication  \
        --process_general_replication \
        --bleurt_eval \
        --rouge_eval \
        --icl_eval \
