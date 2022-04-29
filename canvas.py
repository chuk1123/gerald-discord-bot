def find_tasks(url):

    from bs4 import BeautifulSoup
    import requests
    import re
    import json

    tasks = []

    cookies={'canvas_session': "nVNkLUfpb-2uBlruR6sipw+p4Tw2zK0gG2Prvm9M8dGS6RWwjUJfqWvdCPdDk2_qmU46svfw5S3mKktmf5oOt8dCfuyywP79pdywV5TJLiEkGTUaBHVzPaP17n6DerKCE3NY6F7O5l0FIcTvRw9IsaUdQQXUh-8RixjBZe5zdZSHquI51Hjq5aT5gAn-7y4rFmfp-r-pkLWQqcGj0oOF76eX2zrXDDU-9a4clbCys7VIGhP1S9KHGdj1yp2p7c8wNBqAYgtAqQiP0o0WYVAbeLyaN5eGOVQp6v5QlKUbAV6D2NLSfst2w-csMqsAFsWEomN5AIcFxowpyEssPHJvCYyp9n6RmFHFYYosn9besUqbZ04PWgQyE71eNt-E2MBP-Eg_hhtwrOLiXyRhFTZeiVCrTBGB2LJJbOvzkWNdCc52A.ocBO-qNgVWpoaZDSFy3_fovoRNE.Ymv_zA"}
    html_text = requests.get(url, cookies=cookies).text

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