import random
import json
header = ['a', "b", 'c', 'd']
raw = {}
for i in header:
    raw[i] = []
    for j in range(80):
        raw[i].append(round(float(random.random()*100), 5))
with open('./raw.json', 'w+') as f:
    json.dump(raw, f)
