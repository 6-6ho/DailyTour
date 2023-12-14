import pandas as pd

def get_reg_tb():
    file1_path = '../Data/Predicted_Data/attr_scaled.csv'
    file2_path = '../Data/DB/COUNTRY_TB.csv'
    
    file3_path = '../Data/Predicted_Data/accom_scaled.csv'
    file4_path = '../Data/DB/COUNTRY_TB.csv'

    # 실제 CSV 파일 로드
    df1 = pd.read_csv(file1_path, usecols=['CNT_NAME', 'REG_NAME', 'ATTR_NAME'])
    df2 = pd.read_csv(file2_path)
    
    df3 = pd.read_csv(file3_path, usecols=['CNT_NAME', 'REG_NAME', 'ACCOM_NAME'])
    df4 = pd.read_csv(file4_path)

    # 'REG_NAME'을 기준으로 두 데이터 프레임을 병합합니다.
    merged_df1 = pd.merge(df1, df2, on=['CNT_NAME', 'REG_NAME'])
    merged_df2 = pd.merge(df3, df4, on=['CNT_NAME', 'REG_NAME'])

    # 'ATTR_CODE' 열을 생성합니다. 여기서는 예시로 'CNT_CODE'와 'ATTR_NAME'을 결합합니다.
    merged_df1['ATTR_CODE'] = ['AT' + str(1000 + i) for i in range(len(merged_df1))]
    merged_df2['ACCOM_CODE'] = ['AC' + str(1000 + i) for i in range(len(merged_df2))]

    # 최종적으로 필요한 열만 선택하여 새로운 데이터 프레임을 만듭니다.
    result_df1 = merged_df1[['ATTR_CODE', 'REG_CODE', 'ATTR_NAME']]
    result_df2 = merged_df2[['ACCOM_CODE', 'REG_CODE', 'ACCOM_NAME']]
    
    result_df1.to_csv('../Data/DB/REG_ATTRS_TB.csv', index=False)
    result_df2.to_csv('../Data/DB/REG_ACCOM_TB.csv', index=False)
    
if __name__=="__main__":
    get_reg_tb()
