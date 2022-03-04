import re

cl_script = open('clueless.txt', 'r').read()
cl_list = re.split('\.\n|\?\n|!\n', cl_script)

cl_utters = []
for item in cl_list:
    line = item.replace('\n', '')
    if re.search('\slike,\s|Like,\s', line):
        line2 = re.sub('\slike,\s|Like,\s', ' LIKE, ---$--- ', line)
        cl_utters.append(line2)
with open('clueless_likes.txt', 'w') as cll:
    for item in cl_utters:
        cll.write('\n>'+item)
