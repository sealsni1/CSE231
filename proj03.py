# import math
NUMBER_OF_PAYMENTS = 360    # 30-year fixed rate mortgage, 30 years * 12 monthly payments
SEATTLE_PROPERTY_TAX_RATE = 0.0092
SAN_FRANCISCO_PROPERTY_TAX_RATE = 0.0074
AUSTIN_PROPERTY_TAX_RATE = 0.0181
EAST_LANSING_PROPERTY_TAX_RATE = 0.0162
AVERAGE_NATIONAL_PROPERTY_TAX_RATE = 0.011
SEATTLE_PRICE_PER_SQ_FOOT = 499.0
SAN_FRANCISCO_PRICE_PER_SQ_FOOT = 1000.0
AUSTIN_PRICE_PER_SQ_FOOT = 349.0
EAST_LANSING_PRICE_PER_SQ_FOOT = 170.0
AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT = 244.0
APR_2023 = 0.0668

# ''' WRITE YOUR CODE USING THE CONSTANT VALUES and THE STRINGS ABOVE '''
keep_going_text = 'y'
monthly_payment_schedule = ''

while keep_going_text == 'y':
    # Header for starting code
    print('\nMORTGAGE PLANNING CALCULATOR\n============================ ')
    print('\nEnter a value for each of the following items or type \'NA\' if unknown')

    # Ask user for a known location
    user_location = input('\nWhere is the house you are considering' '(Seattle, San Francisco, Austin, East Lansing)?')
    user_location = user_location[0].upper() + user_location[1:]

    # Assign variables for calculations and set them to zero
    apr = 0
    home_cost = 0
    max_payment = False
    monthly_taxes = 0
    monthly_payment = 0
    monthly_interest_rate = 0
    mortgage_payment = 0
    payment_to_loan = 0
    payment_to_interest = 0
    property_tax_rate = 0
    price_per_sq_foot = 0
    principle_loan_amount = 0
    remaining_loan_amount = 0
    total_payment = 0
    unknown = False
    square_feet = False
    square_feet_calculation = 0
    month = 'Month'
    interest = 'Interest'
    payment = 'Payment'
    balance = 'Balance'

    # Check to see if the Location is known
    if user_location in ['Seattle', 'San Francisco', 'Austin', 'East Lansing']:

        # Set property tax rate and price per square foot based on location
        if user_location == 'Seattle':
            property_tax_rate = SEATTLE_PROPERTY_TAX_RATE
            price_per_sq_foot = SEATTLE_PRICE_PER_SQ_FOOT

        elif user_location == 'San Francisco':
            property_tax_rate = SAN_FRANCISCO_PROPERTY_TAX_RATE
            price_per_sq_foot = SAN_FRANCISCO_PRICE_PER_SQ_FOOT

        elif user_location == 'Austin':
            property_tax_rate = AUSTIN_PROPERTY_TAX_RATE
            price_per_sq_foot = AUSTIN_PRICE_PER_SQ_FOOT

        elif user_location == 'East Lansing':
            property_tax_rate = EAST_LANSING_PROPERTY_TAX_RATE
            price_per_sq_foot = EAST_LANSING_PRICE_PER_SQ_FOOT

    else:
        # Location is not known, use national average values
        unknown = True
        property_tax_rate = AVERAGE_NATIONAL_PROPERTY_TAX_RATE
        price_per_sq_foot = AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT

    # Ask user for MAX Square Footage and MAX Monthly Payment
    user_square_footage = input('\nWhat is the maximum square footage you are considering? ')
    user_max_monthly_payment = input('\nWhat is the maximum monthly payment you can afford? ')

    # If the MAX monthly payment does NOT equal 'NA' calculate ...
    if user_max_monthly_payment != 'NA':
        user_max_monthly_payment = float(user_max_monthly_payment)
        max_payment = True

    elif user_max_monthly_payment == 'NA':
        max_payment = False

    # Check to see if user input a maximum square footage for house
    if user_square_footage == 'NA':
        square_feet = True
        max_payment = False

    # If Square footage does NOT equal 'NA' calculate the Home cost
    elif user_square_footage != 'NA':
        user_square_footage = float(user_square_footage)
        home_cost = user_square_footage * price_per_sq_foot

    else:
        # If user does NOT provide a Sq Footage or Monthly payment ask them to try again
        print('\nYou must either supply a desired square footage or a maximum monthly payment. Please try again.')
        keep_going_text = input('\nWould you like to make another attempt (Y or N)? ')
        keep_going_text = keep_going_text.lower()
        continue

    # Ask user for a down payment and current APR
    user_down_payment = input('\nHow much money can you put down as a down payment? ')
    user_apr = input('\nWhat is the current annual percentage rate? ')

    # Find out if user provided a down payment amount
    if user_down_payment != 'NA':
        user_down_payment = float(user_down_payment)

    else:
        # Set the down payment to zero if user doe not provide one
        user_down_payment = 0

    # Find out if user provided an Annual Percentage Rate
    if user_apr != 'NA':
        user_apr = float(user_apr)

    else:
        # If user did not provide APR set the APR to the national average
        user_apr = APR_2023 * 100

    # If user did not provide location execute Unknown statement
    if unknown is True:
        print('\nUnknown location. Using national averages for price per square foot and tax rate.')
        user_location = 'the average U.S. housing market'

    # Print the output for the mortgage calculator to the user if square footage was included
    if square_feet is True:
        user_square_footage = 100
        monthly_interest_rate = (user_apr / 100) / 12
        while True:
            home_cost = user_square_footage * price_per_sq_foot
            principle_loan_amount = home_cost - user_down_payment
            monthly_payment = (principle_loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -NUMBER_OF_PAYMENTS)

            monthly_taxes = (property_tax_rate / 12) * home_cost
            mortgage_payment = monthly_payment + monthly_taxes

            if mortgage_payment > user_max_monthly_payment:
                # Calculations
                user_square_footage -= 1
                home_cost = user_square_footage * price_per_sq_foot
                break
            else:
                user_square_footage += 1

        # Print statements
        print(f'\n\nIn {user_location}, a maximum monthly payment of ${user_max_monthly_payment:,.2f} allows the purchase of a house of {user_square_footage:,.0f} sq. feet for ${home_cost:,.0f}')
        print(f'\t assuming a 30-year fixed rate mortgage with a ${user_down_payment:,.0f} down payment at {user_apr:,.1f}% APR.')

    elif square_feet is False:
        # Calculations
        principle_loan_amount = home_cost - user_down_payment  # Correct
        monthly_taxes = (property_tax_rate / 12) * home_cost  # Correct
        monthly_interest_rate = user_apr / 12 / 100  # Correct
        monthly_payment = (principle_loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -NUMBER_OF_PAYMENTS)
        mortgage_payment = monthly_taxes + monthly_payment
        user_square_footage = int(user_square_footage)

        # Print statements
        print(f'\n\nIn {user_location}, an average {user_square_footage:,} sq. foot house would cost ${home_cost:,.0f}.')
        print(f'A 30-year fixed rate mortgage with a down payment of ${user_down_payment:,.0f} at {user_apr:,.1f}% APR results')
        print(f'\tin an expected monthly payment of ${monthly_taxes:,.2f} (taxes) + ${monthly_payment:,.2f} (mortgage payment) = ${mortgage_payment:,.2f}')

    # If user provided a max monthly payment, decide if the user can afford the payment
    if max_payment is True:
        user_max_monthly_payment = int(user_max_monthly_payment)
        if mortgage_payment > user_max_monthly_payment:
            print(f'Based on your maximum monthly payment of ${user_max_monthly_payment:,.2f} you cannot afford this house.')

        elif mortgage_payment <= user_max_monthly_payment:
            print(f'Based on your maximum monthly payment of ${user_max_monthly_payment:,.2f} you can afford this house.')

        # Ask the user if they would like to print the monthly payment schedule

    if square_feet is False:
        monthly_payment_schedule = input('\nWould you like to print the monthly payment schedule (Y or N)? ')
        monthly_payment_schedule = monthly_payment_schedule.lower()

    # Set remaining loan amount to the cost of the Principle
    remaining_loan_amount = principle_loan_amount

    # If user want's monthly schedule print the schedule out
    if monthly_payment_schedule == 'y':
        # Print header for monthly schedule
        print(f'\n{month:^7}|{interest:^12}|{payment:^13}|{balance:^14}')
        print('================================================')

        # For loop to iterate through the monthly payments
        for i in range(1, NUMBER_OF_PAYMENTS + 1):
            payment_to_interest = (remaining_loan_amount * (user_apr / 100)) / 12
            payment_to_loan = monthly_payment - payment_to_interest

            # Execute print statement
            print(f'{i:^7}| ${payment_to_interest:>9,.2f} | ${payment_to_loan:>10,.2f} | ${remaining_loan_amount:>11,.2f}') # Align these to the right

            # Calculations for Monthly Payment Schedule
            remaining_loan_amount = remaining_loan_amount - payment_to_loan

    # Ask user if they would like another attempt
    keep_going_text = input('\nWould you like to make another attempt (Y or N)? ')
    keep_going_text = keep_going_text.lower()
    continue
