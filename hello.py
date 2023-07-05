import time
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def focus_timer(duration):
    end_time = time.time() + duration * 60
    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        timer = f"{minutes:02d}:{seconds:02d}"
        print(f"Remaining time: {timer}", end="\r")
        time.sleep(1)
    print("Focus time is over!")

if __name__ == "__main__":
    clear_console()
    print("Welcome to the Focus Timer!")
    duration = int(input("Enter the duration (in minutes): "))
    focus_timer(duration)
