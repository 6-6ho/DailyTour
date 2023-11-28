import os
import glob
import json
import matplotlib.pyplot as plt
from konlpy.tag import Okt
from typing import Dict
import pandas as pd
from train import remove_locations
from wordcloud import WordCloud


def text_normalization(text):
    okt = Okt()
    # 제외하고 싶은 단어들의 리스트
    stopwords = {'곳', '수', '것', '때', '의', '그', '이'}
    return ' '.join(
        word for word, tag in okt.pos(text, stem=True)
        if tag in ['Noun', 'Adjective'] and not word.endswith('다') and word not in stopwords
    )

def get_attr_code(attr_name):
    print('get attr code')
    attr_code_df = pd.read_csv('../Data/DB/REG_ATTRS_TB.csv')
    attr_code = attr_code_df[attr_code_df['ATTR_NAME']
                             == attr_name]['ATTR_CODE'].values[0]

    return attr_code


def load_review_files(review_type: str) -> None:
    dir_path = f'../Data/Review_Data/{review_type.upper()}_Review'
    pattern = os.path.join(dir_path, '*_review_recent.json')
    json_files = glob.glob(pattern)

    for json_file in json_files:
        data = parse_json_to_string(json_file)
        for item_name, text_data in data.items():
            generate_wordcloud(text_data, item_name)


def parse_json_to_string(json_file):
    print('parse json')
    # 각 관광지에 대한 텍스트 데이터를 저장할 딕셔너리
    attraction_data = {}

    with open(json_file, 'r', encoding='utf-8') as file:
        reviews = json.load(file)
        for review in reviews:
            # 관광지 이름에서 선행 공백을 제거
            attr_name = review['attr_name'].lstrip()
            # 제목과 내용을 결합하고 위치 정보를 제거
            extracted_text = remove_locations(review['title'] + " " + review['content'], review['region'])
            # 관광지가 이미 존재하면 텍스트에 추가하고, 그렇지 않으면 새로운 항목을 생성
            if attr_name in attraction_data:
                attraction_data[attr_name] += " " + extracted_text
            else:
                attraction_data[attr_name] = extracted_text

    # 각 관광지에 대해 누적된 텍스트 데이터를 반환
    return attraction_data

def generate_wordcloud(text, attr_name):
    print('gen wordcloud')
    normed_text = text_normalization(text)
    wordcloud = WordCloud(width=800, height=400,
                          background_color='white', font_path="C:\Windows\Fonts\H2HDRM.TTF").generate(normed_text)

    save_wordcloud(wordcloud, attr_name)


def save_wordcloud(wordcloud, attr_name):
    print('save')
    save_path = '../Data/word-cloud/'
    attr_code = get_attr_code(attr_name)
    file_name = f'{attr_code}_worldcloud.png'
    wordcloud.to_file(save_path + file_name)

    print(f'save file : {file_name}')


if __name__ == '__main__':
    review_types = ['attr', 'accom']

    for review in review_types:
        load_review_files(review)
