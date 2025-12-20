import random
import datetime

def lucky_day_picker():
    print("☘ Lucky Day Picker!")
    print("=" * 30)

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    to_do = {
        "Monday": "Sleep",
        "Tuesday": "Eat",
        "Wednesday": "Goon",
        "Thursday": "Drink",
        "Friday": "Goon",
        "Saturday": "Watch movies",
        "Sunday": "Gay"
    }

    lucky_day = random.choice(days)
    today = datetime.datetime.now().strftime("%A")

    print(f"Today is: {today}")
    print(f"Your Lucky Day is: {lucky_day}!")
    print(f"Suggested activity is: {to_do[lucky_day]}")
    print("-" * 30)
    
    if today == lucky_day:
        print("✨ WOWW TODAY IS YOUR LUCKY DAYY!! ✨")
    else:
        print("Better luck tomorrow!")

lucky_day_picker()

while True:
    lucky_day_picker()
    user_input = input("\press 1 to pick a lucky day or press 0 to exit: ")
    if user_input == "1":
        lucky_day_picker()
    elif user_input == "0":
        print("Thank you for using Lucky Day Picker. Goodbye!")
        break
    else:
        print("Invalid input. Please try again.")