#!/bin/bash

python  ../../../src/run.py \
        --experiment gpt4/rte/train \
        --filename ../../../data/rte/rte_train.csv \
        --task nli \
        --dataset RTE \
        --split train \
        --model gpt-4-0613 \
        --text_column sentence1 sentence2 \
        --label_column label \
        --process_guided_replication  \
        --process_general_replication \
        --bleurt_eval \
        --rouge_eval \
        --icl_eval \
