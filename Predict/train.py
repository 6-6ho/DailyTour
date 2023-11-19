import glob
import json
from konlpy.tag import Okt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from joblib import dump, load

okt = Okt()

def tokenize_korean_text(text):
    return [
        word for word, tag in okt.pos(text, stem=True)
        if tag in ['Noun', 'Verb', 'Adjective']
    ]

def train():
    file_pattern = '../data/Review_Data/Attr_Review/*_attr_review_train.json'

    review_files = glob.glob(file_pattern)

    combined_comments = []
    combined_labels = []

    for file_path in review_files:
        with open(file_path, 'r', encoding='utf-8') as file:
            reviews_data = json.load(file)
            for review in reviews_data:
                combined_comments.append(' '.join(tokenize_korean_text(review['title'] + " " + review['content'])))
                combined_labels.append(1 if int(review['score']) > 3 else 0)  # 1 for positive, 0 for negative

    vectorizer = CountVectorizer(tokenizer=lambda x: x.split(), lowercase=False)
    combined_comment_vectors = vectorizer.fit_transform(combined_comments)

    X_train, X_test, y_train, y_test = train_test_split(combined_comment_vectors, combined_labels, test_size=0.2, random_state=42)

    sgd_model = SGDClassifier(loss='log_loss', max_iter=1000)

    sgd_model.fit(X_train, y_train)

    for file_path in review_files:
        with open(file_path, 'r', encoding='utf-8') as file:
            reviews_data = json.load(file)
            country_comments = [' '.join(tokenize_korean_text(review['title'] + " " + review['content'])) for review in reviews_data]
            country_labels = [1 if int(review['score']) > 3 else 0 for review in reviews_data]

            country_comment_vectors = vectorizer.transform(country_comments)

            country_pred = sgd_model.predict(country_comment_vectors)

            country_accuracy = accuracy_score(country_labels, country_pred)
            print(country_accuracy)

    dump(sgd_model, 'sgd_model.joblib')
    dump(vectorizer, 'vectorizer.joblib')
    
if __name__=='__main__':
    train()
