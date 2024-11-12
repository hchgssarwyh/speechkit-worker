import requests
import json
from schemes import Root
import os
from dotenv import load_dotenv

url = 'https://stt.api.cloud.yandex.net/stt/v3/getRecognition'
# Загружаем переменные из .env файла
load_dotenv()
# Доступ к переменным окружения
api_key = os.getenv('API_KEY')
folder_id = os.getenv('FOLDER_ID')
headers = {
    'Authorization': f'Bearer {api_key}',
    'x-folder-id': folder_id
}
# В это поле нужно вставить id, который мы получили при отправке файла
file_id = 'your_file_id'
# Выполняем запрос к API
result = requests.get(url + '?operationId=' + file_id, headers=headers)

response_text = result.text
json_objects = response_text.splitlines()  # Разбиваем ответ по строкам

parsed_data = []  # Здесь будем хранить распарсенные данные

for obj in json_objects:
    try:
        # Преобразуем строку JSON в объект
        parsed_obj = json.loads(obj)

        # Теперь десериализуем в модель Pydantic, используя метод from_dict
        root_obj = Root.from_dict(parsed_obj)

        parsed_data.append(root_obj)

    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
    except Exception as e:
        print(f"Ошибка при десериализации в модель: {e}")

# Теперь обработаем данные и соберем текст по спикерам
speaker_texts = {}

# Пройдем по всем результатам в parsed_data
for data in parsed_data:
    # Проверяем, есть ли результат (result) и его финальные альтернативы (final)
    if data.result and data.result.final:
        for alternative in data.result.final.alternatives:
            text = alternative.text  # Получаем текст из альтернативы
            speaker_tag = alternative.speakerTag if hasattr(alternative, 'speakerTag') else 'unknown'  # Получаем speakerTag (если есть)

            # Сохраняем или выводим текст по спикерам
            if speaker_tag:
                if speaker_tag not in speaker_texts:
                    speaker_texts[speaker_tag] = []
                speaker_texts[speaker_tag].append(text)

# Выводим собранный текст по каждому спикеру
for speaker, texts in speaker_texts.items():
    print(f"Спикер {speaker}:")
    print(" ".join(texts))
    print()
