# Python program to read
# json file


import json

# Opening JSON file
f = open('infonfl.json')

# returns JSON object as
# a dictionary
data = json.load(f)

#Find Keys
nflids = data.keys()

lines = []
for id in nflids:
    #print (data[id]['full_name'])
    if 'height' in data[id]:
        h=data[id]['height']
    else:
        h=0
    if 'weight' in data[id]:
        w=data[id]['weight']
    else:
        w=0
    #print (h,',',w,',',data[id]['full_name'])
    line = "%d,%d,%s\n" % (h,w,data[id]['full_name'])
    lines.append(line)
# create file
with open('nfl.csv', 'w') as f:
    for l in lines:
        f.write(l)


# Closing file
f.close()