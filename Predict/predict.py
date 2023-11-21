import os
import glob
import pandas as pd
import json
from joblib import load

# 필요한 함수를 import합니다. 이 함수들은 리뷰 텍스트 처리에 사용됩니다.
from train import tokenize_korean_text, remove_locations

def load_model_and_vectorizer(review_type):
    # 저장된 모델과 벡터라이저를 불러옵니다.
    model = load(f'sgd_model_{review_type}.joblib')
    vectorizer = load(f'vectorizer_{review_type}.joblib')
    return model, vectorizer

def process_file(file_path, model, vectorizer, name_key):
    # 파일 경로에서 국가명을 추출합니다.
    cnt_name = os.path.basename(file_path).split('_')[0]
    review_summary = {}
    
    # JSON 파일을 열어 데이터를 로드합니다.
    with open(file_path, 'r', encoding='utf-8') as file:
        reviews_data = json.load(file)
        # 리뷰 데이터를 순회하며 긍정 및 부정 리뷰의 개수를 집계합니다.
        for review in reviews_data:
            region = review.get('region', 'Unknown')
            review_name = review.get(name_key, 'Unknown')
            # 집계를 위한 딕셔너리를 초기화합니다.
            review_summary.setdefault(region, {}).setdefault(review_name, {'pos': 0, 'neg': 0})
            # 리뷰 텍스트를 처리하여 분석 준비를 합니다.
            text_to_analyze = ' '.join(tokenize_korean_text(remove_locations(review['title'] + " " + review['content'], [region])))
            # 텍스트를 벡터화하고 모델을 사용하여 예측합니다.
            comment_vector = vectorizer.transform([text_to_analyze])
            prediction = model.predict(comment_vector)
            # 예측 결과에 따라 긍정 또는 부정 리뷰의 개수를 업데이트합니다.
            count_key = 'pos' if prediction == 1 else 'neg'
            review_summary[region][review_name][count_key] += 1
            
    return cnt_name, review_summary

def save_results(results, output_directory, review_type):
    # 결과 데이터를 DataFrame으로 변환하고 CSV 파일로 저장합니다.
    df_results = pd.DataFrame(results)
    output_file = os.path.join(output_directory, f'{review_type}_review_analysis.csv')
    df_results.to_csv(output_file, index=False, encoding='utf-8-sig')

def analyze_reviews(review_type, data_directory, output_directory):
    # 모델과 벡터라이저를 불러옵니다.
    model, vectorizer = load_model_and_vectorizer(review_type)
    # 리뷰 유형에 따라 사용할 키를 설정합니다.
    name_key = 'attr_name' if review_type == 'attr' else 'hotel_name'
    # 파일 패턴을 정의하고 일치하는 파일을 찾습니다.
    file_pattern = os.path.join(data_directory, f'*_{review_type}_review_recent.json')
    review_files = glob.glob(file_pattern)
    results = []

    # 각 파일을 처리하고 결과를 집계합니다.
    for file_path in review_files:
        print(f'Analyzing {file_path}...')
        cnt_name, review_summary = process_file(file_path, model, vectorizer, name_key)
        # 집계된 데이터를 결과 리스트에 추가합니다.
        for region, names in review_summary.items():
            for name, counts in names.items():
                results.append({
                    'CNT_NAME': cnt_name,
                    'REG_NAME': region,
                    f'{review_type.upper()}_NAME': name,
                    'REV_POS': counts['pos'],
                    'REV_NEG': counts['neg']
                })

    # 결과를 저장합니다.
    save_results(results, output_directory, review_type)

if __name__=='__main__':
    data_directories = {
        'attr': '../Data/Review_Data/Attr_Review',
        'accom': '../Data/Review_Data/Accom_Review'
    }
    output_directory = '../Data/Predicted_Data'

    for review_type in ['attr', 'accom']:
        analyze_reviews(review_type, data_directories[review_type], output_directory)
