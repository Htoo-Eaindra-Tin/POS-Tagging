def load_pos_data(filepath):
    sentences = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            pairs = line.split()
            sentence = [tuple(p.rsplit('/', 1)) for p in pairs if '/' in p]
            if sentence:
                sentences.append(sentence)
    return sentences

sentences = load_pos_data("data/mypos-ver.3.0.txt")
print(sentences[0][:5])
