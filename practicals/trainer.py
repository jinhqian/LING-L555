import sys

countlist = []
m_words = {}
m_tags = {}
freqdict = {} #frequency of [word,tag]
totaltokens = 0

for line in sys.stdin.readlines():

    line = line.strip('\n')

    if '\t' not in line:
        continue
#    if len(line) > 0 and line[0] == '#':
#        continue
    row = line.split('\t')
    word = row[1]
    tag = row[3]
    countlist.append((word,tag))
    totaltokens = totaltokens + 1
    
#print(countlist)

for word, tag in countlist :
    if word not in freqdict:
        freqdict[word] = 0
    freqdict[word] = freqdict[word] + 1
    
#print(freqdict)

for (word, tag) in countlist:
    if tag not in m_tags:
        m_tags[tag] = 0
    m_tags[tag] = m_tags[tag] + 1
    if word not in m_words :
        m_words[word] = {}
    if tag not in m_words[word]:
        m_words[word][tag] = 0
    m_words[word][tag] = m_words[word][tag] + 1
#print(m_words)
print('#P\tcount\ttag\tword')
for tag in m_tags:
    print(round(m_tags[tag]/totaltokens, 2),'\t', m_tags[tag],'\t', tag,'\t', '_')

for word in m_words:
    for tag in m_words[word]:
            print(m_words[word][tag]/freqdict[word],'\t', m_words[word][tag],'\t', tag, '\t', word)
