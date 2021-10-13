import sys

symbol = {}

fd = open('trans.txt', 'r')

for line in fd.readlines():
    line = line.strip('\n')
    (s, w) = line.split('\t')
    symbol[s] = w

for line in sys.stdin.readlines():
    line = line.strip('\n')
    if '\t' not in line:
        print(line)
        continue
    row = line.split('\t')
    if len(row) != 10:
        print(line)
        continue
    form = row[1]
    for character in symbol:
        form = form.replace(character, symbol[character])
    if form.isalpha():
        row[9] = 'IPA=%s' % (form)
    print('\t'.join(row))

