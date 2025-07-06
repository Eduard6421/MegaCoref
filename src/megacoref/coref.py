import torch
import numpy as np
from transformers import BertTokenizerFast

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def get_token_word_mapping(text, tokenizer):
    encoding = tokenizer(text, return_offsets_mapping=True, add_special_tokens=False, return_tensors="pt")

    tokens = encoding.tokens()
    word_ids = encoding.word_ids()

    print(f"Tokens: {tokens}")
    print(f"Word IDs: {word_ids}")

    '''
    words = []
    seen_ids = set()

    for i, word_id in enumerate(word_ids):
        if word_id is not None and word_id not in seen_ids:
            start, end = encoding.offset_mapping[i]
            words.append(text[start:end])
            seen_ids.add(word_id)

    word_ids = np.array([-1 if w is None else w for w in word_ids])

    return tokens, word_ids, words
    '''


if __name__ == "__main__":
    tokenizer = BertTokenizerFast.from_pretrained("bert-base-uncased")

    samples = [
        "A state-of-the-art model.",
        "Hello, how are you?",
        "This is not right!"
    ]

    get_token_word_mapping(samples[0], tokenizer)
    get_token_word_mapping(samples[0], tokenizer)

