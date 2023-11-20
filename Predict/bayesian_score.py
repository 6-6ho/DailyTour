import pandas as pd

attr_df = pd.read_csv('../Data/Predicted_Data/attr_review_analysis.csv')
accom_df = pd.read_csv('../Data/Predicted_Data/accom_review_analysis.csv')

# 전체 리뷰 개수에서 긍정 리뷰의 평균 비율을 계산합니다.
total_pos_reviews = attr_df['ATTR_REV_POS'].sum() + accom_df['ACCOM_REV_POS'].sum()
total_reviews = total_pos_reviews + attr_df['ATTR_REV_NEG'].sum() + accom_df['ACCOM_REV_NEG'].sum()
P_avg = total_pos_reviews / total_reviews

# 평균 리뷰 개수를 사용하는 가중치를 계산합니다.
C = total_reviews / (len(attr_df) + len(accom_df))

# 각 관광지와 숙박시설에 대해 베이지안 평균 점수를 계산하고 5점 척도로 변환합니다.
def calculate_bayesian_score(row, review_type):
    n = row[f'{review_type}_REV_POS'] + row[f'{review_type}_REV_NEG']
    P_item = row[f'{review_type}_REV_POS'] / n if n else 0
    P_bayes = (C * P_avg + n * P_item) / (C + n)
    return round(P_bayes * 5, 1)

attr_df['score'] = attr_df.apply(calculate_bayesian_score, axis=1, review_type='ATTR')
accom_df['score'] = accom_df.apply(calculate_bayesian_score, axis=1, review_type='ACCOM')

# 결과를 새로운 CSV 파일로 저장합니다.
attr_df.to_csv('../Data/Predicted_Data/attr_review_analysis_scores.csv', index=False)
accom_df.to_csv('../Data/Predicted_Data/accom_review_analysis_scores.csv', index=False)

attr_df.head(), accom_df.head()  # 결과의 일부를 보여줍니다.
