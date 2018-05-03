try:
	from lib import *
	from bs4 import BeautifulSoup
except ImportError or ValueError:
	print('gunakan python3 ya gan, masih ada issue kalo pake python dibawah 3 \nhttps://stackoverflow.com/questions/27327901/python-valueerror-chr-arg-not-in-range256')
	exit()
import shlex
import subprocess
import requests
from termcolor import colored
import sys
import time
import signal
def proxygratis():
	tidak_ada = 0
	#print(colored(banner, "blue"))
	nama = 'proxy.txt'
	save = open(nama, 'w+')
	save.write('')
	#req = urllib.request.Request('https://free-proxy-list.net/anonymous-proxy.html')
	#req.add_header('User-agent', 'Mozilla/5.0 (X11; Linux i686; rv:45.0) Gecko/20100101 Firefox/45.0')
	headers1 = {'Cookie':'wordpress_test_cookie=WP Cookie check',
				'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:45.0) Gecko/20100101 Firefox/45.0',
				'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
				'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
				'Accept-Encoding': 'none',
				'Accept-Language': 'en-US,en;q=0.8',
				'Connection': 'keep-alive'}
	resp = requests.get('https://free-proxy-list.net/anonymous-proxy.html', headers=headers1)
	#sol = urllib.parse.unquote(urllib.parse.unquote(resp.text))
	soup = BeautifulSoup(resp.text, "lxml")
	#soup = BeautifulSoup(res, "lxml")

	data = []
	table = soup.find('table', attrs={'class':'table table-striped table-bordered'})
	table_body = table.find('tbody')

	rows = table_body.find_all('tr')
	for row in rows:
	    cols = row.find_all('td')
	    cols = [ele.text.strip() for ele in cols]
	    data.append([ele for ele in cols if ele])
	i = 1
	x = {}
	for datas in data:
		x[i] = datas[0]+':'+datas[1]
		i = i + 1

	masuk = 0
	cek = 0
	j = 1
	hidup = 0
	while j < i:
		data = x[j]
		a = 0
		for titik2 in list(data): 
			if titik2 == ':':
				batas = a 
				break
			a = a + 1

		data_ = data[:batas]
		def ping(data_):
			cmd=shlex.split("ping -c1 "+data_)
			try:
				output = subprocess.check_output(cmd)
			except subprocess.CalledProcessError:
				hidup = 0
			except socket.gaierror:
				hidup = 0
			except subprocess.CalledProcessError:
				hidup = 0
			else:
				hidup = 1
			return hidup

		def signal_handler(signum, frame):
			raise Exception("tidak_ada")

		signal.signal(signal.SIGALRM, signal_handler)
		signal.alarm(2)   # Ten seconds
		try:
			cek = cek + 1
			if ping(data_) == 0:
				tidak_ada = 0
			elif ping(data_) == 1:
				save.write(data+'\n')
				masuk = masuk + 1
		except Exception:
			tidak_ada = 0
		sys.stdout.write('proxy di cek > '+str(cek)+' | proxy hidup > '+str(masuk))
		sys.stdout.flush()
		sys.stdout.write('\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b')
		sys.stdout.write('\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b')
		sys.stdout.write('\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b')
		sys.stdout.write('\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b')
		j = j + 1
	save.close()
	keluar = 'proxy di cek > '+str(cek)+' | proxy hidup > '+str(masuk)
	return keluar

banner = open('banner.txt').read()
print(banner)

print(proxygratis())