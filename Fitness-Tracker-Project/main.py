import datetime
import json

# Function to load existing data from the file
def load_data():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data

# Function to save data to the file
def save_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

# Function to calculate the total calories burned for a specific date
def calculate_total_calories(data, date):
    total_calories = 0
    if date in data:
        for entry in data[date]:
            total_calories += entry['calories']
    return total_calories

# Function to add a new exercise entry
def add_exercise(data):
    exercise_date = input("Enter the exercise date (YYYY-MM-DD): ")
    exercise_name = input("Enter the exercise name: ")
    exercise_calories = int(input("Enter the calories burned: "))

    entry = {
        'name': exercise_name,
        'calories': exercise_calories
    }

    if exercise_date in data:
        data[exercise_date].append(entry)
    else:
        data[exercise_date] = [entry]

    save_data(data)
    print("Exercise entry added successfully!")

# Function to display the total calories burned for a specific date
def display_total_calories(data):
    date = input("Enter the date to display total calories burned (YYYY-MM-DD): ")
    total_calories = calculate_total_calories(data, date)
    print(f"Total calories burned on {date}: {total_calories}")

# Main function
def main():
    print("Fitness Tracker")

    data = load_data()

    while True:
        print("\n1. Add Exercise Entry")
        print("2. Display Total Calories Burned")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_exercise(data)
        elif choice == '2':
            display_total_calories(data)
        elif choice == '3':
            print("Thank you for using Fitness Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
