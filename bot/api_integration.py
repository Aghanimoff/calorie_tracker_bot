import requests
from .config import OPENAI_API_KEY

def analyze_user_input(input_text):
    try:
        response = requests.post("https://api.openai.com/v1/engines/davinci/completions",
                                 headers={"Authorization": f"Bearer {OPENAI_API_KEY}"},
                                 json={"prompt": input_text, "max_tokens": 150})
        if response.status_code == 200:
            return response.json()["choices"][0]["text"]
        else:
            return "Произошла ошибка при обработке вашего запроса."
    except Exception as e:
        return str(e)
