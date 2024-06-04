#!/bin/bash

python  ../../../src/run.py \
        --experiment ../../../results/gpt4/wnli/valid \
        --filepath ../../../data/wnli/wnli_valid.csv \
        --task nli \
        --dataset WNLI \
        --split validation \
        --model gpt-4-0613 \
        --text_column sentence1 sentence2 \
        --label_column label \
        --process_guided_replication  \
        --process_general_replication \
        --bleurt_eval \
        --rouge_eval \
        --icl_eval \
