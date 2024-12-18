import datetime
print("Sleeping")
current_time = datetime.datetime(2024, 10, 23, 6, 50, 0) 
print(current_time.strftime("%H:%M:%S"), end='\r')

while True:
    noise = str.lower(input("Hear noise? y/n: "))

    if noise == "y":
        break
    elif noise == "n":
        print("Continue sleeping")
        current_time += datetime.timedelta(minutes=15)
    else:
        print("invalid response")
        
print(current_time.strftime("%H:%M:%S"), end='\r')
        
while True:            
    school = str.lower(input("Do I have to go to school today? y/n: "))

    if school == "y":
        break
    elif school == "n":
        print("Continue sleeping until I want to wake up")
        print ("Wake up")
        print ("Start my day however I want")
        quit()
    else:
        print("invalid response")
        
print(current_time.strftime("%H:%M:%S"), end='\r')
        
while True:
    unwell = str.lower(input("Am I feeling unwell? y/n: "))

    if unwell == "y":
        print("Continue sleeping until I want to wake up")
        print ("Wake up")
        print ("Start my day however I want")
        quit()
    elif unwell == "n":
        print("Go downstairs to the kitchen")
        print("Eat breakfast")
        current_time += datetime.timedelta(minutes=5)
        break
    else:
        print("invalid response")

print(current_time.strftime("%H:%M:%S"), end='\r')

while True:
    breakfast = str.lower(input("What do I want to have? bread/meat/coffee/fruit: "))
    morefood = str.lower(input("Do I want anything else? y/n: "))

    if breakfast == "bread":
        if morefood == "n":
                current_time += datetime.timedelta(minutes=5)
                break

    elif breakfast == "meat":
        if morefood == "n":
                current_time += datetime.timedelta(minutes=5)
                break
        
    elif breakfast == "coffee":
        if morefood == "n":
                current_time += datetime.timedelta(minutes=5)
                break
       
    elif breakfast == "fruit":
        if morefood == "n":
                current_time += datetime.timedelta(minutes=5)
                break
        
    else:
        print("invalid response")

print(current_time.strftime("%H:%M:%S"), end='\r')
        
while True:
    finishfood = str.lower(input("Have I finished my food? y/n: "))

    if finishfood == "n":
        print("Continue eating")
        current_time += datetime.timedelta(minutes=20)
    elif finishfood == "y":
        print("Go upstairs")
        print("Go to bathroom to brush teeth")
        current_time += datetime.timedelta(minutes=10)
        break
    else:
        print("invalid response")

print(current_time.strftime("%H:%M:%S"), end='\r')

while True:
    weather = str.lower(input("Is it below 65 degrees today? y/n: "))

    if weather == "n":
        print("Change and don't wear two layers")
        print("Prepare backpack")
        current_time += datetime.timedelta(minutes=10)
        break
    elif weather == "y":
        print("Change")
        print("Wear two layers")
        print ("Prepare backpack")
        current_time += datetime.timedelta(minutes=10)
        break
    else:
        print("invalid response")
        
print(current_time.strftime("%H:%M:%S"), end='\r')

while True:
    leave = str.lower(input("Is my dad ready to drive me to school? y/n: "))

    if leave == "n":
        print("Wait")
        current_time += datetime.timedelta(minutes=10)
    elif leave == "y":
        print("Go into car")
        current_time += datetime.timedelta(minutes=5)
        break
    else:
        print("invalid response")

print(current_time.strftime("%H:%M:%S"), end='\r')

while True:
    arrive = str.lower(input("Have we arrived to school? y/n: "))

    if arrive == "n":
        print("Wait")
        current_time += datetime.timedelta(minutes=10)
    elif arrive == "y":
        print("Get out of car")
        print ("Go into school")
        print ("Go through school day")
        current_time += datetime.timedelta(minutes=420)
        break
    else:
        print("invalid response")

print(current_time.strftime("%H:%M:%S"), end='\r')

while True:
    school_day = str.lower(input("Has school finished? y/n: "))

    if school_day == "n":
        print("Wait for classes to finish")
        current_time += datetime.timedelta(minutes=30)
    elif school_day == "y":
        break
    else:
        print("invalid response")
        
print(current_time.strftime("%H:%M:%S"), end='\r')

