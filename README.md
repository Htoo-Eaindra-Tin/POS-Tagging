# POS-Tagging
# Myanmar POS Tagger (`python-crfsuite`)

A Myanmar Part-of-Speech (POS) tagging project using Conditional Random Fields (`python-crfsuite`) trained on the **myPOS** corpus (`mypos-ver.3.0.txt`)[cite: 1].

## Dataset
* **Source:** [myPOS Corpus by Ye Kyaw Thu](https://github.com/ye-kyaw-thu/myPOS)
* **Corpus File Used:** `mypos-ver.3.0.txt` (kept locally in `data/`, excluded from version control)[cite: 1]
* **Train / Test Split:** 80% / 20% (`34,556` train sentences and `8,640` test sentences; `108,072` test tokens)[cite: 1]


## Model & Features
* **Algorithm:** Linear-chain Conditional Random Fields (`pycrfsuite.Trainer` and `pycrfsuite.Tagger`)[cite: 1]
* **Features:** Token text, character n-grams/affixes, numeric checks, neighboring word/suffix context, and sentence boundary markers (`BOS` / `EOS`)[cite: 1]
* **Evaluation Summary:** `0.96` overall token accuracy (`0.96` weighted avg F1, `0.93` macro avg F1) across 15 POS tags on the test set[cite: 1]

## Setup & Usage
1. Install dependencies:
   ```bash
   pip install python-crfsuite scikit-learn
   ```
2. Place `mypos-ver.3.0.txt` inside a local `data/` folder (`data/mypos-ver.3.0.txt`)[cite: 1].
3. Open `Htoo_Eaindra_Tin.assignment-1.ipynb` and run the cells to train or evaluate the model and tag input tokens[cite: 1].
