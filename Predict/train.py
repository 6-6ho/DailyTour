import glob
import json
from konlpy.tag import Okt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import SGDClassifier
from joblib import dump

# 한국어 형태소 분석기 Okt 객체 생성
okt = Okt()

def tokenize_korean_text(text):
    # 주어진 텍스트를 형태소 분석하여 명사, 동사, 형용사만 추출
    return [
        word for word, tag in okt.pos(text, stem=True)
        if tag in ['Noun', 'Verb', 'Adjective']
    ]

def remove_locations(text, locations):
    # 주어진 텍스트에서 위치 정보를 제거
    for location in locations:
        text = text.replace(location, '')
    return text

def load_data_and_labels(file_path):
    # 파일을 열어 리뷰 데이터를 로드하고, 텍스트와 라벨을 추출하여 반환
    with open(file_path, 'r', encoding='utf-8') as file:
        reviews_data = json.load(file)
        comments = [' '.join(tokenize_korean_text(remove_locations(review['title'] + " " + review['content'], [review.get('region', ''), review.get('country', '')]))) for review in reviews_data]
        labels = [1 if int(review['SCORE']) > 3 else 0 for review in reviews_data]
    return comments, labels

def train_and_evaluate(review_type):
    # 학습할 리뷰 파일의 패턴을 지정
    file_pattern = f'../data/Review_Data/{review_type.capitalize()}_Review/*_{review_type}_review_train.json'
    review_files = glob.glob(file_pattern)
    
    all_comments = []
    all_labels = []

    # 모든 리뷰 파일을 순회하며 데이터를 로드
    for file_path in review_files:
        print(f'Processing file: {file_path}')
        comments, labels = load_data_and_labels(file_path)
        all_comments.extend(comments)
        all_labels.extend(labels)

    # TF 방식으로 텍스트 데이터를 벡터화
    vectorizer = CountVectorizer(tokenizer=tokenize_korean_text, lowercase=False)
    comment_vectors = vectorizer.fit_transform(all_comments)

    # 데이터를 학습 세트와 테스트 세트로 분리
    X_train, X_test, y_train, y_test = train_test_split(comment_vectors, all_labels, test_size=0.2, random_state=42)

    # 그리드 서치를 사용하여 최적의 하이퍼파라미터를 찾기
    param_grid = {
        'alpha': [0.0001, 0.001, 0.01, 0.1],
        'penalty': ['l2', 'l1', 'elasticnet'],
        'max_iter': [1000, 2000, 3000]
    }

    # SGD 분류기를 사용하고, 로지스틱 회귀 손실 함수를 사용하여 그리드 서치 수행
    grid_search = GridSearchCV(SGDClassifier(loss='log_loss'), param_grid, cv=5, scoring='accuracy')
    grid_search.fit(X_train, y_train)

    # 최적의 파라미터와 모델을 추출
    best_params = grid_search.best_params_
    best_model = grid_search.best_estimator_

    # 테스트 데이터에 대한 예측을 수행하고 정확도를 측정
    test_predictions = best_model.predict(X_test)
    test_accuracy = accuracy_score(y_test, test_predictions)
    print(f'Best parameters: {best_params}')
    print(f'Test Accuracy with best parameters: {test_accuracy:.2f}')

    # 최적의 모델과 벡터라이저를 파일로 저장
    dump(best_model, f'sgd_model_{review_type}.joblib')
    dump(vectorizer, f'vectorizer_{review_type}.joblib')


if __name__ == '__main__':
    print("ATTR REVIEW")
    train_and_evaluate('attr')
    print("ACCOM REVIEW")
    train_and_evaluate('accom')
