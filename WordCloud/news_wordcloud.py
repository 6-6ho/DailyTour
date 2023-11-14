from konlpy.tag import Kkma
from konlpy.tag import Okt
from collections import Counter
import pandas as pd
import nltk
import json
import matplotlib.pyplot as plt
# %matplotlib inline 
from wordcloud import WordCloud, STOPWORDS

with open('travel_news.json', 'r', encoding='utf8') as f:
    news_list = json.load(f)

df = []



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


    
    
        