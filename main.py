import time, random, difflib
try:
    import pyautogui
except (ImportError, ModuleNotFoundError, Exception):
    import os
    os.system("pip install pyautogui")
finally:
    import pyautogui

def is_done(word):
    return difflib.get_close_matches(word.lower(), ["done", "d"], n=1, cutoff=0.6)

def collect_messages():
    messages = []
    print("Enter your messages one by one.")
    print("Type 'done' when finished.\n")

    while True:
        msg = input("Message: ").strip()
        if is_done(msg):
            break
        if msg:
            messages.append(msg)

    return messages

def type_message(messages):
    chosen = random.choice(messages)
    print(f"\nSelected message: {chosen}")
    
    input("Focus the text field and press Enter to type the message...")
    try:
        n = int(input("How many times to send the message? (default 5): ").strip())
    except (ValueError, Exception):
        n = 5
    time.sleep(5)

    # pyautogui.typewrite(chosen, interval=0.05)
    # pyautogui.press("enter")
    
    for send in range(n):
        pyautogui.typewrite(chosen, interval=0.05)
        pyautogui.press("enter")
        print(f"Sent {send + 1} of {n}")
        time.sleep(1)

    print("Message typed!\n")

def main():
    while True:
        messages = collect_messages()

        if not messages:
            print("No messages were entered.")
            return

        type_message(messages)

        print("Message list cleared.")

        again = input("Do you want to enter new messages? (yes/no): ").strip().lower()
        if difflib.get_close_matches(again, ["no", "n"], n=1, cutoff=0.6):
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
