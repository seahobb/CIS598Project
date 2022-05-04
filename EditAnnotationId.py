import json
import os

folderPath = 'C:\\Users\\jmyos\\OneDrive - Kansas State University\\598\\CIS598Project\\CIS598Project\\EditAnnotations'

#jsonList = os.listdir(folderPath)

with open('C:\\Users\\jmyos\\OneDrive - Kansas State University\\598\\CIS598Project\\CIS598Project\\EditAnnotations\\_annotations.cocotrain.json', 'r') as file:
    data = json.load(file)
    num = 0
    for i in data['annotations']:
        num = i['id']
        i['id'] = num + 3638
        print(i['id'])
        #730 for valid
        #781 for test
        #3638 for train

with open('C:\\Users\\jmyos\\OneDrive - Kansas State University\\598\\CIS598Project\\CIS598Project\\EditAnnotations\\_annotations.cocotrain2.json', 'w') as file:
    json.dump(data, file)