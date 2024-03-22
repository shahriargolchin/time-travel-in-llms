#!/bin/bash

python  ../../../src/run.py \
        --experiment gpt4/samsum/test \
        --filename ../../../data/samsum/samsum_test.csv \
        --task sum \
        --dataset SAMSum \
        --split test \
        --model gpt-4-0613 \
        --text_column summary \
        --process_guided_replication  \
        --process_general_replication \
        --bleurt_eval \
        --rouge_eval \
        --icl_eval \
