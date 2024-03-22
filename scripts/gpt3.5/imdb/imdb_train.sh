#!/bin/bash

python  ../../../src/run.py \
        --experiment gpt3.5/imdb/train \
        --filename ../../../data/imdb/imdb_train.csv \
        --task cls \
        --dataset IMDB \
        --split train \
        --model gpt-3.5-turbo-0613 \
        --text_column text \
        --label_column label \
        --process_guided_replication  \
        --process_general_replication \
        --bleurt_eval \
        --rouge_eval \
        --icl_eval \