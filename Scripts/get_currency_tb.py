import pandas as pd
import requests
from datetime import datetime, timedelta

# 국가 코드와 통화 데이터프레임 생성
cnt_code_with_currency = {
    'CNT_CODE': ['JP', 'CN', 'VN', 'TH', 'PH', 'HK', 'TW', 'MO', 'SG', 'MY', 'ID', 'KH', 'TR', 'IN', 'MN', 'MM', 'ES', 'DE', 'AU', 'GB', 'SI', 'RU', 'US', 'CA', 'MX', 'AU', 'NZ'],
    'CURRENCY': ['JPY', 'CNH', 'VND', 'THB', 'PHP', 'HKD', 'TWD', 'MOP', 'SGD', 'MYR', 'IDR', 'KHR', 'TRY', 'INR', 'MNT', 'MMK', 'EUR', 'EUR', 'AUD', 'GBP', 'EUR', 'RUB', 'USD', 'CAD', 'MXN', 'AUD', 'NZD']
}
cc_df = pd.DataFrame(cnt_code_with_currency)

# 날짜 포매팅 함수
def format_date(date):
    return date.strftime('%Y%m%d')

# API URL 설정
base_url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'
authkey = 'QFenQjzBrzZixROTFHyY5QN2IMkUmZ0e'
data = 'AP01'

# 환율 평균값을 저장할 데이터프레임 초기화
rates_df = pd.DataFrame()

# 날짜 설정: 최근 6개월
end_date = datetime.now() - timedelta(days=1)
start_date = end_date - timedelta(days=180)

# 각 국가별 환율 데이터 수집
while start_date <= end_date:
    if start_date.weekday() < 5:  # 주말 제외
        searchdate = format_date(start_date)
        url = f'{base_url}?authkey={authkey}&searchdate={searchdate}&data={data}'

        try:
            response = requests.get(url).json()
            if response:
                ex_pd = pd.DataFrame(response)
                ex_pd['ttb'] = ex_pd['ttb'].str.replace(',', '').str.extract('(\d+(?:\.\d+)?)').astype(float)

                # 각 국가별 환율 데이터를 cc_df와 병합
                merged_df = cc_df.merge(ex_pd[['cur_unit', 'ttb']], left_on='CURRENCY', right_on='cur_unit', how='inner')
                rates_df = pd.concat([rates_df, merged_df[['CNT_CODE', 'CURRENCY', 'ttb']]])
        except requests.RequestException as e:
            print(f"Request Error: {e}")
        except pd.errors.EmptyDataError as e:
            print(f"Pandas Error: {e}")

    start_date += timedelta(days=1)

# 각 국가별 환율 평균 계산 및 int 형으로 변환
avg_rates_df = rates_df.groupby(['CNT_CODE', 'CURRENCY'])['ttb'].mean().reset_index()
avg_rates_df['EXCHANGE_AVG'] = avg_rates_df['ttb'].apply(lambda x: int(round(x)))

# 불필요한 'ttb' 열 제거
avg_rates_df.drop('ttb', axis=1, inplace=True)

# 결과 저장
csv_output_path = 'country_currency_avg.csv'
avg_rates_df.to_csv(csv_output_path, index=False, encoding='utf-8')
