import pandas as pd

# 데이터 불러오기
df1 = pd.read_csv('../Data/Predicted_Data/accom_merged_score.csv')
df2 = pd.read_csv('../Data/Predicted_Data/attr_merged_score.csv')

# 각 데이터프레임에 대한 스케일링 함수
def scale_scores(df):
    min_score = df['SCORE'].min()
    max_score = df['SCORE'].max()
    df['SCORE'] = round(1 + ((df['SCORE'] - min_score) * (5 - 1)) / (max_score - min_score),2)
    return df

# 스케일링 적용
df1_scaled = scale_scores(df1)
df2_scaled = scale_scores(df2)

# 스케일링된 데이터 저장
df1_scaled.to_csv('../Data/Predicted_Data/accom_scaled.csv', index=False)
df2_scaled.to_csv('../Data/Predicted_Data/attr_scaled.csv', index=False)
