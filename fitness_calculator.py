#Ask for name
name = input("What's your name please? " )

#Let's ask for weight
weight = float(input("What's your weight in kg? ") )

#Let's ask about cycling
miles = 0  # Initialize miles variable to avoid reference before assignment
cycling = input("Did you cycle this week? " )

if cycling.lower() == "yes":
    miles = float(input("How many miles did you cycle this week? ") )

if miles > 0:
    print(f"That's great! You cycled {miles} miles this week and you weigh {weight} kg.  Fantastic effort!" )
elif miles == 0:
    print("No worries! Cycling is just one of many ways to stay active. There's always next week!" )


#Let's ask about swimming

minutes = 0  # Initialize minutes variable to avoid reference before assignment
swimming = input("Did you swim this week? " )

if swimming.lower() == "yes":
    print("Great job on swimming! It's a wonderful way to stay fit." )
    minutes = float(input("How many minutes did you spend swimming this week? ") )

if minutes > 0:
    print(f"That's awesome! You spent {minutes} minutes swimming this week." )
elif minutes == 0:
    print("No worries! Swimming is just one of many ways to stay active. There's always next week!" )



#Calculate total exercise time

total_exercise_time = miles * 4 + minutes  # Assuming cycling burns 4 minutes per mile
print(f"Your total exercise time this week is {total_exercise_time} minutes." )
print("Remember, consistency is key to maintaining a healthy lifestyle. Keep up the great work!" )