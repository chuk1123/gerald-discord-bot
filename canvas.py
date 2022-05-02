from bs4 import BeautifulSoup
import requests
import json

def find_tasks(url, cookies):

    tasks = []
    
    html_text = requests.get(url, cookies={'canvas_session':cookies}).text
    soup = BeautifulSoup(html_text, 'html.parser')

    script_tag = soup.find_all('script')
    data = script_tag[2].text.strip()[3896:-1149]
    try:
        data = json.loads(data)
        data = data['WIKI_PAGE']['body']

        soup2 = BeautifulSoup(data, 'html.parser')

        work = soup2.find_all('p')
        
        for w in work:
            link = w.find('a')
            if link:
                tasks.append([w.text, link['href']])
            else:
                tasks.append([w.text, None])

        tasks.pop(1)
        return tasks
    
    except:
        print("Couldn't log in. Need new cookies")
        
    return []

def find_cookies():
    s = requests.Session()

    loginurl = 'https://iusd.instructure.com/login/ldap'
    r = s.get(loginurl)
    temp_soup = BeautifulSoup(r.content, 'html.parser')
    
    auth_token = temp_soup.find('input', attrs={'name': 'authenticity_token'})['value']
    payload = {'utf8': '✓', 
    'authenticity_token': auth_token, 
    'redirect_to_ssl': '1', 
    'pseudonym_session[unique_id]': '24ChuKevin', 
    'pseudonym_session[password]': '512190105', 
    'pseudonym_session[remember_me]': '1'}

    response = s.post(loginurl, data=payload)
    cookies = response.cookies['canvas_session']

    return cookies