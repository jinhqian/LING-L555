import sys

index = 1

line = sys.stdin.readline()

while line:
    print('# sent_id = %d' % (index))
    index = index + 1
    print('# text = %s' % (line))
    tokens = line.replace(',', ' ,').replace('.', ' . ').replace("'", " ' ").replace(':', ' :').replace('and', ' and ').replace('(', ' (').replace(')', ' )').replace('"', ' " ').replace('  ', ' ').split()
    token_id = 1
    for token in tokens:
        print('%d\t%s\t_\t_\t_\t_\t_\t_\t_\t_' % (token_id,token))
        token_id = token_id + 1
    print()
    line = sys.stdin.readline()
