n = 'Y'

while n == 'Y':

    playerChoice1 = ''
    playerChoice2 = ''
    listOfChoice = ('Rock', 'Paper', 'Scissors')

    print(' Please enter one of the values: Rock, Paper, Scissors')

    while True:
        playerChoice1 = (input('Player 1, please enter a choice: '))
        if playerChoice1 in listOfChoice: break
        else: 
            print('Please enter a value between Rock, Paper and Scissors') 

    while True:
        playerChoice2 = (input('Player 2, please enter a choice: '))
        if playerChoice2 in listOfChoice: break
        else: 
            print('Please enter a valid choice') 

    def chooseWinner(choice1, choice2):
        if choice1 == choice2:
            return 'It is a Draw.'
        elif choice1 == 'Rock' and choice2 == 'Scissors':
            return 'Congratulations player 1.'
        elif choice1 == 'Scissors' and choice2 == 'Paper':
            return 'Congratulations player 1.'
        elif choice1 == 'Paper' and choice2 == 'Rock':
            return 'Congratulations player 1.'
        else: return 'Congratulations player 2.'

    print(chooseWinner(playerChoice1, playerChoice2))

    while True:
        n = (input('Would you like to start another game? [Y/N]: '))
        if n in ('Y', 'N'): break
        else: 
            print('Please enter a valid choice between [Y/N]')