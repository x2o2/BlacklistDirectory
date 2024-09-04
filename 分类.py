import re

import torch
from transformers import AutoTokenizer, BertForSequenceClassification

model_path = r"C:\Users\admin\Downloads\Compressed\iioSnailbert-base-chinese-word-classifier"

tokenizer = AutoTokenizer.from_pretrained(model_path,clean_up_tokenization_spaces=True)
model = BertForSequenceClassification.from_pretrained(model_path)

words =  [word for line in open('./黑名单/readme.md',encoding='utf-8')
                .read().splitlines() if not line.strip().startswith('#')
                        for word in re.split(r'\s+', line.strip()) if word]
print(words)
inputs = tokenizer(words, return_tensors='pt', padding=True)
outputs = model(**inputs).logits
outputs = outputs.sigmoid()
preds = outputs > 0.5

for i, pred in enumerate(preds):
    pred = torch.argwhere(pred).view(-1)
    labels = [model.config.id2label[int(id)] for id in pred]

    with open(f"./分类/{'其他' if len(labels) == 0 else labels[0]}.md", 'a', encoding='utf-8') as file:
        file.write(" ".join(words))
    print(words[i], ":", labels)


