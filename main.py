import json
import os
from datetime import date

DATA_FILE = "habits.json"


def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def save_data(habits):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(habits, f, indent=2)


def list_habits(habits):
    if not habits:
        print("\nNo habits yet. Add one!\n")
        return
    print("\nYour habits:")
    for i, h in enumerate(habits, start=1):
        print(f"{i}. {h['name']} (done {len(h['log'])} time(s))")
    print()


def add_habit(habits):
    name = input("New habit name: ").strip()
    if not name:
        print("Name cannot be empty.\n")
        return
    if any(h["name"].lower() == name.lower() for h in habits):
        print("That habit already exists.\n")
        return
    habits.append({"name": name, "log": []})
    save_data(habits)
    print(f"Added habit: {name}\n")


def mark_done(habits):
    if not habits:
        print("\nNo habits yet. Add one first.\n")
        return
    list_habits(habits)
    try:
        idx = int(input("Which habit did you complete today? ")) - 1
    except ValueError:
        print("Please enter a number.\n")
        return
    if not (0 <= idx < len(habits)):
        print("Invalid choice.\n")
        return
    today = date.today().isoformat()
    if today in habits[idx]["log"]:
        print("You already marked this habit as done today.\n")
        return
    habits[idx]["log"].append(today)
    save_data(habits)
    print("Nice job! Marked as done for today.\n")


def main():
    habits = load_data()
    while True:
        print("=== Habit Tracker ===")
        print("1. List habits")
        print("2. Add habit")
        print("3. Mark habit as done today")
        print("4. Quit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            list_habits(habits)
        elif choice == "2":
            add_habit(habits)
            habits = load_data()
        elif choice == "3":
            mark_done(habits)
            habits = load_data()
        elif choice == "4":
            print("Goodbye, keep building good habits! 💪")
            break
        else:
            print("Please choose 1–4.\n")


if __name__ == "__main__":
    main()
