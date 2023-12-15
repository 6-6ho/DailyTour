import os
import glob
import json
from konlpy.tag import Okt
from wordcloud import WordCloud
import numpy as np
from PIL import Image

img_mask = np.array(Image.open('airplane.png'))

def text_normalization(text: str)-> str:
    okt = Okt()
    # 제외하고 싶은 단어들의 리스트
    stopwords = {'해외여행', '해외', '여행', '것', '등', '수', '올해', '지역', '중', '명', '경우', '예약', '여행객', '여행사', '관계자', '항공사', '최근',
                 '상품', '수요', '한국', '노선', '한국인', '현재', '기록', '국내', '증가', '약', '더', '인기', '상황', '및', '위', '라며', '전', '주'
                 , '지난해', '이후', '이', '때문', '국가', '전체', '대한', '지난', '가장', '말', '방분'}
    return ' '.join(
        word for word, tag in okt.pos(text, stem=True)
        if tag in ['Noun', 'Adjective'] and not word.endswith('다') and word not in stopwords
    )

def load_news_file() -> None:
    file_path = f'../Data/News_Data/travel_news.json'
    with open(file_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)
        
        articles = json_data["travel_news"]
        
        concat_text = ''
        
        for article in articles:
            title = article["news_title"]
            content = article["news_content"]
            concatenated_text = f"{title} {content} "
            concat_text += concatenated_text
        
    generate_wordcloud(concat_text)

def generate_wordcloud(text):
    normed_text = text_normalization(text)
    
    wordcloud = WordCloud(width=300, height=200, max_words=200, max_font_size=50, min_font_size=13, mask=img_mask,
                          background_color='white', font_path="C:\Windows\Fonts\H2HDRM.TTF").generate(normed_text)
    save_wordcloud(wordcloud)

def save_wordcloud(wordcloud):
    save_path = '../Data/News_Data/'
    file_name = 'news_wordcloud.png'
    wordcloud.to_file(save_path + file_name)

    print(f'save file : {file_name}')


if __name__ == '__main__':
    load_news_file()