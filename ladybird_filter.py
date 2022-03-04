import re

lb_script = open('ladybird.txt', 'r').read()
lb_list = re.split('\.\n|\?\n|!\n', lb_script)

lb_utters = []
for item in lb_list:
    line = item.replace('\n', '')
    if re.search('\slike,\s|Like,\s', line):
        line2 = re.sub('\slike,\s|Like,\s', ' LIKE, ---$--- ', line)
        lb_utters.append(line2)
with open('ladybird_likes.txt', 'w') as lbl:
    for item in lb_utters:
        lbl.write('\n>'+item)

