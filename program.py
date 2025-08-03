
# calculating odd days for centuries.
def calculate_year_odd_days(c_year):
    
    remainder_years = c_year % 100

    century_part = c_year - remainder_years

    centurey_rem = century_part % 400

    if centurey_rem == 100:
        century_odd_days = 5

    elif centurey_rem == 200:
        century_odd_days = 3

    elif centurey_rem == 300:
        century_odd_days = 1
    
    else: 
        century_odd_days = 0

    print(f"Century odd days: {century_odd_days}") 

    



# input method defined
def get_day_of_week():
    
    year = int(input("Enter Year:"))
    month = int(input("Enter Month:"))
    day = int(input("Enter Day:"))

    completed_year =  year - 1

    # Passing the completed_year to the calculate_year_odd_days() function.
    odd_days_for_years = calculate_year_odd_days(completed_year)


# main execution
get_day_of_week()

