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

def search(w,list_guess):
    for mapeo in list_guess:
        if w == mapeo:
            print("Ya introdujo la letra ",w," Intente con otra letra.")
            clear = False
            break
        else:
            clear = True
    return clear

def run():
    words_create()
    choose = random.randint(1,6)
    palabra = read_words(choose)

    list_guess = [" _ " for i in range(1, len(palabra))]
    ban = True
    y = 0
    print(''.join(list_guess))  

    while ban == True:  
        w = input("Introduce una letra: ")
        w = w.upper()
        i = 0
        os.system("clear") 

        clear = search(w,list_guess)

        if clear == True:
            for letra in palabra:
                if w == letra:
                    list_guess[i] = w
                    y = y + 1
                if y == len(list_guess):
                    ban = False
                i = i + 1
        print(''.join(list_guess))
  
    print("Ganaste, La Palabra es:",''.join(list_guess),"!!!!!")    

if __name__ == '__main__':
    run()
