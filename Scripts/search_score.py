# COUNTRY_INFO_TB.csv 의 SEARCH_VOL, CNT_CODE 사용
# Ooutbound_10Y_Data_en에서 2023행 찾아서 SEARCH_VOL이 0이 아니라면 SERACH_VOL / 2023행, CNT_CODE가 맞는 데이터로 나눔
# 이후에 스케일링    

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def calculate_search_rate():
    outbound_df = pd.read_csv("../Data/Outbound_Data/outbound_10Y_Data_en.csv")
    country_info_df = pd.read_csv("../Data/DB/COUNTRY_INFO_TB.csv")

    outbound_2023_df = outbound_df[outbound_df['year'] == 2023].drop(columns=['year'])
    pivot_outbound_2023_df = outbound_2023_df.melt(var_name='CNT_CODE', value_name='OUTBOUND_COUNT')

    merged_df = country_info_df.merge(pivot_outbound_2023_df, on='CNT_CODE', how='left')

    merged_df['SEARCH_RATE'] = merged_df.apply(
        lambda row: row['SEARCH_VOL'] / row['OUTBOUND_COUNT'] if row['OUTBOUND_COUNT'] > 0 else None, 
        axis=1
    )

    # 0 값을 제외하고 스케일링 및 점수 계산
    scaler = MinMaxScaler()
    filtered_df = merged_df[merged_df['SEARCH_VOL'] > 0]
    filtered_df['SEARCH_RATE_SCALED'] = scaler.fit_transform(filtered_df[['SEARCH_RATE']].dropna())

    # SEARCH_RATE가 높을수록 점수가 낮아짐 (1에 가까워짐)
    filtered_df['SEARCH_SCORE'] = filtered_df['SEARCH_RATE_SCALED'].apply(lambda x: round((1 - x) * 4 + 1, 2))

    # 원본 데이터프레임에 점수 업데이트
    merged_df['SEARCH_SCORE'] = 0
    merged_df.loc[filtered_df.index, 'SEARCH_SCORE'] = filtered_df['SEARCH_SCORE']

    return merged_df[['CNT_CODE', 'CURRENCY', 'EX_RATE', 'EX_AVG', 'SEARCH_SCORE']]

if __name__ == "__main__":
    result = calculate_search_rate()
    print(result)
    result.to_csv('../Data/COUNTRY_INFO_TB_SEARCH_SCORE.csv', index=False, encoding='utf-8')
    