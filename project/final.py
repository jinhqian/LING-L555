import sys

hanza = open ('hanza.txt', 'r')
hanza_list = hanza.readlines()
#print(hanza_list)

hangul = open ('hangul.txt', 'r')
hangul_list = hangul.readlines()
#print(hangul_list)

my_dict = {}
for (hangul_word, hanza_word) in zip(hangul_list, hanza_list):
    my_dict[hangul_word.strip()] = hanza_word.strip()
#print(my_dict)

#freqdict = {}

for block in sys.stdin.read().split('\n\n'):
    hanzacount = 0
    hangulcount = 0
    if block.strip() == '':
        continue
    for line in block.split('\n'):
        line = line.strip('\n')
        if '\t' not in line:
            print(line)
            continue
        row = line.split('\t')
        if len(row) != 10:
            print(line)
            continue
        form = row[1]
        hangulcount = hangulcount +1
        if form in my_dict:
            hanzacount = hanzacount + 1
            row[9] = 'Hanza=%s' % (my_dict[form])
            #countlist=[]
            #countlist.append(my_dict[form]) 
        #print(countlist)
        print('\t'.join(row))

    print('+Hanza: %d' % (hanzacount))
    print('+Hangul: %d' % (hangulcount))

    hanzarate = ( hanzacount / hangulcount ) if hangulcount != 0 else 0
    #print(round(c,2))
    print('+Hanza_rate='"{0:.0%}".format(hanzarate))
