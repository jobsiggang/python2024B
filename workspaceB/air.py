import requests
# serviceKey='eQaqrVvz7HoT3seuAaJ8rW4eNKU6GW%2BfLhDgLw8%2B6G3jtnJ6HqCSpZOoflkqNLy7E4n9VzxmVBg%2FHjQ3lFYRZQ%3D%3D'
serviceKey='eQaqrVvz7HoT3seuAaJ8rW4eNKU6GW+fLhDgLw8+6G3jtnJ6HqCSpZOoflkqNLy7E4n9VzxmVBg/HjQ3lFYRZQ=='
url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'
params ={'serviceKey' : serviceKey, 'returnType' : 'json', 'numOfRows' : '100', 'pageNo' : '1', 'sidoName' : '울산', 'ver' : '1.0' }

response = requests.get(url, params=params)
air=response.text
print(air)