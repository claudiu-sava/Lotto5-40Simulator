import random
from tkinter import *

main = Tk()

main.geometry("500x500")
main.resizable(0, 0)
nameLabel = Label(text="Lotto 5/40")
nameLabel.grid(column=0, row=1, sticky=E)

firstNr = None
secondNr = None
thirdNr = None
fourthNr = None
fifthNr = None

choice1, choice2, choice3, choice4, choice5 = None, None, None, None, None

numbersGuessed = 0

def checkDuplicates():
  if firstNr == secondNr == thirdNr == fourthNr == fifthNr:
    generateNumbers()

def generateNumbers():
  global firstNr, secondNr, thirdNr, fourthNr, fifthNr
  firstNr = random.randint(1, 40)
  secondNr = random.randint(1, 40)
  thirdNr = random.randint(1, 40)
  fourthNr = random.randint(1, 40)
  fifthNr = random.randint(1, 40)
  checkDuplicates()

def checkUserInput():
  numbers = [choice1, choice2, choice3, choice4, choice5]
  if len(numbers) != len(set(numbers)):
    print("You have entered duplicate numbers. Please enter the numbers again")
    userInput()
  elif choice1 > 40 or choice2 > 40 or choice3 > 40 or choice4 > 40 or choice5 > 40:
    print("Your numbers must be between 1 and 40. Please enter the numbers again")
    userInput()

def userInput():
  global choice1, choice2, choice3, choice4, choice5
  print("Enter the first number: ")
  choice1 = int(input())
  print("Enter the second number: ")
  choice2 = int(input())
  print("Enter the third number: ")
  choice3 = int(input())
  print("Enter the fourth number: ")
  choice4 = int(input())
  print("Enter the fifth number: ")
  choice5 = int(input())
  checkUserInput()

def checkNumbers():
  global numbersGuessed, firstNr, secondNr, thirdNr, fourthNr, fifthNr, choice1, choice2, choice3, choice4, choice5

  if choice1 == firstNr or choice1 == secondNr or choice1 == thirdNr or choice1 == fourthNr or choice1 == fifthNr:
    numbersGuessed = numbersGuessed + 1
  if choice2 == firstNr or choice2 == secondNr or choice2 == thirdNr or choice2 == fourthNr or choice2 == fifthNr:
    numbersGuessed = numbersGuessed + 1
  if choice3 == firstNr or choice3 == secondNr or choice3 == thirdNr or choice3 == fourthNr or choice3 == fifthNr:
    numbersGuessed = numbersGuessed + 1
  if choice4 == firstNr or choice4 == secondNr or choice4 == thirdNr or choice4 == fourthNr or choice4 == fifthNr:
    numbersGuessed = numbersGuessed + 1
  if choice5 == firstNr or choice5 == secondNr or choice5 == thirdNr or choice5 == fourthNr or choice5 == fifthNr:
    numbersGuessed = numbersGuessed + 1
  if numbersGuessed >= 3:
    print("You win! You guessed " + str(numbersGuessed) + " numbers out of 6 numbers!")
  else:
    print("You lost... You guessed " + str(numbersGuessed) + " numbers out of 6 numbers! Better luck next time!")
  print("The winning numbers are: " + str(firstNr) + ", " + str(secondNr) + ", " + str(thirdNr) + ", " + str(fourthNr) + ", " + str(fifthNr))
  print("Your numbers are: " + str(choice1) + ", " + str(choice2) + ", " + str(choice3) + ", " + str(choice4) + ", " + str(choice5))

generateNumbers()



userInput()
checkNumbers()
main.mainloop()
