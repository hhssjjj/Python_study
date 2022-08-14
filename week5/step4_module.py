from re import sub

st3 = 'test^홍길동 abc 대한*민국 123$tbc'

#(1) 특수문자 제거
text1 = sub('[\^*$]+', '', st3)
print(text1)

#(2) 숫자 제거
text2 = sub('[0-9]', '', text1)
print(text2)


#텍스트
texts = ['우리나라 땡땡 대한민국, 우리나라%$ 만세', '보험료 15000원에 평생 보장 마감임박 개이득 ', '나는 홍길동 hogitld 헐랭']

not_allow = ['땡땡', '개이득', '헐랭']


def clean_text(text_string):
    clean_text = sub('[\^*#@%$]+', '', text_string) #특수문자 걸러낸 문자열
    clean_text = sub('[0-9]', '', clean_text) #숫자제거
    clean_text = clean_text.upper() #소문자, 대문자 전처리
    #비속어 제거
    for bad_word in not_allow:
        clean_text = sub(bad_word, '***', clean_text)
    return clean_text

for txt in texts:
    print('전처리 전:', txt)
    print('전처리 후:', clean_text(txt))


#리스트 내포

clean_texts = [ clean_text(txt) for txt in texts ]
print(clean_texts)












