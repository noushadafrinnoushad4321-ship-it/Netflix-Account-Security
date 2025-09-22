import time

COMMON_PASSWORDS = [
    "password", "123456", "netflix", "netflix123",
    "qwerty", "letmein", "welcome", "admin"
]

def demo(target_password: str):
    print("Simulating brute-force attack...")
    for guess in COMMON_PASSWORDS:
        print(f"Trying: {guess}")
        time.sleep(0.3)
        if guess == target_password:
            print(f"Cracked! Password='{guess}'")
            return
    print("Password not found in common passwords list.")

def main():
    target = input("Enter a sample password to test: ").strip()
    demo(target)

if __name__ == "__main__":
    main()
