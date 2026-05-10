import re
import time
import random
import string
import hashlib

# ---------------- HASH FUNCTION ----------------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# ---------------- PROGRESS BAR ----------------
def show_progress_bar(score):
    bar_length = 20
    filled = int(bar_length * score // 100)
    bar = "█" * filled + "░" * (bar_length - filled)
    print(f"\nProgress: |{bar}| {score}/100")


# ---------------- SMART SUGGESTIONS ----------------
def smart_suggestions(password, score):
    suggestions = []

    if score <= 40:
        suggestions.append("❌ Very weak password — unsafe")

    if len(password) < 12:
        suggestions.append("🔐 Use 12–16 characters")

    if not re.search(r"[A-Z]", password):
        suggestions.append("🔤 Add uppercase letters")

    if not re.search(r"[a-z]", password):
        suggestions.append("🔡 Add lowercase letters")

    if not re.search(r"[0-9]", password):
        suggestions.append("🔢 Add numbers")

    if not re.search(r"[@$!%*?&#]", password):
        suggestions.append("💥 Add special characters")

    if re.search(r"(.)\1\1", password):
        suggestions.append("🚨 Avoid repeated characters")

    return suggestions


# ---------------- SAVE PASSWORD (HASHED) ----------------
def save_password(password):
    hashed = hash_password(password)

    with open("passwords.txt", "a") as file:
        file.write(hashed + "\n")


# ---------------- PASSWORD GENERATOR ----------------
def generate_password(length=12):
    if length < 8:
        length = 8

    chars = string.ascii_letters + string.digits + "@$!%*?&#"

    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice("@$!%*?&#")
    ]

    for i in range(length - 4):
        password.append(random.choice(chars))

    random.shuffle(password)
    final_password = "".join(password)

    # Save hashed password
    save_password(final_password)

    return final_password


# ---------------- PASSWORD CHECKER ----------------
def check_password_strength(password):
    score = 0

    print("\n===== PASSWORD ANALYZER =====\n")

    if len(password) >= 8:
        score += 20
    if re.search(r"[A-Z]", password):
        score += 20
    if re.search(r"[a-z]", password):
        score += 20
    if re.search(r"[0-9]", password):
        score += 20
    if re.search(r"[@$!%*?&#]", password):
        score += 20

    print("Analyzing...\n")
    time.sleep(1)

    show_progress_bar(score)

    # Strength level
    if score <= 40:
        print("\n❌ Strength: Weak Password")
    elif score <= 60:
        print("\n⚠️ Strength: Moderate Password")
    elif score <= 80:
        print("\n🔐 Strength: Strong Password")
    else:
        print("\n🔥 Strength: Very Strong Password")

    # Suggestions
    suggestions = smart_suggestions(password, score)

    print("\n===== SMART SUGGESTIONS =====")
    for s in suggestions:
        print("-", s)


# ---------------- MAIN MENU ----------------
def main():
    print("\n===== CYBER SECURITY TOOL =====")
    print("1. Check Password Strength")
    print("2. Generate Strong Password")

    choice = input("\nEnter choice (1/2): ")

    if choice == "1":
        password = input("\nEnter password: ")
        check_password_strength(password)

    elif choice == "2":
        length = int(input("Enter password length (min 8): "))

        print("\nGenerating secure password...\n")
        time.sleep(1)

        new_password = generate_password(length)

        print("🔥 Generated Password:", new_password)
        print("💾 Saved securely (hashed) in passwords.txt")

    else:
        print("❌ Invalid choice")


# RUN PROGRAM
main()