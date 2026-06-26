import os
from dotenv import load_dotenv

load_dotenv()

LLAMA_API_KEY = os.getenv("LLAMA_API_KEY")
KIMI_API_KEY = os.getenv("KIMI_API_KEY")
MIXTRAL_API_KEY = os.getenv("MIXTRAL_API_KEY")
PHI_API_KEY = os.getenv("PHI_API_KEY")
