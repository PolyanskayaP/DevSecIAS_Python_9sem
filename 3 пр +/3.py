import json
import os

d = {
"data": "Click Here",
"size": 36,
"style": "bold",
"name": "text1",
"hOffset": 250,
"vOffset": 100,
"alignment": "center",
"onMouseUp": "sun1.opacity = (sun1.opacity / 100) * 90;"
}
filename = "sample.json"


with open(filename, "w") as outfile:
    json.dump(d, outfile, indent=4, ensure_ascii=False)

with open(filename, "r") as file:
    for line in file:
        print(line)

file.close()
os.remove(filename)