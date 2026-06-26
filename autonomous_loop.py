import time
from agents import Agents
from memory import add_memory

agent = Agents()

def generate_task():
    return "Improve previous AI system or fix last error"

def is_bad(output):
    if output is None:
        return True
    if "error" in str(output).lower():
        return True
    return False


while True:

    print("\n🤖 AUTONOMOUS LOOP START")

    task = generate_task()
    print("TASK:", task)

    try:

        plan = agent.manager(task)
        code = agent.coder(plan)
        review = agent.reviewer(code)
        final = agent.judge(plan + code + review)

        print("\nFINAL OUTPUT:\n", final)

        # Save memory
        add_memory(task, final)

        # Self healing
        if is_bad(final):
            print("\n⚠️ ERROR DETECTED → SELF HEALING")

            fixed = agent.reviewer(code + "\nFIX IT")
            final = agent.judge(fixed)

            add_memory(task + " (FIXED)", final)

    except Exception as e:
        print("CRASH:", e)
        add_memory(task, str(e))

    print("\n⏳ Sleeping 10 sec...\n")
    time.sleep(10)

