"""
dailytour score
출국자 수의 비중이 매우 적은(혹은 없는) 국가에 대한 ***종합 점수***를 나타냄
(출국자수에 대해서만 제공하는 느낌이 많다 → 출국자수에 대한 점수를 대폭 줄이고
나머지 컨텐츠(숙소, 관광지 등)에 대해서 새로운 점수를 제공하는 시스템)
국가별 컨텐츠의 평균점수, 환율 점수에 대한 비율을 정해야 함
일단 숙소, 관광지, 환율 점수 자체가 1~5점으로 분포 되어 있으니까
1:1:1로 반영하게 코드 작성, 이후에 점수 분포를 보고 스케일링 혹은 비율 변경
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