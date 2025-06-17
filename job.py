import requests
from bs4 import BeautifulSoup

link = 'https://www.infojobs.com.br/empregos.aspx?palabra=estagio+ti&provincia=176'

response = requests.get(link)

if response.status_code == 200:
    print('STATUS: ',response.status_code,'- Request successful!')
    print('URL: ', response.url)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    jobs = soup.find_all('div', class_='card')
    print(f'Found {len(jobs)} job postings:')
    
    for job in jobs:
        print('-----------------------------------')
        name = job.find('h2', class_='h3 font-weight-bold text-body mb-8')
        name = str(name)
        print('Job Title:', name.replace('<h2 class="h3 font-weight-bold text-body mb-8">', '').strip().replace('</h2>',''))
else:
    print('STATUS: ',response.status_code,'- Request failed with status code:', response.status_code)