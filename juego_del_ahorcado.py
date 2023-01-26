import os
import random

def words_create():
    words_game = ["PANAMA","AGUACATE","AHORCADO","PYTHON","PROGRAMACION","CANAL"]
    with open("./words/words.txt", "w",encoding="utf-8") as f:
        for word in words_game:
            f.write(word)
            f.write("\n")

def read_words(num):
    i = 0
    with open("./words/words.txt", "r",encoding="utf-8") as f:
        for word in f:
            guess = word
            i = i + 1
            if i == num:
                break
    return guess

def run():
    words_create()
    #choose = random.randint(1,6)
    choose = 7
    palabra = read_words(choose)
    list_guess = [ ]
    
    for i in range(1, len(palabra)):
        list_guess.append(" _ ")

    x = len(list_guess)
    ban = True
    y = 0
    clear = True
    print(''.join(list_guess))  

    while ban == True:  
        w = input("Introduce una letra: ")
        w = w.upper()
        i = 0
        os.system("clear") 

        for mapeo in list_guess:
            if w == mapeo:
                print("Ya introdujo la letra ",w," Intente con otra letra.")
                clear = False
                break
            else:
                clear = True
        if clear == True:
            for letra in palabra:
                if w == letra:
                    list_guess[i] = w
                    y = y + 1
                if y == x:
                    ban = False
                i = i + 1
        print(''.join(list_guess))
  
    print("Ganaste, La Palabra es:",''.join(list_guess),"!!!!!")    

if __name__ == '__main__':
    run()