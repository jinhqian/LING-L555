import sys

hanza = open ('hanza.txt', 'r')
hanza_list = hanza.readlines()
#print(hanza_list)

hangul = open ('hangul.txt', 'r')
hangul_list = hangul.readlines()
#print(hangul_list)

All_hanzas = 0
All_tokens = 0

my_dict = {}
for (hangul_word, hanza_word) in zip(hangul_list, hanza_list):
    my_dict[hangul_word.strip()] = hanza_word.strip()
#print(my_dict)

for block in sys.stdin.read().split('\n\n'):
    hanzacount = 0
    tokencount = 0
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
        tokencount = tokencount +1
        if form in my_dict:
            hanzacount = hanzacount + 1
            row[9] = 'Hanza=%s' % (my_dict[form])
        print('\t'.join(row))

    print('#Hanza: %d' % (hanzacount)) #total number of hanza appeared in every sentence.
    print('#Token: %d' % (tokencount)) #total tokens of every sentence.

    hanzarate = ( hanzacount / tokencount ) if tokencount != 0 else 0
    print('#Hanza_rate='"{0:.0%}".format(hanzarate)) #rate of hanza in total tokens from one sentence.

    All_hanzas = All_hanzas + hanzacount
    All_tokens = All_tokens + tokencount

print('\n#Total_hanzas: %d' % (All_hanzas)) # total hanzas from the whole text.
print('#Total_tokens: %d' % (All_tokens)) #total tokens from the whole text.
print('#Total_rate='"{0:.0%}".format(All_hanzas/All_tokens)) #rate of total hanza in total tokens from the whole text.
