import requests
from bs4 import BeautifulSoup
import json
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
from fake_useragent import UserAgent
disable_warnings(InsecureRequestWarning)

ua = str(UserAgent().random)
headers = {'User-Agent': ua}
url = 'https://ro.umich.edu/calendars/schedule-of-classes/locations'

html = requests.get(url, headers=headers, verify=False)
soup = BeautifulSoup(html.text, 'html.parser')

paragraphs = soup.find_all('p')

abbreviations_map = {}

for p in paragraphs:
    strong_tag = p.find('strong')
    if strong_tag:
        abbreviation = strong_tag.text.strip()
        parts = p.get_text(separator='|').split('|')
        if len(parts) >= 3:
            name = parts[1].strip()
            campus = parts[2].strip()
            abbreviations_map[abbreviation] = {'name': name, 'campus': campus}

with open('abbreviations.json', 'w') as json_file:
    json.dump(abbreviations_map, json_file, indent=4)

