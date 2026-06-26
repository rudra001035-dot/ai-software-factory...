import os
import zipfile
import subprocess
from agents import Agents

agent = Agents()

# ---------------------------
# FILE WRITER
# ---------------------------
def save_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)

# ---------------------------
# ZIP CREATOR
# ---------------------------
def create_zip(folder):
    zipf = zipfile.ZipFile(folder + ".zip", "w", zipfile.ZIP_DEFLATED)

    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            zipf.write(file_path, file_path)

    zipf.close()

# ---------------------------
# PARSE AI OUTPUT
# ---------------------------
def parse_output(text, folder):

    current_file = None
    buffer = []

    for line in text.split("\n"):

        if line.startswith("FILE:"):
            if current_file:
                save_file(current_file, "\n".join(buffer))

            current_file = os.path.join(folder, line.replace("FILE:", "").strip())
            buffer = []

        else:
            buffer.append(line)

    if current_file:
        save_file(current_file, "\n".join(buffer))

# ---------------------------
# GIT INIT + PUSH
# ---------------------------
def git_push(folder):

    try:
        os.chdir(folder)

        subprocess.run(["git", "init"])
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", "AI generated project"])

        print("\n⚠️ GitHub push skipped (need remote repo URL setup)")

    except Exception as e:
        print("Git Error:", e)

# ---------------------------
# AI PROJECT BUILDER V3
# ---------------------------
if __name__ == "__main__":

    print("\n🤖 AI SOFTWARE FACTORY v3 STARTED\n")

    task = input("Enter your project task: ")

    project_name = "ai_factory_project"

    prompt = f"""
You are an ELITE SOFTWARE ARCHITECT AI.

RULES:
- Output ONLY code files
- Format: FILE: filename.py
- Must be production-ready
- Must include full working project
- No explanation

TASK:
{task}
"""

    print("\n🧠 Generating project...\n")

    result = agent.manager(prompt)

    print("\n📦 AI OUTPUT RECEIVED\n")
    print(result)

    print("\n⚙️ Building project...\n")

    parse_output(result, project_name)

    # requirements auto
    save_file(project_name + "/requirements.txt", "requests\npython-dotenv\n")

    # zip export
    create_zip(project_name)

    # git init
    git_push(project_name)

    print("\n✅ VERSION 3 COMPLETE")
    print("📁 Folder:", project_name)
    print("📦 ZIP:", project_name + ".zip")
