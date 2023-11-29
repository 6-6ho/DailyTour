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

# 결과 데이터프레임 초기화
result_df = pd.DataFrame()

# 날짜 설정
end_date = datetime.now() - timedelta(days=1)  # 어제 날짜
valid_days_count = 0

# 10개의 유효한 데이터를 수집할 때까지 반복
while valid_days_count < 10:
    if end_date.weekday() < 5:  # 주말 제외
        searchdate = format_date(end_date)
        url = f'{base_url}?authkey={authkey}&searchdate={searchdate}&data={data}'

        try:
            response = requests.get(url).json()
            if response:
                ex_pd = pd.DataFrame(response)
                ex_pd['ttb'] = ex_pd['ttb'].str.replace(',', '', regex=True).str.extract('(\d+\.\d+)').astype(float)
                ex_pd['DATE'] = searchdate

                merged_df = cc_df.merge(ex_pd[['cur_unit', 'ttb', 'DATE']], left_on='CURRENCY', right_on='cur_unit', how='inner')
                result_df = pd.concat([result_df, merged_df[['DATE', 'CNT_CODE', 'CURRENCY', 'ttb']]], ignore_index=True)

                valid_days_count += 1
        except requests.RequestException as e:
            print(f"Request Error: {e}")
        except pd.errors.EmptyDataError as e:
            print(f"Pandas Error: {e}")

    end_date -= timedelta(days=1)

# 'ttb' 열을 'EXCHANGE_RATE'로 이름 변경
result_df = result_df.rename(columns={'ttb': 'EXCHANGE_RATE'})

# 결과 저장
csv_output_path = 'country_currency.csv'
result_df.to_csv(csv_output_path, index=False, encoding='utf-8')
