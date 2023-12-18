import pandas as pd

def get_reg_tb():
    file1_path = '../Data/Predicted_Data/attr_scaled.csv'
    file2_path = '../Data/DB/COUNTRY_TB.csv'
    
    file3_path = '../Data/Predicted_Data/accom_scaled.csv'
    file4_path = '../Data/DB/COUNTRY_TB.csv'

    df1 = pd.read_csv(file1_path, usecols=['CNT_NAME', 'REG_NAME', 'ATTR_NAME'])
    df2 = pd.read_csv(file2_path)
    
    df3 = pd.read_csv(file3_path, usecols=['CNT_NAME', 'REG_NAME', 'ACCOM_NAME'])
    df4 = pd.read_csv(file4_path)

    merged_df1 = pd.merge(df1, df2, on=['CNT_NAME', 'REG_NAME'])
    merged_df2 = pd.merge(df3, df4, on=['CNT_NAME', 'REG_NAME'])

    merged_df1['ATTR_CODE'] = ['AT' + str(1000 + i) for i in range(len(merged_df1))]
    merged_df2['ACCOM_CODE'] = ['AC' + str(1000 + i) for i in range(len(merged_df2))]

    result_df1 = merged_df1[['ATTR_CODE', 'REG_CODE', 'ATTR_NAME']]
    result_df2 = merged_df2[['ACCOM_CODE', 'REG_CODE', 'ACCOM_NAME']]
    
    result_df1.to_csv('../Data/DB/REG_ATTRS_TB.csv', index=False)
    result_df2.to_csv('../Data/DB/REG_ACCOM_TB.csv', index=False)
    
if __name__=="__main__":
    get_reg_tb()
