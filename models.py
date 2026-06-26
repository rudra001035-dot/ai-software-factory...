import requests

class AIClient:

    def call(self, url, api_key, model, message):

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "model": model,
            "messages": [
                {"role": "user", "content": message}
            ],
            "temperature": 0.6,
            "max_tokens": 1000
        }

        try:
            res = requests.post(url, headers=headers, json=data)
            out = res.json()

            if "choices" in out:
                return out["choices"][0]["message"]["content"]
            return str(out)

        except Exception as e:
            return f"ERROR: {str(e)}"

