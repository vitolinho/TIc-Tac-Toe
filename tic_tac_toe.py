def tic_tac_toe():
    # plateau de jeu
    tray = [
            ["_","_","_"],
            ["_","_","_"],
            ["_","_","_"],
    ]
    
    # permet d'afficher le plateau de jeu
    i = 0
    while i < len(tray):
        print(tray[i])
        i = i + 1
    
    # fonction qui fait jouer les joueurs
    def play(signe):
        X = int(input("Donnez moi les coordonnées(0 étant tout en haut et 2 étant tout en bas) : "))
        while X < 0 or X > 2:
            print("Valeurs incorrectes")
            X = int(input("Donnez moi les coordonnées(0 étant tout en bas et 2 étant tout en bas) : "))
        
        Y = int(input("Donnez moi les coordonnées(0 étant tout à gauche et 2 étant tout à droite) : "))
        while Y < 0 or Y > 2:
            print("Valeurs incorrectes")
            Y = int(input("Donnez moi les coordonnées(0 étant tout à gauche et 2 étant tout à droite) : "))




        while tray[X][Y] != "_":
            print("Oh, il y a deja quelqu'un ici ...")
            i = 0
            # permet d'afficher le plateau de jeu
            while i < len(tray):
                print(tray[i])
                i = i + 1
            
            print("Ces petits tricheurs de",signe,"doivent rejouer")
            X = int(input("Donnez moi les coordonnées(0 étant tout en bas et 2 étant tout en bas) : "))
            Y = int(input("Donnez moi les coordonnéess(0 étant tout à gauche et 2 étant tout à droite) : "))
            
        
        else:
            tray[X][Y] = signe
        
        i = 0
        while i < len(tray):
            print(tray[i])
            i = i + 1
    
    # fonction chargé de trouver les combinaisons gagnantes
    def Search_combi_win(Liste,signe):
        if Liste[0][0] == signe and Liste[0][1] == signe and Liste[0][2] == signe:
            return True
        elif Liste[1][0] == signe and Liste[1][1] == signe and Liste[1][2] == signe:
            return True
        elif Liste[2][0] == signe and Liste[2][1] == signe and Liste[2][2] == signe:
            return True
        elif Liste[0][0] == signe and Liste[1][0] == signe and Liste[2][0] == signe:
            return True
        elif Liste[0][1] == signe and Liste[1][1] == signe and Liste[2][1] == signe:
            return True
        elif Liste[0][2] == signe and Liste[1][2] == signe and Liste[2][2] == signe:
            return True
        elif Liste[0][0] == signe and Liste[1][1] == signe and Liste[2][2] == signe:
            return True
        elif Liste[0][2] == signe and Liste[1][1] == signe and Liste[2][0] == signe:
            return True
        return False

    nb_essay = 0
    while nb_essay < 9 and Search_combi_win(tray,"X") == False and Search_combi_win(tray,"O") == False:
        if nb_essay % 2== 0:
            print("C'EST AU TOUR DES X.")
            play("X")
            
        else:
            print("C'EST AU TOUR DES O.")
            play("O")
        nb_essay = nb_essay + 1
    if Search_combi_win(tray,"X") == True:
        print("LES X ONT GAGNÉS !")
    elif Search_combi_win(tray,"O") == True:
        print("LES O ONT GAGNÉS !")
    else:
        print("ÉGALITÉ !!")

# Menu du jeu
def menu():
    print("""

████████ ██  ██████     ████████  █████   ██████     ████████  ██████  ███████ 
   ██    ██ ██             ██    ██   ██ ██             ██    ██    ██ ██      
   ██    ██ ██             ██    ███████ ██             ██    ██    ██ █████   
   ██    ██ ██             ██    ██   ██ ██             ██    ██    ██ ██      
   ██    ██  ██████        ██    ██   ██  ██████        ██     ██████  ███████ 
                                                                               
                                                                               

    """)
    print("""
    1 - Lancer la partie
    2 - Crédits
    3 - Quitter le jeu
    """)
    menu_choice = input("Entrez la valeur 1, 2 ou 3: ")
    if menu_choice == "1" :
        tic_tac_toe()

    elif menu_choice == "2":
        print("Ce jeu a été coder par Vitomir LACES.")
        input("tapez sur entrez pour revoir le menu")
        menu()

    elif menu_choice == "3" :
        print("Vous avez quittez le jeu")
        print("Au revoir ")
        return

menu()