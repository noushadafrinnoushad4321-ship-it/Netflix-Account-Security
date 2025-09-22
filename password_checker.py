import re

def score_password(pw: str) -> str:
    length = len(pw)
    checks = [
        bool(re.search(r"[a-z]", pw)),
        bool(re.search(r"[A-Z]", pw)),
        bool(re.search(r"\d", pw)),
        bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", pw))
    ]
    points = sum(checks) + (1 if length >= 12 else 0)

    if length < 6 or points <= 1:
        return "Weak"
    if points == 2 or points == 3:
        return "Medium"
    return "Strong"

def main():
    pw = input("Enter a password to check: ").strip()
    rating = score_password(pw)
    print(f"Password strength: {rating}")

if __name__ == "__main__":
    main()
