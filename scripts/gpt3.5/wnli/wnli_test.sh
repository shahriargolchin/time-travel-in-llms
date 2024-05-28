#!/bin/bash

python  ../../../src/run.py \
        --experiment gpt3.5/wnli/test \
        --filepath ../../../data/wnli/wnli_test.csv \
        --task nli \
        --dataset WNLI \
        --split test \
        --model gpt-3.5-turbo-0613 \
        --text_column sentence1 sentence2 \
        --label_column label \
        --process_guided_replication  \
        --process_general_replication \
        --bleurt_eval \
        --rouge_eval \
        --icl_eval \
