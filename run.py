#!/usr/bin/env python3

import os
import json

with open('config.json', encoding='utf8') as config_json:
    config = json.load(config_json)

results = {"errors": [], "warnings": []}

directions = None

if not os.path.exists("secondary"):
    os.mkdir("secondary")

if not os.path.exists("output"):
    os.mkdir("output")

with open("output/out.txt", "w") as f:
    f.write("hello")

with open("secondary/secondary.txt", "w") as f:
    f.write("hello there!")

with open("product.json", "w") as fp:
    json.dump(results, fp)

print("done");
