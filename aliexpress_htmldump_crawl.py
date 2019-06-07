import pandas as pd
import os, sys
from lxml import html
import re

dir = os.listdir(sys.argv[1])
df_excel = pd.DataFrame()
header = []
url = []
for file in dir:
	try:
		print(file)
		df = open(sys.argv[1]+'/'+file, encoding='utf-8')

		data = df.read()
		data = " ".join(data.split())
		block = re.search(r'"Inicio">(.*?)</h1>', data)

		meta_1 = re.findall(r'title="(.*?)"', block.group(0))
		meta_2 = re.findall(r'</span> <span>(.*?)<', block.group(0))

		head = " > ".join(meta_1[1:]) + " > " + meta_2[0] if len(meta_1) > 2 else meta_1[1] + " > " + meta_2[0]	 

		url_part = re.findall(r'class="\s*product.*?href="(.*?)"', data)

		for item in url_part:
			url.append(item)

		print(len(url_part))

		head_part = [head] * len(url_part)

		for item in head_part:
			header.append(item)
	except Exception as e:
		print(str(e))

df_excel['Meta']=header
df_excel['URL']=url
df_excel.to_csv('header_url_data.csv',index=False)