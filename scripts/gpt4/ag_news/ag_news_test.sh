#!/bin/bash

python  ../../../src/run.py \
        --experiment gpt4/ag_news/test \
        --filepath ../../../data/ag_news/ag_news_test.csv \
        --task cls \
        --dataset "AG News" \
        --split test \
        --model gpt-4-0613 \
        --text_column text \
        --label_column column \
        --process_guided_replication  \
        --process_general_replication \
        --bleurt_eval \
        --rouge_eval \
        --icl_eval \
