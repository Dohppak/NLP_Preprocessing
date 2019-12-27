import re

def split(doc):
    return doc.split()

def only_hangul(doc):
    token = split(doc)
    docs = []
    for i in token:
        hangul = re.compile('[^ ㄱ-ㅎ | 가-힣]+')
        result = hangul.sub('',i)
        final = result.strip()
        docs.append(final)
    return docs

print(only_hangul("Oh...! Wow, 도승헌 한국어 어절 분석기를 열심히 만들고있네요. 이 친구는 한글만 리턴시키지"))
