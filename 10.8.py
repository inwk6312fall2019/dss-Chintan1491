#prog 10.8
from random import randint

def date_generator(students):
    dates = []
    for s in range(students):
        dates.append(randint(1,366))
    return dates

# The Date Generator will generate the random number of dates using randint() function

def has_matches(dates):
    dates.sort()
    for i in range(len(dates) - 1):
        if dates[i] == dates[i+1]:
            return True
        return False

#The has_matches function will match the birthday days between two students having
# birthday at same date

def same_day_birthday(num_of_iteration, students):
    matches = 0
    for i in range(num_of_iteration):
        dates = date_generator(students)
        if has_matches(dates):
            matches += 1
    print(f'There are {matches} classes having student with the same birthday date in {num_of_iteration} chances')

same_day_birthday(500,23)
