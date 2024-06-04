#!/bin/bash

python  ../../../src/run.py \
        --experiment ../../../results/gpt4/ag_news/train \
        --filepath ../../../data/ag_news/ag_news_train.csv \
        --task cls \
        --dataset "AG News" \
        --split train \
        --model gpt-4-0613 \
        --text_column text \
        --label_column label \
        --process_guided_replication  \
        --process_general_replication \
        --bleurt_eval \
        --rouge_eval \
        --icl_eval \
