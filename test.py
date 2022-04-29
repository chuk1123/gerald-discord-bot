#Just test, does nothing for the discord bot

from bs4 import BeautifulSoup
import requests
import re
import json

tasks = []

cookies={'canvas_session': "FYq22exrxEuqod4rdpsFMg+i-eEkQGhTqy3MvoCKAySOmc8lcpLpfhhA-gkvhY7FNpT3pnL5y3NnePpsbscs6HiR0AlFIfvYFpCTUJA6RDT7X69318Osp6lYkZ6CpVeXWp0ddJcIt-kgjEj32AuzSKNsjmES1f81GfJdqV6gg-H5evBkkzCxdjNSCcxgufAcphZovHsb11MeuTSQaEfep3ZKXeLBaZBi0ft5P8bBgeW5YqEq0vCkGDEfaBM14M4paTMjhLzVI2co4xlTHzjwj66kq24Aa52ockugCTjCQKCT1R6M9p60hFXVJaDX06T4xvXpiup19qSClXuEZcYCzXMka4T4pIFHYbclgtPDoOj-dMMid4au-vJH2npS_D21J1RUiAklIuIFEryLxkM7MqWcerK8NyxMlRL20QmHvSOZSskgKJJ5WDajdcqrrYFncWFgfksVefhftaUH4p_HEOP.xPoJUfQB709wwyLM8_qFaYX2XvE.Ymovmw"}
html_text = requests.get('https://iusd.instructure.com/courses/104033/pages/unit-5-day-8-work', cookies=cookies).text

soup = BeautifulSoup(html_text, 'html.parser')

print(soup.prettify)