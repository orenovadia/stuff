from compress import _iter_words
all_words = 'all_words'
ofile = 'bad_words'
s1 = set()
for word in _iter_words('words.txt'):
    s1.add(word)
s2 = set()
for word in _iter_words(all_words):
    s2.add(word)
s3 = s2 - s1
for i in s3:
    print i
with open(ofile,'wb') as fout:
    for word  in s3:
        fout.write(word + '\n')

