from konlpy.tag import Kkma
from konlpy.tag import Okt
from collections import Counter
import pandas as pd
import nltk
import json
import matplotlib.pyplot as plt
# %matplotlib inline 
from wordcloud import WordCloud, STOPWORDS


def remove_special_chars(text):
    text = re.sub('[^가-힣a-zA-Z0-9\s]', '', text)  # 한글, 영문, 숫자, 공백 제외한 모든 문자 제거
    text = re.sub('\s+', ' ', text) # 개행 제거
    return text


def json_to_dict(): 
    with open('./Data/News_Data/travel_news.json', 'r', encoding='utf8') as f:
        news_list = json.load(f)

    new_content = []


# spwords = set(STOPWORDS)

# wordcloud = WordCloud(max_font_size=200,
#              font_path='c:/Windows/fonts/malgun.ttf',
#   #          font_path = "/System/Library/fonts/AppleSDGothicNeo.ttc",  # Mac OS
#              stopwords=spwords,background_color='#FFFFFF',
#              width=1200,height=800).generate(news_list[n])
# plt.figure(figsize=(10,8))
# plt.imshow(wordcloud)
# plt.tight_layout(pad=0)
# plt.axis('off')

# # 워드 클라우드를 파일로 저장 
# plt.savefig('wordcloud_image2.png', bbox_inches='tight')
# plt.show()


    
    
        