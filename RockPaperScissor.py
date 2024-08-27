import random
userChoice = input("Choices : Rock, Paper, Scissor \nPick any one :")
def RandomChoice():
    randomNumber = random.random()
    if(randomNumber < 0.333333):
        print("Computer Choice : Rock")
        return "Rock"
    elif(randomNumber > 0.333333 and randomNumber < 0.666666):
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
    else:
        print("Check All cases in code :")
VsComputer(userChoice)