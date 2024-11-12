import requests
import time
import json
import base64
import os
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

# Доступ к переменным окружения
api_key = os.getenv('API_KEY')
folder_id = os.getenv('FOLDER_ID')
audio_file_path = 'output.wav'

# Открываем аудиофайл и кодируем в base64
with open(audio_file_path, 'rb') as audio_file:
    audio_content = base64.b64encode(audio_file.read()).decode('utf-8')

# Заголовки для запроса
# Заголовки для запроса
headers = {
    'Authorization': f'Bearer {api_key}',
    'x-folder-id': folder_id
}

# Данные для конфигурации запроса
data = {
    "content": audio_content,  # или используйте "uri": "your_file_uri" если файл доступен по ссылке
    "recognitionModel": {
        "model": "general",
        "audioFormat": {
            "rawAudio": {
                "audioEncoding": "LINEAR16_PCM",
                "sampleRateHertz": 16000,     # Частота дискретизации
                "audioChannelCount": 1        # Один канал (моно)
            }
        },
        "textNormalization": {
            "textNormalization": "TEXT_NORMALIZATION_ENABLED",
            "profanityFilter": False,
            "literatureText": True,
            "phoneFormattingMode": "PHONE_FORMATTING_MODE_DISABLED"
        },
        "languageRestriction": {
            "restrictionType": "WHITELIST",
            "languageCode": ["ru-RU", "ru"]
        },
        "audioProcessingType": "FULL_DATA"
    },
    "speechAnalysis": {
        "enableSpeakerAnalysis": True,  # Включаем анализ спикеров
        "enableConversationAnalysis": True,  # Включаем анализ разговора
        "descriptiveStatisticsQuantiles": ["0.5"]
    },
    "speakerLabeling": {
        "speakerLabeling": "SPEAKER_LABELING_ENABLED"
    }
}

# URL для запроса
url = f'https://stt.api.cloud.yandex.net/stt/v3/recognizeFileAsync'


# Выполнение запроса
try:
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()  # Проверяем на ошибки HTTP
    print("Запрос успешно выполнен, анализ речи начался.")
    print("Ответ от сервера:", response.json())
except requests.exceptions.RequestException as e:
    print(f"Ошибка при отправке запроса: {str(e)}")
    if response is not None:
        print(f"Ответ от сервера: {response.text}")
