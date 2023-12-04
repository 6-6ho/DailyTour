import pandas as pd

def get():
    file1_path = '../Data/Predicted_Data/attr_review_analysis_scores2.csv'
    file2_path = '../Data/Region_Data/all_unique_region_data.csv'

    # 실제 CSV 파일 로드
    df1 = pd.read_csv(file1_path, usecols=['CNT_NAME', 'REG_NAME', 'ATTR_NAME'])
    df2 = pd.read_csv(file2_path)

    # 'REG_NAME'을 기준으로 두 데이터 프레임을 병합합니다.
    merged_df = pd.merge(df1, df2, on=['CNT_NAME', 'REG_NAME'])

    # 'ATTR_CODE' 열을 생성합니다. 여기서는 예시로 'CNT_CODE'와 'ATTR_NAME'을 결합합니다.
    merged_df['ATTR_CODE'] = ['AT' + str(1000 + i) for i in range(len(merged_df))]

    # 최종적으로 필요한 열만 선택하여 새로운 데이터 프레임을 만듭니다.
    result_df = merged_df[['ATTR_CODE', 'REG_CODE', 'ATTR_NAME']]

    # 결과를 출력합니다.
    print(result_df)
    
    result_df.to_csv('../Data/DB/REG_ATTRS_TB.csv', index=False)
    
if __name__=="__main__":
    get()
