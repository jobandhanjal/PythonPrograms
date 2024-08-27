import random
userChoice = input("Choices : Rock, Paper, Scissor \nYour Choice :")
def RandomChoice():
    randomNumber = random.randint(0,2)
    if(randomNumber == 0):
        print("Computer Choice : Rock")
        return "Rock"
    elif(randomNumber == 1):
        print("Computer Choice : Paper")
        return "Paper"
    else:
        print("Computer Choice : Scissor")
        return "Scissor"
def VsComputer(userChoice) :
    ComputerChoice = RandomChoice()
    if((ComputerChoice == 'Rock' and userChoice == 'Rock') or 
       (ComputerChoice == 'Paper' and userChoice == 'Paper') or 
       (ComputerChoice == 'Scissor' and userChoice == 'Scissor')):
        print("Match Tie :")
    elif(ComputerChoice == 'Rock' and userChoice == 'Paper'):
        print("You are winner : Paper")
    elif(ComputerChoice == 'Rock' and userChoice == 'Scissor'):
        print("Computer is Winner : Rock")
    
    elif(ComputerChoice == 'Paper' and userChoice == 'Rock'):
        print("You are winner : Rock")
    elif(ComputerChoice == 'Paper' and userChoice == 'Scissor'):
        print("Computer is Winner : Paper")

    elif(ComputerChoice == 'Scissor' and userChoice == 'Paper'):
        print("Computer is Winner : Scissor")
    elif(ComputerChoice == 'Scissor' and userChoice == 'Rock'):
        print("You are Winner : Rock")
VsComputer(userChoice)