import json


groups = list()
groups.append('admin level 0')


json_data = []
for idx, group in enumerate(groups):
    json_data.append({
    "model": "email_sender.group",
    "pk": len(json_data) + idx,
    "fields": {
      "id": idx,
      "name": group,
      "permissions": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    }})

with open('groups.json', 'w') as outfile:
    json.dump(json_data, outfile)