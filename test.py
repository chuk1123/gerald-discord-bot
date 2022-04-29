def find_tasks(url):

    from bs4 import BeautifulSoup
    import requests
    import re
    import json

    tasks = []

    cookies={'canvas_session': "Ly_TcOpo4r2r2jgogKuAhg+xbtRLFrPt3JI1pTK0lBrAbKWQ47oOWtyfyhU01GCfu5jWKL5slbB5uglHG37m8xRi4oHPmMfn5a85n5ajFnwoXbPe0Uy8xBR1_vvGCV9HS3r5ZeYPKYGVFt2kmVHhMvSuwllX7GV8L6yCfzNuz7eMiuNgQacTw7i8C-F5q_3qUvMovBrVRy88a7eP3GRfIVHD3SBFuVOHr_THnPi9pJ6u_40XOkm6aJar0VEClbnbflO1Y64DIAM9vMcTSYcmRTVKd18fjVPFBQGvMJRp-1jtIJ0SLkRQCeGbj39skHVXh5tdx-FSibbavFNjtnPWNHOcXGrUdxvqKbjyO9xmkrg8XdlxrDaxSmEHPVlvHA2cIXTG0nntFi6gb-BlVSeNkcf7hVveVbaEAO2FOZzyYAPpBno8A2tokhPNWnyawTBcF3F3vwh2gYPSn87U2kMMoo8N1TWXXliuuYSV4hts3gp-lOfVD0V6vnfwMcIosdMPOS4ZZ5s-xqMAhAexjNzLeMS6BYFHw6NLcVdBQ7WF1Qa0g.TZ05DyiNHnC_PTPS6A0KwBdTgqQ.Ymvy2w"}
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