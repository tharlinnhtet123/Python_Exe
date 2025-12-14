import random
import datetime

def lucky_day_picker():
    print("☘Lucky Day Picker!")
    print("=" * 30)

    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    
    to_do = {
        "Monday", "Sleep"
        "Tuesday", "Eat"
        "Wednesday","Goon"
        "Thursday","Drink"
        "Friday", "Goon"
        "Saturday", "Watch movies"
        "Sunday", "Gay"
    }

    lucky_day = random.choice(days)

    print(f"Your Lucky Day is {lucky_day}!")
    print(f"Suggested activicty is: {to_do[lucky_day]}")
    
    today = datetime.datetime.now().strftime("%A")
    print(f"Today is : {today}")
    
    if (today == lucky_day):
        print("WOWW TODAY IS YOUR LUCKY DAYY!!")
    else:
        print(f"Your Lucky Day is {lucky_day}!")
lucky_day_picker()
