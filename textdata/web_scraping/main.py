import requests
from bs4 import BeautifulSoup
import time

website_content = requests.get(
    'https://www.livius.org/sources/content/achaemenid-royal-inscriptions/')

website_soup = BeautifulSoup(website_content.text, 'html.parser')
first_tbody_element = website_soup.find_all('tbody')[1]
for i in first_tbody_element.find_all('tr'):
    if (i.td.get('colspan') == None):
        if (i.td.a != None):
            modified_link = ''
            if (i.td.a.get('href')[0] == '/'):
                modified_link = 'https://www.livius.org' + i.td.a.get('href')
            else:
                modified_link = i.td.a.get('href')

            link_content = requests.get(modified_link)
            if (link_content.status_code == 200):
                link_soup = BeautifulSoup(link_content.text, 'html.parser')
                file = open(i.td.a.get_text() + '.txt',
                            'w', encoding='utf-8')
                file.write(link_soup.get_text())
                file.close()
                print('---------- ' + i.td.a.get_text() +
                      ' / Exported ----------')
            else:
                print('---------- ' + i.td.a.get_text() + ' / Error ----------')

            time.sleep(1)
