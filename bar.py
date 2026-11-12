weekday =["monday", "tuesday", "wednesday", "thursday", "friday"]
weekend = ["saturday", "sunday"]

str_people_inside = input("How many people are inside? ")
people_inside = int(str_people_inside)
venue_max = 300

if people_inside < venue_max:
    day=input("What day is it?: ")
    if day in weekday:
        age_limit = 21
    else:
        age_limit = 18
    id_validation = input("Do you have a valid ID?: ") .lower()
    if id_validation == "no":
        print("You're not welcome")
    else:
        str_age_check = input("How old is the person? ")
        age = int(str_age_check)
        if age > age_limit:
            print("You're welcome, have a good night!")
        else:
            print("You're not old enough, please leave.")
else:
    print("The venue is full, come back another day or later!")





