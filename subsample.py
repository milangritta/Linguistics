import codecs

counter = 0
out = codecs.open("../data/train_wiki_uniform.txt", "w", encoding="utf-8")
for line in codecs.open("../data/train_wiki.txt", "r", encoding="utf-8"):
    if counter % 3 == 0:
        out.write(line)
    counter += 1