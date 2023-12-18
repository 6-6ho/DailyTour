import pandas as pd

def get_reg_tb():
    file1_path = '../Data/Predicted_Data/attr_scaled.csv'
    file2_path = '../Data/DB/REG_ATTRS_TB.csv'
    
    file3_path = '../Data/Predicted_Data/accom_scaled.csv'
    file4_path = '../Data/DB/REG_ACCOM_TB.csv'

    # 실제 CSV 파일 로드
    df1 = pd.read_csv(file1_path)
    df2 = pd.read_csv(file2_path)
    
    df3 = pd.read_csv(file3_path)
    df4 = pd.read_csv(file4_path)

    # 'REG_NAME'을 기준으로 두 데이터 프레임을 병합합니다.
    merged_df1 = pd.merge(df1, df2, on=['ATTR_NAME'])
    merged_df2 = pd.merge(df3, df4, on=['ACCOM_NAME'])

    # 최종적으로 필요한 열만 선택하여 새로운 데이터 프레임을 만듭니다.
    result_df1 = merged_df1[['ATTR_CODE', 'SCORE', 'ATTR_REV_POS', 'ATTR_REV_NEG']]
    result_df2 = merged_df2[['ACCOM_CODE', 'SCORE', 'ACCOM_REV_POS', 'ACCOM_REV_NEG']]
    
    result_df1.to_csv('../Data/DB/ATTR_INFO_TB.csv', index=False)
    result_df2.to_csv('../Data/DB/ACCOM_INFO_TB.csv', index=False)
    
if __name__=="__main__":
    get_reg_tb()
