import os
import glob
import pandas as pd
import json
from joblib import load

# train.py에서 필요한 함수를 가져옵니다.
from train import tokenize_korean_text, remove_locations

def load_model_and_vectorizer(review_type):
    model = load(f'sgd_model_{review_type}.joblib')
    vectorizer = load(f'vectorizer_{review_type}.joblib')
    return model, vectorizer

def process_file(file_path, model, vectorizer, name_key):
    cnt_name = os.path.basename(file_path).split('_')[0]
    review_summary = {}
    
    with open(file_path, 'r', encoding='utf-8') as file:
        reviews_data = json.load(file)
        for review in reviews_data:
            region = review.get('region', 'Unknown')
            review_name = review.get(name_key, 'Unknown')
            review_summary.setdefault(region, {}).setdefault(review_name, {'pos': 0, 'neg': 0})
            text_to_analyze = ' '.join(tokenize_korean_text(remove_locations(review['title'] + " " + review['content'], [region])))
            comment_vector = vectorizer.transform([text_to_analyze])
            prediction = model.predict(comment_vector)
            count_key = 'pos' if prediction == 1 else 'neg'
            review_summary[region][review_name][count_key] += 1
            
    return cnt_name, review_summary

def save_results(results, output_directory, review_type):
    df_results = pd.DataFrame(results)
    output_file = os.path.join(output_directory, f'{review_type}_review_analysis.csv')
    df_results.to_csv(output_file, index=False, encoding='utf-8-sig')

def analyze_reviews(review_type, data_directory, output_directory):
    model, vectorizer = load_model_and_vectorizer(review_type)
    name_key = 'attr_name' if review_type == 'attr' else 'hotel_name'
    pos_key = f'{review_type.upper()}_REV_POS'
    neg_key = f'{review_type.upper()}_REV_NEG'
    file_pattern = os.path.join(data_directory, f'*_{review_type}_review_recent.json')
    review_files = glob.glob(file_pattern)
    results = []

    for file_path in review_files:
        print(f'Analyzing {file_path}...')
        cnt_name, review_summary = process_file(file_path, model, vectorizer, name_key)
        for region, names in review_summary.items():
            for name, counts in names.items():
                results.append({
                    'CNT_NAME': cnt_name,
                    'REG_NAME': region,
                    f'{review_type.upper()}_NAME': name,
                    pos_key: counts['pos'],
                    neg_key: counts['neg']
                })

    save_results(results, output_directory, review_type)

if __name__=='__main__':
    data_directories = {
        'attr': '../Data/Review_Data/Attr_Review',
        'accom': '../Data/Review_Data/Accom_Review'
    }
    output_directory = '../Data/Predicted_Data'

    for review_type in ['attr', 'accom']:
        analyze_reviews(review_type, data_directories[review_type], output_directory)
