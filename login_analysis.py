import matplotlib.pyplot as plt
from collections import Counter

LOGFILE = "logins.txt"

def parse_logs(path):
    results = []
    with open(path, "r") as f:
        for line in f:
            status = line.strip().split()[-1].lower()  # last word = status
            results.append(status)
    return results

def main():
    events = parse_logs(LOGFILE)
    counts = Counter(events)
    
    # Plot the results
    plt.bar(counts.keys(), counts.values(), color=['red', 'green'])
    plt.title("Login Attempts")
    plt.ylabel("Count")
    plt.xlabel("Status")
    plt.show()

if __name__ == "__main__":
    main()
