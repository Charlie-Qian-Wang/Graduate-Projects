import os
import json
from generateSongCi import generateSongCi, lang
from utils import *


if not os.path.isdir("data"):
    os.makedirs("data")

with open("../songci_same_hxs/data/ci.test.hxs.json","r") as file:
    testingDataset = json.load(file)

testingOutput = []
cnt = 0
for testCase in testingDataset:
    cnt += 1
    print(cnt)
    testingOutput.append(generateSongCi(testCase["src"],testCase["rhythmic"],lang))

with open("data/testingOutput_sdgt_hxs.json","w") as file:
    json.dump(testingOutput, file, indent=2, ensure_ascii=False)
