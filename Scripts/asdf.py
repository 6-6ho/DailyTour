import json

def merge_datasets(recent_data, train_data):
    """
    Merges the train dataset into the recent dataset based on the hotel name.
    For each hotel, adds up to 5 positive and 5 negative reviews from the train dataset
    that are not already in the recent dataset.
    """
    # Convert recent data into a dictionary for easier access
    recent_dict = {}
    for review in recent_data:
        hotel_name = review['hotel_name']
        if hotel_name not in recent_dict:
            recent_dict[hotel_name] = []
        recent_dict[hotel_name].append(review)

    # Process train data
    for review in train_data:
        hotel_name = review['hotel_name']
        if hotel_name in recent_dict:
            # Count positive and negative reviews for the hotel in recent data
            pos_count = sum(1 for r in recent_dict[hotel_name] if r['score'] in [4, 5])
            neg_count = sum(1 for r in recent_dict[hotel_name] if r['score'] in [1, 2])

            # Check for duplicates and add non-duplicates to the recent data
            if review not in recent_dict[hotel_name]:
                if review['score'] in [4, 5] and pos_count < 5:
                    recent_dict[hotel_name].append(review)
                elif review['score'] in [1, 2] and neg_count < 5:
                    recent_dict[hotel_name].append(review)

    # Convert the dictionary back to a list
    merged_data = []
    for reviews in recent_dict.values():
        merged_data.extend(reviews)

    return merged_data

if __name__ == '__main__':
    recent_data_path = '../Data/Review_Data/Accom_Review/뉴질랜드_accom_review_recent.json'
    train_data_path = '../Data/Review_Data/Accom_Review/뉴질랜드_accom_review_train.json'
    
    # Load data from the files
    with open(recent_data_path, 'r', encoding='utf-8') as file:
        recent_data = json.load(file)
    
    with open(train_data_path, 'r', encoding='utf-8') as file:
        train_data = json.load(file)

    # Merge datasets
    merged_data = merge_datasets(recent_data, train_data)
    
    print(f"recent_data len = {len(recent_data)}, train_data len = {len(train_data)}, merged_data = {len(merged_data)}")