import time
import threading
import winsound

class PomodoroTimer:
    def __init__(self, work_duration=25, short_break=5, long_break=15, long_break_interval=4):
        self.work_duration = work_duration * 60  # minutes to seconds
        self.short_break = short_break * 60  # minutes to seconds
        self.long_break = long_break * 60  # minutes to seconds
        self.long_break_interval = long_break_interval
        self.session_count = 0
        self.is_running = False
        self.history = []

    def start_timer(self, duration, label):
        print(f"{label} timer started for {duration // 60} minutes.")
        self.is_running = True
        while duration > 0 and self.is_running:
            mins, secs = divmod(duration, 60)
            time_format = f'{mins:02d}:{secs:02d}'
            print(time_format, end='\r')
            time.sleep(1)
            duration -= 1
        
        if self.is_running:
            self.session_count += 1 if label == "Work" else 0
            self.history.append(f"Completed: {label} session")
            winsound.Beep(1000, 1000)  # Notify the user when the session ends
            print(f"{label} session ended.")
            self.is_running = False

    def start_pomodoro(self):
        threading.Thread(target=self._pomodoro_cycle).start()

    def _pomodoro_cycle(self):
        while self.is_running:
            self.start_timer(self.work_duration, "Work")
            if self.session_count % self.long_break_interval == 0 and self.session_count != 0:
                self.start_timer(self.long_break, "Long Break")
            else:
                self.start_timer(self.short_break, "Short Break")

    def stop_timer(self):
        if self.is_running:
            print("Timer stopped.")
            self.is_running = False

    def reset_timer(self):
        self.is_running = False
        self.session_count = 0
        self.history = []
        print("Timer reset.")

    def view_history(self):
        if self.history:
            print("Session History:")
            for entry in self.history:
                print(entry)
        else:
            print("No sessions completed yet.")

    def set_custom_durations(self, work_duration=None, short_break=None, long_break=None):
        if work_duration:
            self.work_duration = work_duration * 60
        if short_break:
            self.short_break = short_break * 60
        if long_break:
            self.long_break = long_break * 60
        print("Durations updated.")

def print_menu():
    print("\nPomodoro Timer")
    print("1. Start Pomodoro")
    print("2. Stop Timer")
    print("3. Reset Timer")
    print("4. View Session History")
    print("5. Set Custom Durations")
    print("6. Exit")
    print("\nSelect an option:")

def main():
    pomodoro = PomodoroTimer()
    while True:
        print_menu()
        choice = input()

        if choice == '1':
            if not pomodoro.is_running:
                pomodoro.is_running = True
                pomodoro.start_pomodoro()
            else:
                print("Pomodoro is already running!")
        elif choice == '2':
            pomodoro.stop_timer()
        elif choice == '3':
            pomodoro.reset_timer()
        elif choice == '4':
            pomodoro.view_history()
        elif choice == '5':
            work_duration = int(input("Enter work duration (minutes): "))
            short_break = int(input("Enter short break duration (minutes): "))
            long_break = int(input("Enter long break duration (minutes): "))
            pomodoro.set_custom_durations(work_duration, short_break, long_break)
        elif choice == '6':
            print("Exiting Pomodoro Timer.")
            if pomodoro.is_running:
                pomodoro.stop_timer()
            break
        else:
            print("Invalid option, please select again.")

if __name__ == "__main__":
    main()