while True:
    gym = str.lower(input("Do I have to go to the gym today? y/n: "))

    if gym == "n":
        print("Wait for my mom to pick me up from school")
        break
    elif gym == "y":
        print("Workout")
        current_time += datetime.timedelta(minutes=60)
        break
    else:
        print("invalid response")

print(current_time.strftime("%H:%M:%S"), end='\r')

while True:
    home = str.lower(input("Has mom arrived? y/n: "))

    if home == "n":
        print("keep waiting")
        current_time += datetime.timedelta(minutes=10)
    elif home == "y":
        print("Get into the car")
        break
    else:
        print("invalid response")

print(current_time.strftime("%H:%M:%S"), end='\r')

while True:
    arrived = str.lower(input("Have we arived home? y/n: "))

    if arrived == "n":
        print("Wait")
        current_time += datetime.timedelta(minutes=15)
    elif arrived == "y":
        print("Get out of car")
        print ("Go inside")
        current_time += datetime.timedelta(minutes=3)
        break
    else:
        print("invalid response")

print(current_time.strftime("%H:%M:%S"), end='\r')

while True:
    homework = str.lower(input("Do I have homework remaining? y/n: "))

    if homework == "n":
        print("Do whatever I want")
        current_time += datetime.timedelta(minutes=30)
        break
    elif homework == "y":
        print("work on homework")
        current_time += datetime.timedelta(minutes=30)
    else:
        print("invalid response")

print(current_time.strftime("%H:%M:%S"), end='\r')

while True:
    walk = str.lower(input("Is it a nice day outside and do I have energy left? y/n: "))

    if walk == "n":
        print("Keep doing whatever I want inside")
        current_time += datetime.timedelta(minutes=30)
        break
    elif walk == "y":
        print("Go on a walk outside")
        print ("Return home after an hour")
        current_time += datetime.timedelta(minutes=60)
        break
    else:
        print("invalid response")

print(current_time.strftime("%H:%M:%S"), end='\r')

while True:
    dinner= str.lower(input("Is dinner ready? y/n: "))

    if dinner == "n":
        print("Keep doing whatever I want inside")
        current_time += datetime.timedelta(minutes=20)
    elif dinner == "y":
        print("Go and eat dinner")
        break
    else:
        print("invalid response")

print(current_time.strftime("%H:%M:%S"), end='\r')

while True:
    dinner= str.lower(input("What do I want to have? sandwich/steak/soup/chicken/rice: "))

    if dinner == "sandwich":
        moredinner = str.lower(input("Do I want anything else? y/n: "))
        if moredinner == "n":
                current_time += datetime.timedelta(minutes=8)
                break

    elif dinner == "steak":
        moredinner = str.lower(input("Do I want anything else? y/n: "))
        if moredinner == "n":
                current_time += datetime.timedelta(minutes=8)
                break
        
    elif dinner == "soup":
        moredinner = str.lower(input("Do I want anything else? y/n: "))
        if moredinner == "n":
                current_time += datetime.timedelta(minutes=8)
                break
       
    elif dinner == "chicken":
        moredinner = str.lower(input("Do I want anything else? y/n: "))
        if moredinner == "n":
                current_time += datetime.timedelta(minutes=8)
                break
    elif dinner == "rice":
        moredinner = str.lower(input("Do I want anything else? y/n: "))
        if moredinner == "n":
                current_time += datetime.timedelta(minutes=8)
                break
    else:
        print("invalid response")

print(current_time.strftime("%H:%M:%S"), end='\r')

while True:
    finished = str.lower(input("Have I finished my food? y/n: "))

    if finished == "n":
        print("Continue eating")
        current_time += datetime.timedelta(minutes=30)
    elif finished == "y":
        break
    else:
        print("invalid response")

print(current_time.strftime("%H:%M:%S"), end='\r')

while True:
    sleep = str.lower(input("Do I have anything left that I want or need to do? y/n: "))

    if sleep == "n":
        print("Go to sleep")
        break
    elif sleep == "y":
        print("Do any remaining tasks")
        current_time += datetime.timedelta(minutes=60)
    else:
        print("invalid response")

print(current_time.strftime("%H:%M:%S"), end='\r')


    

            
        





