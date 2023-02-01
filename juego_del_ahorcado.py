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
    try:
        with open("./words/words.txt", "r",encoding="utf-8") as f:
            for word in f:
                guess = word
                i = i + 1
                if i == num:
                    break
        return guess
    except OSError:
        print("No se puede abrir el archivo, compruebe la ubicación.")



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
        assert w.isnumeric() and len(w)> 1, "No se permite introducir cadenas vacías ni números. Intente otra vez."
        w = w.upper()

        i = 0
        os.system("clear") 

        clear = lambda string: string in list_guess
        clear = not(clear(w))

        if clear == True:
            for letra in palabra:
                if w == letra:
                    list_guess[i] = w
                    y = y + 1
                if y == len(list_guess):
                    ban = False
                i = i + 1
        else:
            print(f"La letra {w} ya fue utilizada, intente otra letra")
        print(''.join(list_guess))

    print("Ganaste, La Palabra es:",''.join(list_guess),"!!!!!")    

if __name__ == '__main__':
    run()
