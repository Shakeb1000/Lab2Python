# Author: Shakeb Siddiqui sms8508@psu.edu
# Collaborator: Eric Byjoo ezb5481@psu.edu
# Section: 10
# Breakout: 1

def getLettergrade(grade):
  if (grade >= 93.0):
    return "A"
  elif (grade>= 90.0 ):
    return "A-"
  elif (grade>= 87.0):
    return "B+"
  elif (grade>= 83.0):
    return "B"
  elif (grade>= 80.0):
    return "B-"
  elif (grade>= 77.0):
    return "C+"
  elif (grade>= 70.0):
    return "C"
  elif (grade>= 60.0):
    return "D"
  else:
    return "F"

def run():
  grade = input("Enter your CMPSC 131 grade: ")
  grade = float(grade)
  print(f"Your letter grade for CMPSC 131 is {getLettergrade(grade)}.")

  if __name__ == "__main__":
    run