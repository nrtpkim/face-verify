import requests
import time


url = "http://192.168.1.102:1234/verify/1-1"
for i in range(10):
  t0 = time.time()
  payload={}
  files=[
    ('img1',('../assets/photo/BLACKPINK-Lisa with 2 face.jpg',open('../assets/photo/BLACKPINK-Lisa with 2 face.jpg','rb'),'image/jpeg')),
    ('img2',('../assets/photo/Blackpink_Lisa_190621_2.png',open('../assets/photo/Blackpink_Lisa_190621_2.png','rb'),'image/jpeg'))
  ]
  
  headers = {}


  response = requests.request("POST", url, headers=headers, data=payload, files=files)
  t1 = time.time()
  print("detected : {0} ms".format((t1-t0)*1000))
  
  print(response.text)