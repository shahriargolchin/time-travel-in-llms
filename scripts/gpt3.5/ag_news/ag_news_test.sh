#!/bin/bash

python  ../../../src/run.py \
        --experiment ../../../results/gpt3.5/ag_news/test \
        --filepath ../../../data/ag_news/ag_news_test.csv \
        --task cls \
        --dataset "AG News" \
        --split test \
        --model gpt-3.5-turbo-0613 \
        --text_column text \
        --label_column label \
        --process_guided_replication  \
        --process_general_replication \
        --bleurt_eval \
        --rouge_eval \
        --icl_eval \
