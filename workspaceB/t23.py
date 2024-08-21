import requests
url=f'https://ncic.re.kr/mobile.kri.org4.inventoryDocument.do?pOrgNo=10069974'
re=requests.get(url)
# data=re.json()
print(re.text)