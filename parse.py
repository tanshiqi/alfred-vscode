import os
import json
import sys
dir = os.environ['dir']

projects = os.listdir(dir)

items = []
for project in projects:
    file_full_path = dir + "/" + project
    if (os.path.isdir(file_full_path)):
        item = {
            "title": project,
            "subtitle": file_full_path,
            "arg": file_full_path
        }
        if sys.argv[1]:
            if sys.argv[1].lower() in project.lower():
                items.append(item)
        else:
            items.append(item)

result = {
    "items": items
}

output = json.dumps(result)
print(output)
