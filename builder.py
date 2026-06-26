import os
from agents import Agents

agent = Agents()

def save_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)

def parse_and_build(text):
    files = text.split("FILE:")

    for f in files:
        if f.strip() == "":
            continue

        try:
            header, content = f.split("\n", 1)
            filename = header.strip()

            print(f"📁 Creating: {filename}")
            save_file(filename, content.strip())

        except:
            print("⚠️ Skipped invalid block")

if __name__ == "__main__":

    print("\n🤖 AI PROJECT BUILDER STARTED")

    task = input("\nEnter your project task: ")

    prompt = f"""
You are a PROJECT BUILDER AI.

Return ONLY code files in this format:

FILE: main.py
<code here>

FILE: bot.py
<code here>

Task:
{task}
"""

    result = agent.manager(prompt)

    print("\n🧠 AI OUTPUT:\n")
    print(result)

    print("\n⚙️ Building project files...\n")

    parse_and_build(result)

    print("\n✅ PROJECT CREATED SUCCESSFULLY")
