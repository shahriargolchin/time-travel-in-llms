#!/bin/bash

python  ../../../src/run.py \
        --experiment gpt4/samsum/train \
        --filename ../../../data/samsum/samsum_train.csv \
        --task sum \
        --dataset SAMSum \
        --split train \
        --model gpt-4-0613 \
        --text_column summary \
        --process_guided_replication  \
        --process_general_replication \
        --bleurt_eval \
        --rouge_eval \
        --icl_eval \
