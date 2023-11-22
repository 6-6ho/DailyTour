import os
import json

def flatten_json_list(file_path):
    # 파일을 열어 JSON 데이터를 로드합니다.
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # 중첩된 JSON 리스트를 평탄화합니다.
    flattened_data = [item for sublist in data for item in sublist]

    # 평탄화된 데이터를 같은 파일에 다시 저장합니다.
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(flattened_data, file, ensure_ascii=False, indent=4)

def process_json_files(directory):
    # 주어진 디렉토리에서 모든 JSON 파일을 찾아 처리합니다.
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            flatten_json_list(file_path)  # 각 JSON 파일을 평탄화하는 함수를 호출합니다.

# 처리할 JSON 파일이 저장된 디렉토리의 경로를 설정합니다.
directory_path = '../Data/Review_Data/Accom_Review'
# 디렉토리 내의 모든 JSON 파일을 평탄화하는 함수를 호출합니다.
process_json_files(directory_path)
