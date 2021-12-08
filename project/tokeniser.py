import sys

index = 1

line = sys.stdin.readline()

while line:
    print('# sent_id = %d' % (index))
    index = index + 1
    print('# text = %s' % (line.strip()))
    tokens = line.replace('”', ' ” ').replace('“', ' “ ').replace('·', ' · ').replace(',', ' ,').replace('.', ' . ').replace("'", " ' ").replace(':', ' :').replace('~', ' ~ ').replace('(', ' ( ').replace(')', ' )').replace('"', ' " ').replace('에', ' 에').replace('은', ' 은').replace('는', ' 는').replace('으로',' 으로').replace('에서', ' 에서').replace('이다', ' 이다').replace('한다', ' 한다').replace(' \n', '\n').replace('\n ', '\n').replace('부터', ' 부터').split()
    token_id = 1
    for token in tokens:
        print('%d\t%s\t_\t_\t_\t_\t_\t_\t_\t_' % (token_id,token))
        token_id = token_id + 1
    print()
    line = sys.stdin.readline()
