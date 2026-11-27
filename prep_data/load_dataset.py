# prepare_data.py

def load_dataset(file_path):
    """
    Load the POS dataset and return a list of sentences.
    Each sentence is a list of (word, tag) tuples.
    """

    sentences = []      # Store all sentences
    sentence = []       # Store one sentence

    with open(file_path, "r", encoding="utf-8") as file:

        for line in file:

            line = line.strip()

            # Empty line means the sentence ends
            if line == "":
                if sentence:
                    sentences.append(sentence)
                    sentence = []

            else:
                word, tag = line.split("/",1)
                sentence.append((word, tag))

    # Add the last sentence if the file doesn't end with a blank line
    if sentence:
        sentences.append(sentence)

    return sentences


if __name__ == "__main__":

    dataset = load_dataset("./data/mypos-ver.3.0.txt")

    print("Number of sentences:", len(dataset))
    print(dataset[0])
