from datetime import datetime

userInput = input("Enter your goal with a deadline seperated by colon example: learn python:20.08.2021\n")
while ":" not in userInput:
    userInput = input("Please seperate by colon. Try again:\n")
inputList = userInput.split(":")

goal = inputList[0]
deadline = inputList[1]


deadlineDate = datetime.strptime(deadline, "%d.%m.%Y")
todayDate = datetime.today()
daysRemaining = deadlineDate - todayDate
hoursRemaining = int(daysRemaining.total_seconds() / 60 / 60)
print(f"Dear user! Time remaining to {goal}: is {daysRemaining} days and in hours: {hoursRemaining}h.")