import json

def merge_datasets(recent_data, train_data):
    recent_dict = {}
    review_counts = {}
    merged_data = []

    # 먼저 recent_data를 merged_data에 추가
    merged_data.extend(recent_data)

    for review in recent_data:
        attr_name = review['attr_name']
        if attr_name not in recent_dict:
            recent_dict[attr_name] = []
        recent_dict[attr_name].append(review['title'])

        # 초기화
        if attr_name not in review_counts:
            review_counts[attr_name] = {'positive': 0, 'negative': 0}

    for review in train_data:
        attr_name = review['attr_name']
        if attr_name in recent_dict:
            if review['title'] not in recent_dict[attr_name]:
                pos_count = sum(1 for r in merged_data if r['attr_name'] == attr_name and r['score'] in [4, 5])
                neg_count = sum(1 for r in merged_data if r['attr_name'] == attr_name and r['score'] in [1, 2])

                if review['score'] in [4, 5] and pos_count < 5:
                    merged_data.append(review)
                    review_counts[attr_name]['positive'] += 1
                elif review['score'] in [1, 2] and neg_count < 5:
                    merged_data.append(review)
                    review_counts[attr_name]['negative'] += 1
                    


    return merged_data, review_counts

if __name__ == '__main__':
    recent_data_path = '../Data/Review_Data/Attr_Review/일본_attr_review_recent.json'
    train_data_path = '../Data/Review_Data/Attr_Review/일본_attr_review_train.json'
    
    with open(recent_data_path, 'r', encoding='utf-8') as file:
        recent_data = json.load(file)
    
    with open(train_data_path, 'r', encoding='utf-8') as file:
        train_data = json.load(file)

    merged_data, review_counts = merge_datasets(recent_data, train_data)
    
    print(f"recent_data len = {len(recent_data)}, train_data len = {len(train_data)}, merged_data = {len(merged_data)}")
    print(f"Total number of attrs: {len(review_counts)}")

    for attr, counts in review_counts.items():
        print(f"{attr}: Positive reviews added = {counts['positive']}, Negative reviews added = {counts['negative']}")
