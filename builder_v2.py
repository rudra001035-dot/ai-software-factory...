import os
import zipfile
from agents import Agents

agent = Agents()

def save_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)

def create_zip(folder_name):
    zipf = zipfile.ZipFile(folder_name + ".zip", "w", zipfile.ZIP_DEFLATED)

    for root, dirs, files in os.walk(folder_name):
        for file in files:
            file_path = os.path.join(root, file)
            zipf.write(file_path, file_path)

    zipf.close()

def parse_ai_output(text, project_folder):

    current_file = None
    buffer = []

    lines = text.split("\n")

    for line in lines:

        if line.startswith("FILE:"):
            if current_file:
                save_file(current_file, "\n".join(buffer))

            current_file = os.path.join(project_folder, line.replace("FILE:", "").strip())
            buffer = []

        else:
            buffer.append(line)

    if current_file:
        save_file(current_file, "\n".join(buffer))

def generate_requirements(folder):

    req = os.path.join(folder, "requirements.txt")

    content = "requests\npython-dotenv\n"

    save_file(req, content)

if __name__ == "__main__":

    print("\n🤖 AI PROJECT BUILDER v2 STARTED\n")

    task = input("Enter your project task: ")

    project_name = "ai_project"

    prompt = f"""
You are an ADVANCED SOFTWARE ENGINEER AI.

Return a FULL PROJECT with multiple files.

RULES:
- Use format: FILE: filename.py
- Only return code
- No explanation
- Clean production-ready Python code
- Must be runnable in Termux

TASK:
{task}
"""

    print("\n🧠 Generating project...\n")

    result = agent.manager(prompt)

    print("\n📦 AI OUTPUT RECEIVED\n")

    print(result)

    print("\n⚙️ Building project files...\n")

    parse_ai_output(result, project_name)

    generate_requirements(project_name)

    create_zip(project_name)

    print("\n✅ PROJECT CREATED!")
    print("📁 Folder:", project_name)
    print("📦 ZIP:", project_name + ".zip")
