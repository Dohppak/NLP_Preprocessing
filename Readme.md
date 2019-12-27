### 어절 분석
`preprocessing.py`
- 파이썬 split함수

### 정규표현식으로 한글만 남기기
`preprocessing.py`
- re.compile('[^ ㄱ-ㅎ | 가-힣]+')

### 형태소 분석
`pos_tagger.py`
- requirements : konlpy
    - https://konlpy-ko.readthedocs.io/ko/v0.4.3/
    - https://medium.com/@jjeaby/osx-mojave-%EC%97%90%EC%84%9C-mecab-python3-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0-c007bcb19189
    - https://blog.naver.com/PastView.nhn?blogId=coldoutside&logNo=221449433535&from=search&redirect=Log&widgetTypeCall=true&directAccess=false
- 형태소 태그 정보
    - https://docs.google.com/spreadsheets/d/1OGAjUvalBuX-oZvZ_-9tEfYD2gQe7hTGsgUpiiBSXI8/edit#gid=0

- user_dict : 고유명사를 지정하게 해줌


### Result
```
python preprocessing.py 
```
##### Query : "Oh...! Wow, 도승헌 한국어 어절 분석기를 열심히 만들고있네요. 이 친구는 한글만 리턴시키지"
- ['', '', '도승헌', '한국어', '형태소', '분석기를', '열심히', '만들고있네요', '이', '친구는', '한글만', '리턴시키지']


```
python pos_tagger.py 
```
##### 그냥 형태소 분석기 
- ['도승헌/NNP', '한국어/NNP', '형태소/NNP', '분석기/NNG', '를/JKO', '열심히/MAG', '만들/VV', '고/EC' , '있/VX', '네요/EF', './SF', '이/MM', '친구/NNG', '는/JX', '그냥/MAG', '포스태깅/NA']
##### 특정 형태소, 용언만 남기고 태그 
- ['도승헌', '한국어', '형태소', '분석기', '만들', '친구', '용언', '남기', '형용사', '동사', '명사']
