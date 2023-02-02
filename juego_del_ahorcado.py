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

def read_title():
    try:
        with open("./home/Titulo.txt","r",encoding="utf-8") as f:
            for ascii_art in f:
                print(ascii_art)
    except OSError:
        print("No se encontró el archivo title.txt")

def life(life_score):
    try:
        if life_score == 5:
            with open("./frames/ahorcado-1.txt","r",encoding="utf-8")as f:
                for hangman in f:
                    print(hangman)
        elif life_score == 4:
            with open("./frames/ahorcado-2.txt","r",encoding="utf-8")as f:
                for hangman in f:
                    print(hangman)
        elif life_score == 3:
            with open("./frames/ahorcado-3.txt","r",encoding="utf-8")as f:
                for hangman in f:
                    print(hangman)
        elif life_score == 2:
            with open("./frames/ahorcado-4.txt","r",encoding="utf-8")as f:
                for hangman in f:
                    print(hangman)
        elif life_score == 1:
            with open("./frames/ahorcado-5.txt","r",encoding="utf-8")as f:
                for hangman in f:
                    print(hangman)
        elif life_score == 0:
            with open("./frames/ahorcado-6.txt","r",encoding="utf-8")as f:
                for hangman in f:
                    print(hangman)
    except OSError:
        print("No se encuentran los archivos en la carpeta frame")

def run():
    read_title()
    os.system("Pause")
    words_create()
    choose = random.randint(1,6)
    palabra = read_words(choose)

    list_guess = [" _ " for i in range(1, len(palabra))]
    ban = True
    y = 0
    z = 0
    life_score = 5
    os.system("clear")
    life(life_score) 
    print(''.join(list_guess))  

    while ban == True:
        error_input = False
        conval = False  
        w = input("Introduce una letra: ")
        w = w.upper()
        
        error_input_lambda = lambda string: string.isnumeric() or len(string) == 0 or len(w) > 1
        error_input = error_input_lambda(w)
        fun_conval = lambda string: string in palabra
        conval = fun_conval(w)

        if conval == False:
            life_score = life_score - 1 

        if error_input == True:
            print("El juego no acepta cadenas vacias, ni frases, ni numeros. Vuelva a intentarlo.")
        else:
            i = 0
            
            os.system("clear") 
            clear = lambda string: string in list_guess
            clear = not(clear(w))

            if clear == True:
                for letra in palabra:
                    if w == letra:
                        list_guess[i] = w
                        y = y + 1
                    i = i + 1 
                if y == len(list_guess):
                    print("GANASTE EL JUEGO DEL AHORCADO, LA PALABRA FUE: ") 
                    ban = False
                       
            else:
                print(f"La letra {w} ya fue utilizada, intente otra letra")
                life_score = life_score - 1 
            
            life(life_score) 
            print("\n",''.join(list_guess))

            if life_score == 0:
                ban = False
                os.system("cls")
                life(life_score)
                print(f"Perdiste, has fallado 5 intentos T.T, la palabra era: {palabra}")

if __name__ == '__main__':
    run()
