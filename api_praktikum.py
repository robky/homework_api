from pprint import pprint
import requests
import os
import datetime as DT
from dotenv import load_dotenv

load_dotenv()
# Теперь переменная TOKEN, описанная в файле .env,
# доступна в пространстве переменных окружения

token = os.getenv('TOKEN')
date = DT.datetime.fromisoformat('2022-03-01 00:00:00')

url = 'https://practicum.yandex.ru/api/user_api/homework_statuses/'
headers = {'Authorization': f'OAuth {token}'}
payload = {'from_date': int(date.timestamp())}

# Делаем GET-запрос к эндпоинту url с заголовком headers и параметрами params
homework_statuses = requests.get(url, headers=headers, params=payload)

# Печатаем ответ API в формате JSON
# print(homework_statuses.text)

# А можно ответ в формате JSON привести к типам данных Python и напечатать и
# его
pprint(homework_statuses.json())
