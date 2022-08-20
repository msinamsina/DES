import json


permissions = list()
permissions.append('Can add user')
permissions.append('Can change user')
permissions.append('Can delete user')
permissions.append('Can add group')
permissions.append('Can change group')
permissions.append('Can delete group')
permissions.append('Can add permission')
permissions.append('Can change permission')
permissions.append('Can delete permission')
permissions.append('Can send email')
permissions.append('Can see all articles')
permissions.append('Can see all users')
permissions.append('Can change accepted articles')
permissions.append('Can change presented articles')
permissions.append('Can change paid articles')

json_data = []
for idx, permition in enumerate(permissions):
    json_data.append({
    "model": "email_sender.permission",
    "pk": len(json_data) + idx,
    "fields": {
      "id": idx,
      "title": permition
    }})

with open('fixtures/email_sender/permissions.json', 'w') as outfile:
    json.dump(json_data, outfile)