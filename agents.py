from config import (
    LLAMA_API_KEY,
    KIMI_API_KEY,
    MIXTRAL_API_KEY,
    PHI_API_KEY
)

from models import AIClient

client = AIClient()


class Agents:

    def manager(self, task):
        return client.call(
            "https://integrate.api.nvidia.com/v1/chat/completions",
            LLAMA_API_KEY,
            "meta/llama-3.3-70b-instruct",
            f"""
You are a SYSTEM ARCHITECT AI.

Return ONLY:
- Architecture
- Steps
- Technical plan
- No storytelling

Task:
{task}
"""
        )

    def coder(self, task):
        return client.call(
            "https://integrate.api.nvidia.com/v1/chat/completions",
            KIMI_API_KEY,
            "meta/llama-3.3-70b-instruct",
            f"""
You are a SENIOR PYTHON ENGINEER.

Write ONLY working Python code.

Task:
{task}
"""
        )

    def reviewer(self, code):
        return client.call(
            "https://integrate.api.nvidia.com/v1/chat/completions",
            MIXTRAL_API_KEY,
            "mistralai/mixtral-8x7b-instruct",
            f"""
You are a CODE REVIEW ENGINE.

Find bugs and FIX them.

Return ONLY corrected code.

Code:
{code}
"""
        )

    def judge(self, outputs):
        return client.call(
            "https://integrate.api.nvidia.com/v1/chat/completions",
            LLAMA_API_KEY,
            "meta/llama-3.3-70b-instruct",
            f"""
You are FINAL AI JUDGE.

Select best output and return ONLY final clean answer.

{outputs}
"""
        )

