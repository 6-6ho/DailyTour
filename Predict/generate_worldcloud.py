import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os
import glob
import json
from predict import remove_locations

def parse_json_to_string(dir_path):
    text_data = []

    pattern = os.path.join(dir_path, '*_review_recent.json')
    json_files = glob.glob(pattern)

    for json_file in json_files:
        with open(json_file, 'r', encoding='utf-8') as file:
            review = json.load(file)
            extracted_text = remove_locations(review['title'] + " " + review['content'], review['region'])
        
        text_data.extend(extracted_text)

    return text_data

def generate_wordcloud(text):
    # WordCloud 객체 생성 및 설정
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    # 워드클라우드를 그림으로 표시
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
    
def save_wordcloud(wordcloud):
    file_name = f'{attr_code}worldcloud.png'
    wordcloud.to_file(file_name)
    
    print(f'save file : {file_name}')
    
    
if __name__=='__main__':
    dir_path = ['../Data/Accom_Review', '../Data/Attr_Review']
    
    for dir_name in dir_path:
        generate_wordcloud(dir_name)
    
    