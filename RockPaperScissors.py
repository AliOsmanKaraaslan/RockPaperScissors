import random
def GetChoices():
    playerChoice = input("Enter a choice (Rock, Paper, Scissors)")
    options = ["Rock", "Paper", "Scissors"]
    computerChoice = random.choice(options)
    # Dizideki 3 string değerden 1 ini seçiyor
    choices = {"Player" : playerChoice, "Computer" : computerChoice}
    # Dictionary Tanımlanıyor 
    # Dictionary anahtar ve değer içerir 
    return choices

def CheckWin(player, computer): 
    print(f"You chose {player}, computer chose {computer}")
    # Üsttekinin en yorum satırının en altındaki print ile farkı
    #
    # Başında f olmasına dikkat et çünkü bu bir f-string (formatlı String)
    # Daha okunabilir ve temiz bir kod sağlar.
    # Değişken adlarını veya ifadelerini yazarken daha az hata yapma olasılığına sahiptir.
    # Diğer string biçimleme yöntemlerine göre genellikle daha hızlıdır.
    #
    #
    #print("YOU CHOSE : " + player + " COMPUTER CHOSE : " + computer)
    if player == computer:
        return "It's a tie!"
    elif player == "Rock":
        if computer == "Scissors":
            return "Rock smashes scissors! You Win!"
        else : 
            return "Paper covers rock! You Lose!"
        
    elif player == "Paper":
        if computer == "Rock":  
            return "Paper covers rock! You Win!"
        else:
            return "Scissors cuts paper! You Lose!"
        
    elif player == "Scissors":
        if computer == "Rock":
            return "Rock smashes scissors! You Lose!"
        else:
            return "Scissors cuts paper! You Win!"
        
option = "1"
while(option == "1"):
    inputNumber = "True"
    choices = GetChoices()
    result = CheckWin(choices["Player"], choices["Computer"])
    print(result)
    while(inputNumber == "True"):
        option = input("press 0 for end the game\npress 1 for continue the game")
        if option != "1" and option != "0" :
            print("Your Click Wrong Number. Try Again")
        elif option == "1" or option == "0":
            break