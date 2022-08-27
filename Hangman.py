import random 
import os

def read_data(filepath="./palabras.txt"):
    words = []
    with open(filepath, 'r', encoding='utf8') as f:
        for line in f:
            words.append(line.strip().upper())
    return words

def run():
    data = read_data(filepath="./palabras.txt")
    chosen_word = random.choice(data)
    chosen_word_list = [letter for letter in chosen_word]
    chosen_word_list_underscores = ["_"] * len(chosen_word_list)
    letter_index_dict = {}
    for idx, letter in enumerate(chosen_word):
        if not letter_index_dict.get(letter):
            letter_index_dict[letter] = []
        letter_index_dict[letter].append(idx)

    while True:
        os.system("cls")
        print("""
        ___________.._______
        | .__________))______|
        | | / /      ||
        | |/ /       ||
        | | /        ||.-''./
        | |/         |/  _  \/
        | |          ||  `/,|
        | |          (\.`_.'
        | |         .-`--'.
        | |        /Y . . Y\.
        | |       // |   | \..
        | |      //  | . |  \..
        | |     ()   |   |   ()
        | |          ||'||
        | |          || ||
        | |          || ||
        | |          || ||
        | |         / | | \.
    -------------------------
    |  -------------------- |
    | |                   | |
    : :                   : :  
    -------------------------
""")

        for element in chosen_word_list_underscores:
            print(element + " ", end="")
        print("\n")

        try:
            letter = input("Ingresa una letra y presiona Enter: ").strip().upper()
            assert letter.isalpha(), input("SÓLO PUEDES INGRESAR LETRAS. Presiona la tecla Enter para continuar.")
            assert len(letter) == 1, input("SÓLO UNA LETRA POR FAVOR. Presiona la tecla Enter para continuar.")
        except AssertionError as e:
            print(e)
            continue

        if letter in chosen_word_list:
            for idx in letter_index_dict[letter]:
                chosen_word_list_underscores[idx] = letter

        if "_" not in chosen_word_list_underscores:
            os.system("cls")
            print("¡GANASTE! La palabra era", chosen_word)
            break

menu = """
    ___________.._______
    | .__________))______|
    | | / /      ||
    | |/ /       ||
    | | /        ||.-''./
    | |/         |/  _  \/
    | |          ||  `/,|
    | |          (\.`_.'
    | |         .-`--'.
    | |        /Y . . Y\.
    | |       // |   | \..
    | |      //  | . |  \..
    | |     ()   |   |   ()
    | |          ||'||
    | |          || ||
    | |          || ||
    | |          || ||
    | |         / | | \.
-------------------------
|  -------------------- |
| |                   | |
: :                   : :  
-------------------------
______________________________________________________________                       
|              BIENVENIDO AL JUEGO DEL AHORACADO              |
|-------------------------------------------------------------|
|        Para comenzar presiona (1) y luego (Enter)           |  
|        Para salir presiona (Ctrl + C) y luego Enter         |
|_____________________________________________________________|

"""
while True:
    try:
        opcion = input(menu)
        if int(opcion) == 1:
            run()
        else: input("Debes ingresar el número 1 para jugar. Presiona la tecla Enter para reintentar.")
        assert len(str(opcion)) == 1, input("No puedes ingresar varias letras o números!, Presiona la tecla Enter para reintentar.")
    except AssertionError as a:
        print(a)
    except ValueError:
        input("No se aceptan letras, ingresa el número 1 para jugar. Presiona la tecla Enter para reintentar.")

if __name__ == "__main__":
    run()