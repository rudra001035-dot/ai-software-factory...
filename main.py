from agents import Agents

def is_bad(output):
    if output is None:
        return True
    if "error" in str(output).lower():
        return True
    if len(str(output)) < 50:
        return True
    return False


if __name__ == "__main__":

    print("\n🤖 AUTONOMOUS AI SYSTEM STARTED")

    task = input("\nEnter your task: ")

    agent = Agents()

    print("\n[PHASE 1 - MANAGER]")
    plan = agent.manager(task)
    print(plan)

    print("\n[PHASE 2 - CODER]")
    code = agent.coder(plan)
    print(code)

    print("\n[PHASE 3 - REVIEWER]")
    review = agent.reviewer(code)
    print(review)

    print("\n[PHASE 4 - JUDGE]")
    final = agent.judge(plan + code + review)
    print(final)

    # 🔁 AUTONOMOUS SELF-RETRY LOOP
    if is_bad(final):
        print("\n⚠️ Output weak detected → AUTO IMPROVING...")

        improved_code = agent.reviewer(code + "\n" + review)
        final = agent.judge(improved_code)

        print("\n[IMPROVED FINAL OUTPUT]")
        print(final)

    print("\n✅ DONE")
