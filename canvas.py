def find_tasks(url):

    from bs4 import BeautifulSoup
    import requests
    import re
    import json

    tasks = []

    cookies = 'HYO8BdYRoRad-w0DQ6wpyA+wy8ALbmRkYMIbns6DOF01oeT4hO6IX5fUEbn1tgXIZTqPBCWaBYx2BWYE24bDSlxqDBu7TbfAr-tRQtp5L08BxwfG9gDldavN-a1BMap0ZMAaFA9jxUOfHWzlB1qjZ15GEtr_QATQrgj7o_ESSgG1J7q3BEK-DWaNSUOud7paetiRmBDxbbIXwS6hLVsruccVIhjxEm6rca4B-L0KjblA5KE55WzXnN7bLw70Cn9OyABa9WUdv_HbqDk-tpyguGPZGBONJpiAbRreZWxNjOGJ94dxIjkhvK4yOAL8PpuCn_v5lVCI1hubVzMw_rtYH1GAfeemKvq13ZqUv5ZBUqir5ZT0C2SmcGBsc7veHnT9tZKZwk6xZLYPQRLU2QAJq42P71zG-3JZQZpyG3ThS1C1rI194d7War20Ru7Skip33c.0dvtwi1thsrjaF-XoXSA0kckIGE.Ym2AZQ'
    
    html_text = requests.get(url, cookies={'canvas_session':cookies}).text

    soup = BeautifulSoup(html_text, 'html.parser')

    script_tag = soup.find_all('script')

    data = script_tag[2].text.strip()[3896:-1149]

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