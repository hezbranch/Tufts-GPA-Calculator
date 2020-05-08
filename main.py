# Tufts GPA Calculator
# Use this program to calcuate your Tufts GPA
# Author: Hezekiah Branch
# Cognitive Brain Science, CS & EM Minor 
# Class of 2021
# Tufts University
# Spring 2020
# May 08, 2020

import sys

print("Welcome to the Tufts GPA calculator! \n")
print("WARNING: P/F does not factor into GPA and as such \nwill not be counted during this program.")

# Pulled from the Tufts Bulletin
# Visit http://students.tufts.edu/sites/default/files/2019-20_Bulletin.pdf
# for more information
standard = {"A+": 4.0, "A": 4.0, "A-": 3.667,
"B+": 3.333, "B": 3.0, "B-": 2.667,
"C+": 2.333, "C": 2.0, "C-": 1.667, 
"D+": 1.333, "D": 1.0, "D-": 0.667,
"F": 0}

# Store an empty dictionary to hold values of user-inputted courses
courses = {}

def get_input():
  answer = input("Would you like to calculate your GPA?  ").lower().strip()
  if (answer == "yes"):
    return answer
  else:
    sys.exit("GPA not calculated. User has ended Tufts GPA calculator.")

# Get course values
def add_class(answer):
  # Get input on course information from user
  course = input("What class are you adding? ")
  letter_grade = input("What was the letter grade (A+, A, A-, etc.)? ")
  credit_value = input("How many credits? ")
  # Add course name letter grade to courses if valid
  if letter_grade in standard.keys():
    courses[course] = [letter_grade, credit_value]
  else:
    # Validate user input for grade and send error message
    choice = input("Not a grade option. Would you like to try again? ")
    if (choice.lower().strip() == "yes"):
      add_class(answer)

# Add classes to the courses dictionary
def class_registration(first_time):
  print("")
  # Add an empty line for loading screen
  if (first_time == True):
    answer = get_input()
    print("\n---------------------------------------\n")
    print("--------------LOADING------------------\n")
    print("---------------------------------------\n")
    add_class(answer)
    # Store that we have finished our first go around
    first_time = False
    class_registration(first_time)
  elif (first_time == False):
    answer = input("Would you like to add another class? ")
    while (answer.lower().strip() == "yes"):
      add_class(answer)
      print(" ")
      answer = input("Would you like to add another class? ")
  # End the recursion for adding courses
  else:
    print("\nAll classes added!")

def calculate_gpa(courses):
  numerator = 0
  denominator = 0
  for course, grade in courses.items():
    numerator += standard.get(grade[0]) * float(grade[1])
    denominator += float(grade[1])
  gpa = numerator / denominator
  return gpa

# Begin class_registration
first_time = True
class_registration(first_time) 
gpa = calculate_gpa(courses)

# Display course and attached grades to user
for course, grade in courses.items():
  print("\nCourse: ", course, " Grade: ", grade[0], " Credits: ", grade[1])
  print("")

print("\n---------------------------------------\n")
print("--------------LOADING------------------\n")
print("---------------------------------------\n")

# Display GPA rounded to 2 decimals as per Tufts Bulletin regulation
print("\nCalculated GPA: ", round(gpa, 2))
print("Dean's List requirements for A&S: 3.4 Semester GPA and 12 graded SHUs")
print("Dean's List requirements for SoE: 3.2 Semester GPA and 9 graded SHUs and 12 SHUs attempted")

print("\nProgram written by Hezekiah Branch A21")

# Next Steps
# Create a save state for the program
# Allow user to read in files
# Open files
# Edit courses already inputted