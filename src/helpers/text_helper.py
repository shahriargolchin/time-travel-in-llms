from nltk.tokenize import sent_tokenize
import random
import nltk

nltk.download("punkt")


def split_randomly(item_list, min_p, max_p, seed):
    random.seed(seed)
    split_point = round(
        random.uniform(min_p / 100 * len(item_list), max_p / 100 * len(item_list))
    )
    first_piece = " ".join(item_list[:split_point])
    second_piece = " ".join(item_list[split_point:])
    return first_piece, second_piece


def split_text_randomly(text, min_p=40, max_p=70, seed=42):
    sentences = sent_tokenize(text)

    if len(sentences) > 1:
        return split_randomly(sentences, min_p, max_p, seed)
    else:
        words = text.split(" ")
        return split_randomly(words, min_p, max_p, seed)
