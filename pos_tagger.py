from konlpy.tag import Komoran

pos_tagger = Komoran(userdic='./user_dic.txt')
def tokenize(doc, pos_tagger):
    return ['/'.join(t) for t in pos_tagger.pos(doc)]

# example of pos tagger
print("그냥 형태소 분석기 \t")
print(tokenize("도승헌 한국어 형태소 분석기를 열심히 만들고있네요. 이 친구는 그냥 포스태깅", pos_tagger))


save_item = ('NNG','NNP','VV','VA')
def tokenizer_not_remove(doc, pos_tagger):
    item = tokenize(doc, pos_tagger)
    dummy = []
    for indi in item:
        if (indi.split('/')[1] in save_item):
            dummy.append(indi.split('/')[0])
    return dummy

# example of 용언만 남기기
print("특정 형태소, 용언만 남기고 태그 \t")
print(tokenizer_not_remove("도승헌 한국어 형태소 분석기를 열심히 만들고있네요. 이 친구는 용언만 남기자 형용사 동사 명사", pos_tagger))
