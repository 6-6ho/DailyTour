"""
dailytour score
출국자 수의 비중이 매우 적은(혹은 없는) 국가에 대한 ***종합 점수***를 나타냄
(출국자수에 대해서만 제공하는 느낌이 많다 → 출국자수에 대한 점수를 대폭 줄이고
나머지 컨텐츠(숙소, 관광지 등)에 대해서 새로운 점수를 제공하는 시스템)
국가별 컨텐츠의 평균점수, 환율 점수에 대한 비율을 정해야 함
일단 숙소, 관광지, 환율 점수 자체가 1~5점으로 분포 되어 있으니까
1:1:1로 반영하게 코드 작성 이후에 점수 분포를 보고 스케일링 혹은 비율 변경
 -> 환율 점수는 더 인위적인 데이터에 가까우므로 2:2:1정도로
 -> EX_SCORE때문에 더 조절해가면서 봤는데 8:8:1 해야 좀 걷히는 느낌
 -> 그럼 관광지와 호텔에 대해서 점수가 더 많은 이유를 어필하는게 좋을 듯 ( EX_SCORE때문에 조절했다 라기엔 EX_SCORE에 대한 단점을 부각)
 -> 기사 인용하면서 실제로 해외에서 중요하게 생각하는것 1. 맛집 2. 숙소 3. 관광지인데 맛집은 내용에 없으니 제외하고 숙소 관광지에 대해서 사용한다?
 좀 구리긴 한데 이렇게 버무리면 넘어갈 사람이 더 많을 것 같음
검색량을 반영하기엔 검색량이 0인 국가가 많기 때문에 많이 떨어질 것 같음
"""

"""
Predicted_Data에서 accom_scaled, attr_scaled가 점수상 최종 데이터
(accom_scaled.csv와 attr_scaled.csv에서 CNT_NAME을 기준으로 SCORE의 평균을 냄(round(,2)) -> ATTR_SCORE, ACCOM_SCORE로 각각 저장 한 후
COUNTRY_TB와 병합(기준 CNT_NAME)해서 CNT_CODE, ATTR_SCORE, ACCOM_SCORE를 남기고
COUNTRY_INFO_TB에 다시 병합

../Data/Predicted_Data/accom_scaled.csv
../Data/Predicted_Data/attr_scaled.csv

../Data/DB/COUNTRY_TB.csv
../Data/DB/COUNTRY_INFO_TB.csv
"""


import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def merge_scores_with_country_info():
    # 데이터 불러오기
    accom_df = pd.read_csv("../Data/Predicted_Data/accom_scaled.csv", index_col=False)
    attr_df = pd.read_csv("../Data/Predicted_Data/attr_scaled.csv", index_col=False)
    country_tb = pd.read_csv("../Data/DB/COUNTRY_TB.csv", index_col=False)
    country_info_tb = pd.read_csv("../Data/COUNTRY_INFO_TB_EX_SC.csv", index_col=False)

    # accom_scaled.csv와 attr_scaled.csv에서 SCORE 평균 계산
    accom_score = accom_df.groupby('CNT_NAME')['SCORE'].mean().round(2).reset_index().rename(columns={'SCORE': 'ACCOM_SCORE'})
    attr_score = attr_df.groupby('CNT_NAME')['SCORE'].mean().round(2).reset_index().rename(columns={'SCORE': 'ATTR_SCORE'})

    # COUNTRY_TB와 병합
    merged_country_tb = country_tb.merge(accom_score, on='CNT_NAME', how='left').merge(attr_score, on='CNT_NAME', how='left')

    # 필요한 컬럼만 선택 및 CNT_CODE를 기준으로 중복 제거
    merged_country_tb = merged_country_tb[['CNT_CODE', 'ACCOM_SCORE', 'ATTR_SCORE']].drop_duplicates(subset=['CNT_CODE'])

    # COUNTRY_INFO_TB와 병합
    final_merged_df = country_info_tb.merge(merged_country_tb, on='CNT_CODE', how='left')
    
    final_merged_df['PRELIMINARY_TOTAL_SCORE'] = (final_merged_df['EX_SCORE'] * 1 + 
                                       final_merged_df['ACCOM_SCORE'] * 8 + 
                                       final_merged_df['ATTR_SCORE'] * 8)
    
    scaler = MinMaxScaler(feature_range=(3, 10))

    # Check for any infinite values and replace them
    final_merged_df.replace([np.inf, -np.inf], np.nan, inplace=True)
    final_merged_df.dropna(subset=['PRELIMINARY_TOTAL_SCORE'], inplace=True)

    final_merged_df['DT_SCORE'] = scaler.fit_transform(final_merged_df[['PRELIMINARY_TOTAL_SCORE']])

    # Round the normalized score to two decimal places
    final_merged_df['DT_SCORE'] = final_merged_df['DT_SCORE'].round(1)

    return final_merged_df.drop(columns=['PRELIMINARY_TOTAL_SCORE', 'ACCOM_SCORE', 'ATTR_SCORE'])

if __name__=='__main__':    
    final_result = merge_scores_with_country_info()
    print(final_result)
    final_result.to_csv("../Data/DB/COUNTRY_INFO_TB.csv", index=False)

