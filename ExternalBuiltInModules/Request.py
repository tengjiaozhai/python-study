# 请求url
import requests

r = requests.get('https://liaoxuefeng.com/books/python/third-party-modules/requests/index.html')
print(r.status_code)
params = {'pageNum': 1, 'pageSize': 10}
r = requests.post('http://10.160.1.196:7666/complaint/ComplaintProcess/pageList',json=params)
print(r.json())
