"""
all_unique_region_data.csv는 서브
main은 attr_review_analysis_scores2.csv
ATTR_CODE하고 REGION_CODE 컬럼을 추가 함
all_unique_region_data.csv를 가져 옴 거기서 Region Name, Region Code를 가져옴
REGION_NAME에 대해서 해당하는 REGION_CODE 컬럼을 추가 함
그리고 처음부터 끝까지 REG_CODE는 AT1000부터 1씩 증가시키면서 저장
"""
import pandas as pd

def create_attr_data():
    # 파일 경로 설정
    main_file_path = '../Data/Predicted_Data/attr_review_analysis_scores2.csv'
    region_file_path = '../Data/Region_Data/all_unique_region_data.csv'
    output_file_path = 'REG_ATTRS_TB.csv'

    # main 파일을 읽어옴
    main_df = pd.read_csv(main_file_path, encoding='cp1252')

    # 새로운 컬럼 추가 (ATTR_CODE, REGION_CODE)
    main_df['ATTR_CODE'] = [f'AT{i+1000}' for i in range(len(main_df))]
    main_df['REGION_CODE'] = ''

    # region 파일을 읽어옴
    region_df = pd.read_csv(region_file_path, encoding='cp1252')

    # REGION_NAME에 대해서 해당하는 REGION_CODE 컬럼을 추가
    main_df = main_df.merge(region_df[['Region Name', 'Region Code']], left_on='REG_NAME', right_on='Region Name', how='left')

    # 필요한 컬럼만 선택하고 컬럼명 변경
    main_df = main_df[['ATTR_CODE', 'REGION_CODE', 'ATTR_NAME']]

    # REGION_CODE가 없는 경우 "Not_Match"로 설정
    main_df['REGION_CODE'].fillna('Not_Match', inplace=True)

    # REG_CODE 업데이트 (AT1000부터 1씩 증가)
    main_df['REG_CODE'] = [f'AT{i}' for i in range(1000, 1000 + len(main_df))]

    # 결과를 CSV 파일로 저장
    main_df.to_csv(output_file_path, index=False, encoding='cp1252')

    print(f'{output_file_path} 파일이 생성되었습니다.')

# 함수 호출
create_attr_data()
