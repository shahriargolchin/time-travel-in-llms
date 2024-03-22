#!/bin/bash

python  ../../../src/run.py \
        --experiment gpt4/ag_news/train \
        --filename ../../../data/ag_news/ag_news_train.csv \
        --task cls \
        --dataset "AG News" \
        --split train \
        --model gpt-3.5-turbo-0613 \
        --text_column text \
        --label_column label \
        --process_guided_replication  \
        --process_general_replication \
        --bleurt_eval \
        --rouge_eval \
        --icl_eval \
