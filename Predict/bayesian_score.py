import pandas as pd

# 미리 저장된 CSV 파일로부터 데이터를 불러옵니다.
attr_df = pd.read_csv('../Data/Predicted_Data/attr_review_analysis.csv')
accom_df = pd.read_csv('../Data/Predicted_Data/accom_review_analysis.csv')

# 전체 리뷰 개수에서 긍정 리뷰의 평균 비율을 계산합니다.
total_pos_reviews = attr_df['ATTR_REV_POS'].sum() + accom_df['ACCOM_REV_POS'].sum()
total_reviews = total_pos_reviews + attr_df['ATTR_REV_NEG'].sum() + accom_df['ACCOM_REV_NEG'].sum()
P_avg = total_pos_reviews / total_reviews  # 전체 리뷰 중 긍정 리뷰의 평균 비율

# 평균 리뷰 개수를 이용해 가중치 C를 계산합니다.
C = total_reviews / (len(attr_df) + len(accom_df))

# 베이지안 점수 계산 함수
def calculate_bayesian_score(row, review_type):
    # 긍정 리뷰와 부정 리뷰의 총 개수
    n = row[f'{review_type}_REV_POS'] + row[f'{review_type}_REV_NEG']
    # 해당 항목의 긍정 리뷰 비율
    P_item = row[f'{review_type}_REV_POS'] / n if n else 0
    # 베이지안 평균 점수 계산
    P_bayes = (C * P_avg + n * P_item) / (C + n)
    # 5점 척도로 변환하여 반올림
    return round(P_bayes * 5, 1)

# 베이지안 점수 계산을 각 행에 적용
attr_df['score'] = attr_df.apply(calculate_bayesian_score, axis=1, review_type='ATTR')
accom_df['score'] = accom_df.apply(calculate_bayesian_score, axis=1, review_type='ACCOM')

# 계산된 점수를 새로운 CSV 파일로 저장합니다.
attr_df.to_csv('../Data/Predicted_Data/attr_review_analysis_scores.csv', index=False)
accom_df.to_csv('../Data/Predicted_Data/accom_review_analysis_scores.csv', index=False)

# 결과의 처음 몇 줄을 출력하여 확인합니다.
attr_df.head(), accom_df.head()
