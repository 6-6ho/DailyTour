import json
import pandas as pd
import glob
import os

def func(review_type, data_directory, output_directory):
    file_pattern = os.path.join(data_directory, f'*_{review_type}_review_recent.json')
    review_files = glob.glob(file_pattern)

    all_data = []  # 모든 파일의 데이터를 저장할 리스트

    for file_path in review_files:
        name_key = 'attr_name' if review_type == 'attr' else 'hotel_name'
        print(f"Processing file: {file_path}")  # 파일명 출력
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            content_scores = {}
            for entry in data:
                content_name = entry[name_key]
                score = int(entry['score'])
                if content_name in content_scores:
                    content_scores[content_name].append(score)
                else:
                    content_scores[content_name] = [score]

            
            for content, scores in content_scores.items():
                average_score = round(sum(scores)/len(scores), 2)
                name_key = 'attr_name' if review_type == 'attr' else 'accom_name'
                all_data.append({f'{name_key.upper()}': content, 'SCORE': average_score})

    # 모든 데이터를 포함하는 DataFrame 생성
    df = pd.DataFrame(all_data)
    output_file_name = f'{review_type}_review_avg_scores.csv'
    output_path = os.path.join(output_directory, output_file_name)
    df.to_csv(output_path, index=False, encoding='utf-8')

if __name__=='__main__':
    data_directories = {
        'attr': '../Data/Review_Data/Attr_Review',
        'accom': '../Data/Review_Data/Accom_Review'
    }
    output_directory = '../Data/Predicted_Data'

    for review_type in ['attr', 'accom']:
        func(review_type, data_directories[review_type], output_directory)
