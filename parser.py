import requests
from bs4 import BeautifulSoup
import fake_useragent

users = fake_useragent.UserAgent().random

link = 'https://browser-info.ru/'

header = {'User-agent' : users}

response = requests.get(link, headers= header).text
soup = BeautifulSoup(response, 'lxml')
block = soup.find('div', id = 'tool_padding')

# check javascript

javascript = block.find('div', id = 'javascript_check')
status_js = javascript.find_all('span')[1].text
result_js = f'javascript: {status_js}'

# check flash

flash = block.find('div', id = 'flash_version')
status_flash = flash.find_all('span')[1].text
result_flash = f'flash: {status_flash}'

# check user agent

user = block.find('div', id = 'user_agent').text
result_agent = f'user agent: {user}'

print(result_js, result_flash, result_agent, sep='\n')