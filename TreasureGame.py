import gameOptions

welcomeMessage = print('Welcome to Treasure Island.\nYour mission is simple,\nSURVIVE.\n')
playAgain = 'Y'
gameOptions.leftOrRight()

while playAgain != 'N':
    if input(gameOptions.leftOrRight()).upper() != 'LEFT':
        print(gameOptions.gameOver)
        break
        
    print(gameOptions.leftOption)

    if input(gameOptions.swimOrWait()).upper() != 'WAIT':
        print(gameOptions.gameOver)
        break

    if input(gameOptions.swimOrRunBack()).upper() != 'BACK':
        print(gameOptions.gameOver)
        break

    if input(gameOptions.redOrBlue()).upper() != 'YELLOW':
        print(gameOptions.gameOver)
        break
        
    print(gameOptions.youWin()).upper()
    playAgain = input('Play Again? (Y or N)').upper()
