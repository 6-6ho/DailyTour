"""
COUNTRY_INFO_TB.CSV파일에서 EX_AVG / EX_RATE한 값을 RATE_DIV로 저장
"""
import pandas as pd

file_path = '../Data/COUNTRY_INFO_TB_SEARCH_SCORE.csv'

def exchange_score():


    country_info = pd.read_csv(file_path)
    country_info['RATE_DIV'] = country_info['EX_RATE'] / country_info['EX_AVG']

    # RATE_DIV가 낮을수록 높은 점수 (1~5점)
    min_div = country_info['RATE_DIV'].min()
    max_div = country_info['RATE_DIV'].max()

    def calculate_rate_div_score(div, min_div, max_div, scale_max):
        normalized_div = (max_div - div) / (max_div - min_div)
        score = 1 + (normalized_div * (scale_max - 1))
        return round(score, 2)

    # 모든 국가에 대한 초기 점수 계산
    country_info['EX_SCORE'] = country_info['RATE_DIV'].apply(lambda x: calculate_rate_div_score(x, min_div, max_div, 5))

    # TR을 제외한 나머지 국가들에 대해 다시 1~4.5점으로 스케일링
    country_info_without_TR = country_info[country_info['CNT_CODE'] != 'TR']
    min_div_without_TR = country_info_without_TR['RATE_DIV'].min()
    max_div_without_TR = country_info_without_TR['RATE_DIV'].max()

    for idx, row in country_info_without_TR.iterrows():
        country_info.at[idx, 'EX_SCORE'] = calculate_rate_div_score(row['RATE_DIV'], min_div_without_TR, max_div_without_TR, 4.5)
        
    # TR, MN을 제외한 나머지 국가들에 대해 다시 4.0점으로 스케일링
    country_info_without_TR_MN = country_info[(country_info['CNT_CODE'] != 'TR') & (country_info['CNT_CODE'] != 'MN')]
    min_div_without_TR_MN = country_info_without_TR_MN['RATE_DIV'].min()
    max_div_without_TR_MN = country_info_without_TR_MN['RATE_DIV'].max()

    for idx, row in country_info_without_TR_MN.iterrows():
        country_info.at[idx, 'EX_SCORE'] = calculate_rate_div_score(row['RATE_DIV'], min_div_without_TR_MN, max_div_without_TR_MN, 4.0)
    

    result_df = country_info[['CNT_CODE', 'CURRENCY', 'EX_RATE', 'EX_AVG', 'SEARCH_SCORE', 'EX_SCORE']]
    print(result_df)
    return result_df

if __name__ == "__main__":
    result = exchange_score()
    result.to_csv('../Data/COUNTRY_INFO_TB_EX_SC.csv', index=False)