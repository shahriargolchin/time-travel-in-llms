#!/bin/bash

python  ../../../src/run.py \
        --experiment gpt3.5/wnli/valid \
        --filepath ../../../data/wnli/wnli_valid.csv \
        --task nli \
        --dataset WNLI \
        --split validation \
        --model gpt-3.5-turbo-0613 \
        --text_column sentence1 sentence2 \
        --label_column label \
        --process_guided_replication  \
        --process_general_replication \
        --bleurt_eval \
        --rouge_eval \
        --icl_eval \
