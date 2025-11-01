import random
import time

# ---------- Helper Functions ----------

def combine_names(name1, name2, style=1):
    """Generate nickname based on selected style."""
    n1, n2 = name1.strip().capitalize(), name2.strip().capitalize()

    if style == 1:
        # First half of name1 + second half of name2
        return n1[:len(n1)//2] + n2[len(n2)//2:]
    elif style == 2:
        # Random characters from both names
        return ''.join(random.choice(n1 + n2) for _ in range(random.randint(3, 6))).capitalize()
    elif style == 3:
        # First 3 letters of both names
        return (n1[:3] + n2[:3]).capitalize()
    elif style == 4:
        # Reversed combinations
        return (n2[::-1][:3] + n1[::-1][:3]).capitalize()
    else:
        # Default: first 2 letters of name1 + last 2 of name2
        return n1[:2] + n2[-2:]

def nickname_meaning():
    """Generate a random fun meaning for the nickname."""
    meanings = [
        "The one who shines bright 🌟",
        "The mysterious soul 🌙",
        "Full of joy and laughter 😂",
        "The creative dreamer 🎨",
        "Strong and fearless 💪",
        "A heart full of love ❤️",
        "Smart and unstoppable 🚀",
        "The charming personality ✨"
    ]
    return random.choice(meanings)

def generate_nickname():
    """Main nickname generator logic."""
    name1 = input("Enter the first name: ")
    name2 = input("Enter the second name: ")

    print("\nChoose a nickname style:")
    print("1. First half of Name1 + Second half of Name2")
    print("2. Random characters from both names")
    print("3. First 3 letters of both names")
    print("4. Reversed combination")
    print("5. Default: First 2 of Name1 + Last 2 of Name2")

    try:
        style = int(input("Enter your choice (1–5): "))
    except ValueError:
        style = 5

    nickname = combine_names(name1, name2, style)
    meaning = nickname_meaning()

    print("\n🧠 Generating nickname...")
    time.sleep(1)
    print(f"\n💫 Your nickname is: {nickname}")
    print(f"💬 Meaning: {meaning}\n")

    return nickname

# ---------- Main Program ----------

def main():
    nickname_history = []

    print("========== NICKNAME GENERATOR BOT ==========")
    while True:
        nickname = generate_nickname()
        nickname_history.append(nickname)

        again = input("Would you like to generate another nickname? (y/n): ").lower()
        if again != 'y':
            break

    print("\n🎉 Session Ended! Here’s your nickname history:")
    for i, n in enumerate(nickname_history, 1):
        print(f"{i}. {n}")
    print("\nThanks for using Nickname Generator Bot! 👋")

# ---------- Run ----------
if __name__ == "__main__":
    main()
