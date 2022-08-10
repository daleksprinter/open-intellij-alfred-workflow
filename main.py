import sys
import os
import json
query = "{query}"

path = os.getenv("PATH")
img_path = os.getenv("IMG_PATH")

orgs = os.listdir(path=path)
items = []
for o in orgs:
    opath = path + '/' + o
    repos = os.listdir(opath)
    for r in repos:
        rpath = opath + '/' + r
        if not os.path.isdir(rpath):
            continue

        if not query in r:
            continue
        # see https://www.alfredapp.com/help/workflows/inputs/script-filter/json/
        item = {
            "title": r,
            "subtitle": rpath,
            "arg": rpath,
            "icon": {
                "path": img_path
            }
        }
        items.append(item)

print(json.dumps({"items": items}))
