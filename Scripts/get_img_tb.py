import pandas as pd
import os
import glob

def merge_csv(files):
    df_list = []
    for file in files:
        # 파일이 존재하고 비어 있지 않은지 확인
        if os.path.exists(file) and os.path.getsize(file) > 0:
            df = pd.read_csv(file)
            df_list.append(df)

    # 데이터프레임 리스트가 비어 있지 않은 경우에만 concat 실행
    if df_list:
        return pd.concat(df_list, ignore_index=True)
    else:
        # 데이터프레임 리스트가 비어 있는 경우 빈 데이터프레임 반환
        return pd.DataFrame()


def get_img_tb():
    file_path1 = '../Data/DB/REG_ACCOM_TB.csv'
    file_dir1 = '../Data/picture-data/accom'
    
    file_path2 = '../Data/DB/REG_ATTRS_TB.csv'
    file_dir2 = '../Data/picture-data/attr'
    
    file_pattern1 = os.path.join(file_dir1, '*_img_path.csv')
    accom_files = glob.glob(file_pattern1)
    
    file_pattern2 = os.path.join(file_dir2, '*_img_path_reviews.csv')
    attr_files = glob.glob(file_pattern2)
    
    df1 = pd.read_csv(file_path1)
    df2 = pd.read_csv(file_path2)

    # 각 파일 패턴에 해당하는 파일들을 읽어서 하나의 데이터프레임으로 합치기
    accom_df = merge_csv(accom_files)
    attr_df = merge_csv(attr_files)

    # 데이터프레임 병합
    merged_df1 = pd.merge(df1, accom_df, on=['ACCOM_NAME'])
    merged_df2 = pd.merge(df2, attr_df, on=['ATTR_NAME'])
    
    result_df1 = merged_df1[['ACCOM_CODE', 'IMG_PATH']]
    result_df2 = merged_df2[['ATTR_CODE', 'IMG_PATH']]
    
    # 결과 저장
    result_df1.to_csv('../Data/DB/ACCOM_IMG_TB.csv', index=False)
    result_df2.to_csv('../Data/DB/ATTR_IMG_TB.csv', index=False)
    
if __name__ == "__main__":
    get_img_tb()
