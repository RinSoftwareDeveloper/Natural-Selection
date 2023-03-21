# Import Packages
import random
import os
import json

# These settings you can modify to change how this simulation runs.
subject_count = 10
simulation_years = 100

# Create Test-Subject
class testsubject_class():
    def __init__(self, id, charstr):
        self.id = id
        self.charstr = charstr
    def returnstr(self):
        return (f"no{(self.id)}/{self.charstr}")

# Generate Properties
def char_generate():
    local_age = random.randint(1,100) # ref age factor which determines survivability (0 is best)
    local_gender = random.randint(0,1) # 0M 1F
    local_attractivelvl = random.randint(0,8) # determines reproduction level
    local_strength = random.randint(0,8) # ref strength factor which determines survivability (0 is best) 
    local_eyesight = random.randint(0,8) # ref eyesight factor which determines survivablity (0 is best)
    local_intuition = random.randint(0,8) # ref intuition factor which determines survivability (0 is best)
    local_survivability = (100 - (local_age + (local_strength + local_eyesight + local_intuition))) # creates a number for est. death

    local_charstr = "" # Clear
    local_charstr = f"{local_age}~{local_gender}~{local_attractivelvl}~{local_strength}~{local_eyesight}~{local_intuition}~{local_survivability}"
    print(local_charstr)
    return local_charstr

# Create all the test subjects.
testsubjects = []
for subjectcounter in range(0, subject_count):    
    testsubjects.append(testsubject_class(subjectcounter, char_generate()).returnstr())


# Create Simulation
for cur_year in range(simulation_years):
    reader_testsubjects = [] # This is debug to split the subject for reader. We include it in the loop to reset the reader everytime.
    for subjectlen in range(len(testsubjects)):
        reader_testsubjects.append(testsubjects[subjectlen].split("/"))

    reader_attributes = [] # This attribute reader reads the attributes.
    for attributelen in range(len(reader_testsubjects)): 
        reader_attributes.append((reader_testsubjects[attributelen][1]).split("~"))
    
    # This section should change the age attribute everytime the year as passed, worked in test, not vertical integration
    for b in range(len(reader_attributes)):
        reader_attributes[b][0] = str(int(reader_attributes[b][0]) + 1)
    print(reader_attributes[0][0])

    # Return the age of the first test subject everytime for testing purposes.
    print(f"Year: {cur_year}: {reader_attributes[0][0]}") 