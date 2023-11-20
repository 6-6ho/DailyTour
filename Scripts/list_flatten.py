import os
import json

def flatten_json_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        
    flattened_data = [item for sublist in data for item in sublist]

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(flattened_data, file, ensure_ascii=False, indent=4)

def process_json_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            flatten_json_list(file_path)

directory_path = '../Data/Review_Data/Accom_Review'
process_json_files(directory_path)
