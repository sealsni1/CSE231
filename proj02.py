import math

# Variables used in code
angle = 0
coin = 0
current_hp = 0
distance = 0
defacto_speed = 0
qpu = 0
speed = 0
pu_count = 0
mario_position = 0
user_input = '1'

PU_SIZE = 65535
ISLAND = 1000
Scuttlebug_Radius = 10

# Continuous Loop to execute code
while user_input != 'q':
    print("\nSelect one of the following options:")
    print("1: Speed calculator")
    print("2: Parallel Universe navigator")
    print("3: Scuttlebug transportation")
    print("q: Exit the program")

    user_input = input('Option: ')

    if user_input == '1':
        # Get input from user
        qpu = int(input("\nHow many QPUs do you want to travel? "))
        angle = float(input("\nWhat is the angle of the slope on which Mario is standing? "))

        # Calculate the speed
        speed = (PU_SIZE * 4 * qpu) / (math.cos(angle))
        print("\nMario needs", round(speed), "speed")
        qpu = 0
        angle = 0
        speed = 0

    elif user_input == '2':
        # Ask user for input
        angle = float(input("What is the angle of the slope on which Mario is standing? "))
        marios_speed = int(input("What is Mario's speed? \n"))

        # Calculate defacto speed and set variables to zero
        defacto_speed = (marios_speed * math.cos(angle))
        mario_position = 0
        pu_count = 0

        # Check for Quarter step eligibility
        for i in range(1, 5):
            if (0.25 * defacto_speed) == PU_SIZE or abs((0.25 * defacto_speed + mario_position) % PU_SIZE - PU_SIZE) < ISLAND:
                pu_count += (0.25 * defacto_speed) / PU_SIZE

                # Update Marios Position
                if (0.25 * defacto_speed) == PU_SIZE:
                    mario_position = 0
                else:
                    mario_position = ((0.25 * defacto_speed + mario_position) % PU_SIZE) - PU_SIZE

            # If quarter step was invalid
            else:
                print('Quarter step', i, 'is invalid!')
                break

        # Print returning values
        if pu_count < 2:
            print("\nMario has travelled", round(pu_count), "PU")
        else:
            print("\nMario has travelled", round(pu_count), "PUs")

        print('Mario\'s position in this PU:', round(mario_position))

    elif user_input == '3':
        # ask user for input
        current_hp = int(input("\nWhat is Mario's current HP? "))

        # Create while loop to set requirements for HP
        while current_hp not in range(1, 9):
            print("\nInvalid amount of HP!")
            current_hp = int(input("\nWhat is Mario's current HP? "))

        coin = int(input("\nAt what distance is the coin placed? Enter -1 if there is no coin. "))

        if coin != -1:
            distance = Scuttlebug_Radius * current_hp
            if coin < distance and coin % Scuttlebug_Radius == 0:
                current_hp += 1
                distance = Scuttlebug_Radius * current_hp

            print("\nThe Scuttlebug can be transported", distance, "units of distance")

        else:
            distance = Scuttlebug_Radius * current_hp
            print("\nThe Scuttlebug can be transported", distance, "units of distance")

    else:
        user_input = 'q'
