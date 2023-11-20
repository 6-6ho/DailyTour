import glob
import json
from konlpy.tag import Okt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import SGDClassifier
from joblib import dump

okt = Okt()

def tokenize_korean_text(text):
    return [
        word for word, tag in okt.pos(text, stem=True)
        if tag in ['Noun', 'Verb', 'Adjective']
    ]

def remove_locations(text, locations):
    for location in locations:
        text = text.replace(location, '')
    return text

def load_data_and_labels(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reviews_data = json.load(file)
        comments = [' '.join(tokenize_korean_text(remove_locations(review['title'] + " " + review['content'], [review.get('region', ''), review.get('country', '')]))) for review in reviews_data]
        labels = [1 if int(review['score']) > 3 else 0 for review in reviews_data]
    return comments, labels

def train_and_evaluate(review_type):
    file_pattern = f'../data/Review_Data/{review_type.capitalize()}_Review/*_{review_type}_review_train.json'
    review_files = glob.glob(file_pattern)
    
    all_comments = []
    all_labels = []

    for file_path in review_files:
        print(f'Processing file: {file_path}')
        comments, labels = load_data_and_labels(file_path)
        all_comments.extend(comments)
        all_labels.extend(labels)

    # vectorize
    vectorizer = CountVectorizer(tokenizer=tokenize_korean_text, lowercase=False)
    comment_vectors = vectorizer.fit_transform(all_comments)

    X_train, X_test, y_train, y_test = train_test_split(comment_vectors, all_labels, test_size=0.2, random_state=42)

    # hyper parameter grid
    param_grid = {
        'alpha': [0.0001, 0.001, 0.01, 0.1],
        'penalty': ['l2', 'l1', 'elasticnet'],
        'max_iter': [1000, 2000, 3000]
    }

    grid_search = GridSearchCV(SGDClassifier(loss='log_loss'), param_grid, cv=5, scoring='accuracy')
    grid_search.fit(X_train, y_train)

    best_params = grid_search.best_params_
    best_model = grid_search.best_estimator_

    test_predictions = best_model.predict(X_test)
    test_accuracy = accuracy_score(y_test, test_predictions)
    print(f'Best parameters: {best_params}')
    print(f'Test Accuracy with best parameters: {test_accuracy:.2f}')

    dump(best_model, f'sgd_model_{review_type}.joblib')
    dump(vectorizer, f'vectorizer_{review_type}.joblib')

if __name__ == '__main__':
    print("ATTR REVIEW")
    train_and_evaluate('attr')
    print("ACCOM REVIEW")
    train_and_evaluate('accom')
