import re

rm_script = open('ridgemont.txt', 'r').read()
rm_list = re.split('\.\n|\?\n|!\n', rm_script)

rm_utters = []
for item in rm_list:
    line = item.replace('\n', '')
    if re.search('\slike,\s|Like,\s', line):
        line2 = re.sub('\slike,\s|Like,\s', ' LIKE, ---$--- ', line)
        rm_utters.append(line2)
with open('ridgemont_likes.txt', 'w') as rml:
    for item in rm_utters:
        rml.write('\n>'+item)
