import requests
from PIL import Image
from io import BytesIO
payload = {
    'key1': 'value1',
    'key2': 'value2'
}
req = requests.get('http://httpbin.org/get', params = payload)
# 地址
print(req.url)
# 编码方式
print(req.encoding)
# 访问请求体
print(req.content)

i = Image.open(BytesIO(req.content))
