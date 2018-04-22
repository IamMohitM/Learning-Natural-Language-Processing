import nltk
from pickle import load
input = open('C:\\Users\\mohit\\Desktop\\Natural Language Processing\\tagger.pkl', 'rb')
tagger = load(input)
input.close()

def tag(sent):
    sent = sent[0].title() + sent[1:]
    print(sent)
    tokens = nltk.word_tokenize(sent)
    sent_tags = tagger.tag(tokens)
    tags = {}
    for x, y in sent_tags:
        if y not in tags.keys():
            tags[y] = [x]
        else:
            tags[y].append(x)
    return dict(tags)


print(tag('Please close Youtube'))
print(tag('close Youtube'))
print(tag('play a Song'))
print(tag('shutdown Youtube'))
