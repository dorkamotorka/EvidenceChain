import requests

base = "http://172.34.1.3:5000"
filename = 'test.png'
file = {'file': open(filename, 'rb'), 'filename': filename}
resp = requests.post(base + "/files", files=file)
print(resp)
