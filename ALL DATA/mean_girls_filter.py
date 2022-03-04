import re

mg_script = open('mean_girls.txt', 'r').read()
mg_list = re.split('\.\n|\?\n|!\n', mg_script)

mg_utters = []
for item in mg_list:
    line = item.replace('\n', '')
    if re.search('\slike,\s|^Like,\s', line):
        line2 = re.sub('\slike,\s|Like,\s', ' LIKE, ---$--- ', line)
        mg_utters.append(line2)
#opens and writes the results into a txt file
with open('mean_girls_likes.txt', 'w') as mgl:
    for item in mg_utters:
        mgl.write('\n>'+item)