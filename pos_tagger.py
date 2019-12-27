
from konlpy.tag import Okt

pos_tagger = Okt()

def tokenize(doc):
    return ['/'.join(t) for t in pos_tagger.pos(doc, norm=True, stem=True)]

print(tokenize("안녕하세요, 저는 도승헌입니다."))