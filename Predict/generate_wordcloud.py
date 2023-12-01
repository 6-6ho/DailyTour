import os
import glob
import json
from konlpy.tag import Okt
import pandas as pd
from train import remove_locations
from wordcloud import WordCloud
from PIL import Image
import pandas as np

img_mask = np.array(Image.open('heart_shape.png'))

def text_normalization(text: str)-> str:
    okt = Okt()
    # 제외하고 싶은 단어들의 리스트
    stopwords = {'곳', '수', '것', '때', '의', '그', '이', '호텔', '숙소', '방', '위', '진짜', '위치', '좀', '아', '매우', '많이'}
    return ' '.join(
        word for word, tag in okt.pos(text, stem=True)
        if tag in ['Noun', 'Adjective'] and not word.endswith('다') and word not in stopwords
    )

def get_item_code(item_name: str, item_type: str) -> str:
    if item_type == 'attr':
        df = pd.read_csv('../Data/DB/REG_ATTRS_TB.csv')
        filtered_df = df[df['ATTR_NAME'] == item_name]
    elif item_type == 'accom':
        df = pd.read_csv('../Data/DB/REG_ACCOM_TB.csv')
        filtered_df = df[df['ACCOM_NAME'] == item_name]

    if not filtered_df.empty and not pd.isna(filtered_df['ATTR_CODE' if item_type == 'attr' else 'ACCOM_CODE'].values[0]):
        return filtered_df['ATTR_CODE' if item_type == 'attr' else 'ACCOM_CODE'].values[0]
    else:
        return None


def load_review_files(item_type: str) -> None:
    print('load_review_files')
    dir_path = f'../Data/Review_Data/{item_type.upper()}_Review'
    pattern = os.path.join(dir_path, '*_review_recent.json')
    json_files = glob.glob(pattern)

    for json_file in json_files:
        data = parse_json_to_string(json_file, item_type)
        for item_name, text_data in data.items():
            generate_wordcloud(text_data, item_name, item_type)


def parse_json_to_string(json_file, item_type):
    print('parse_json_to_string')
    # 각 item에 대한 텍스트 데이터를 저장할 딕셔너리
    item_data = {}

    with open(json_file, 'r', encoding='utf-8') as file:
        item_reviews = json.load(file)
        for item_review in item_reviews:
            # 선행 공백을 제거
            if item_type == 'accom':
                item_name = item_review['hotel_name'].lstrip()
            else:
                item_name = item_review['attr_name'].lstrip()
            # 제목과 내용을 결합하고 위치 정보를 제거
            extracted_text = remove_locations(item_review['title'] + " " + item_review['content'], item_review['region'])
            # item이 이미 존재하면 텍스트에 추가하고, 그렇지 않으면 새로운 항목을 생성
            if item_name in item_data:
                item_data[item_name] += " " + extracted_text
            else:
                item_data[item_name] = extracted_text

    # 각 관광지에 대해 누적된 텍스트 데이터를 반환
    return item_data

def generate_wordcloud(text, item_name, item_type):
    print('generate_wordcloud')
    normed_text = text_normalization(text)
    item_code = get_item_code(item_name, item_type)
    
    if item_code:
        word_count = len(normed_text.split())
        if word_count >= 10:
            try:
                wordcloud = WordCloud(width=400, height=200, max_words=100, mask=img_mask,
                                      background_color='white', font_path="C:\Windows\Fonts\H2HDRM.TTF").generate(normed_text)
                save_wordcloud(wordcloud, item_code)
            except ValueError:
                print(f'Not enough words to create a word cloud for: {item_name}')
        else:
            print(f'Not generating word cloud for {item_name}: Word count is less than 5')
    else:
        print(f'Item code not found for: {item_name}')


def save_wordcloud(wordcloud, item_code):
    save_path = '../Data/word-cloud/'
    file_name = f'{item_code}_worldcloud.png'
    wordcloud.to_file(save_path + file_name)

    print(f'save file : {file_name}')


if __name__ == '__main__':
    item_types = ['accom']

    for item in item_types:
        load_review_files(item)
