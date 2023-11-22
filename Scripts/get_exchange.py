import requests
import pandas as pd

authkey = 'QFenQjzBrzZixROTFHyY5QN2IMkUmZ0e'
searchdate = '20231121'
data = 'AP01'

url = f' https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={authkey}&searchdate={searchdate}&data={data}'

response = requests.get(url).json()
ex_pd = pd.DataFrame(response)

print(ex_pd)