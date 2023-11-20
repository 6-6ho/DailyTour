import glob
import json
import hashlib
import os

def remove_duplicates_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    unique_data = []
    seen_hashes = set()

    for item in data:
        # dict to string, hashing
        item_hash = hashlib.sha256(json.dumps(item, sort_keys=True).encode('utf-8')).hexdigest()
        if item_hash not in seen_hashes:
            seen_hashes.add(item_hash)
            unique_data.append(item)

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(unique_data, file, ensure_ascii=False, indent=4)

directories = [
    '../Data/Review_Data/Accom_Review',
    '../Data/Review_Data/Attr_Review'
]

for directory in directories:
    json_files = glob.glob(os.path.join(directory, '*.json'))
    for file_path in json_files:
        print(f'Removing duplicates from: {file_path}')
        remove_duplicates_from_json(file_path)
