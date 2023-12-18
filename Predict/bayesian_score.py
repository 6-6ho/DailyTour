import pandas as pd

# 미리 저장된 CSV 파일로부터 데이터를 불러옵니다.
attr_df = pd.read_csv('../Data/Predicted_Data/attr_review_analysis.csv')
accom_df = pd.read_csv('../Data/Predicted_Data/accom_review_analysis.csv')  

# 전체 리뷰 개수에서 긍정 리뷰의 평균 비율을 계산합니다.
attr_pos_reviews = attr_df['ATTR_REV_POS'].sum()
accom_pos_reviews = accom_df['ACCOM_REV_POS'].sum()

attr_total_reviews = attr_pos_reviews + attr_df['ATTR_REV_NEG'].sum()
accom_total_reviews = accom_pos_reviews + accom_df['ACCOM_REV_POS'].sum()
attr_P_avg = attr_pos_reviews / attr_total_reviews  # 전체 리뷰 중 긍정 리뷰의 평균 비율
accom_P_avg = accom_pos_reviews / accom_total_reviews


# 평균 리뷰 개수를 이용해 가중치 C를 계산합니다.
attr_C = attr_total_reviews / len(attr_df)
accom_C = accom_total_reviews / len(accom_df)


# 베이지안 점수 계산 함수
def calculate_bayesian_score(row, review_type):
    if review_type == 'ATTR':
        C = attr_C
        P_avg = attr_P_avg
    elif review_type == 'ACCOM':
        C = accom_C
        P_avg = accom_P_avg

    n = row[f'{review_type}_REV_POS'] + row[f'{review_type}_REV_NEG']
    P_item = row[f'{review_type}_REV_POS'] / n if n else 0
    P_bayes = (C * P_avg + n * P_item) / (C + n)
    return round(P_bayes * 5, 2)

# 베이지안 점수 계산을 각 행에 적용
attr_df['SCORE'] = attr_df.apply(calculate_bayesian_score, axis=1, review_type='ATTR')
accom_df['SCORE'] = accom_df.apply(calculate_bayesian_score, axis=1, review_type='ACCOM')

# 계산된 점수를 새로운 CSV 파일로 저장합니다.
attr_df.to_csv('../Data/Predicted_Data/attr_review_analysis_scores.csv', index=False)
accom_df.to_csv('../Data/Predicted_Data/accom_review_analysis_scores.csv', index=False)