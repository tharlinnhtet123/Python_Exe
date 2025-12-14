import random
import datetime
aa = random.randint(1,5)
print(f"Your number is {aa}")

students = ["may thae","yamone","min khant","wanna","Thar Linn Htet"]

ran_std = random.choice(students)

print(f"Your name is {ran_std}")

today = datetime.datetime.now().strftime("%A")
print(f"Today is {today}")
