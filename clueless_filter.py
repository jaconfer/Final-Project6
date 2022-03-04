import re

cl_script = open('clueless.txt', 'r').read()
cl_list = re.split('\.\n|\?\n|!\n', cl_script)

cl_utters = []
for item in cl_list:
    line = item.replace('\n', '')
    if re.search('\slike,\s', line):
        cl_utters.append(line)
with open('clueless_likes.txt', 'w') as cll:
    for item in cl_utters:
        cll.write('\n>'+item)

