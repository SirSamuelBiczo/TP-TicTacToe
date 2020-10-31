#coding: utf-8

import random

HUMAIN = 'X'
ORDI = 'O'
VIDE = ' '
T_PLATEAU = 3

def init_plateau():
    """
    rien -> liste de liste
    
    Retourne un plateau de jeux vide
    """
    plateau = [] 
    for i in range(T_PLATEAU):
        plateau.append([' ', ' ', ' '])
    return plateau

def print_tableau(plateau):
    """
    liste de liste -> rien
    
    Affiche le plateau du jeux a l'écran 
    """
    
    for i in range(T_PLATEAU):
        print(plateau[i][0] + "|" + plateau[i][1] + "|" + plateau[i][2])
        
        if i == 0 or i == 1:
            print("-----")

def input_humain(plateau):
    """
    liste de liste -> tuple 
    
    Demande a l'utilisateur les indices ou le joueur doit jouer 
    """
    
    saisi_incorrect = True 
    
    while saisi_incorrect:
        saisi = input("Votre coup (\"q\" pour abandonner) : ").lower()
        saisi_list = saisi.split(" ")
        print(saisi_list)
        
        if saisi == "q":
            return False 
            
        if len(saisi_list) == 2 and len(saisi_list[0]) == 1 and len(saisi_list[1]) == 1 and ord(saisi_list[0]) >= ord("0") and ord(saisi_list[0]) <= ord(str(T_PLATEAU-1)) and ord(saisi_list[1]) >= ord("0") and ord(saisi_list[1]) <= ord(str(T_PLATEAU-1)):
            i = int(saisi_list[0])
            j = int(saisi_list[1])
            if plateau[i][j] == VIDE:
                return (i, j)
            else:
                print("Veuillez choisir une case vide ! ! !")
        else:
            print("Veuillez saisir un couple correcte !")

def coords_vides(plateau):
    """
    liste de liste -> liste de tuple
    
    Retourne une liste de tuple contenant coordonnées des cases vide du plateau 
    """
    coordonnee_vide = []
    
    for i in range(T_PLATEAU):
        for j in range(T_PLATEAU):
            if plateau[i][j] == VIDE:
                coordonnee_vide.append((i, j))
    return coordonnee_vide

def input_ordi(plateau):
    """
    liste de liste -> rien
    
    Retourne un tuple contenant le couple jouer par la machine 
    """
    coups_possible = coords_vides(plateau)
    
    return coups_possible[random.randint(0, len(coups_possible)-1)]

def est_victoire(symbole, plateau):
    """
    chaine de caractère, liste de liste -> booléan
    
    Retourne True si le symbole est aligner trois de suite sinon False 
    """
    ###########VERIFICATION EN LIGNE###################
    
     
    for i in range(T_PLATEAU):
        compte_alignement = 0
        for j in range(T_PLATEAU):
            if plateau[i][j] == symbole:
                compte_alignement += 1
        if compte_alignement == T_PLATEAU:
            return True
 
    ###########VERIFICATION EN COLONNE###################
 
    for j in range(T_PLATEAU):
        compte_alignement = 0
        for i in range(T_PLATEAU):
            if plateau[i][j] == symbole:
                compte_alignement += 1
        if compte_alignement == T_PLATEAU:
            return True
         
    
    ###########VERIFICATION EN DIAGONAL###################
 
    # haut gauche vers bas droite 
    if plateau[0][0] == symbole and plateau[1][1] == symbole and plateau[2][2] == symbole:
        return True
    if plateau[0][2] == symbole and plateau[1][1] == symbole and plateau[2][0] == symbole:
        return True
    return False

def joue_partie():
    """
    rien -> rien
    
    Lance une partie de morpion
    """
    
    plateau_de_jeu = init_plateau()
    print_tableau(plateau_de_jeu)
    
    game_over = False # Un peu d'anglais sa fait pas mal 
    
    while not game_over:
        couple_humain = input_humain(plateau_de_jeu)
        
        if couple_humain == False:
            game_over = True
        else:
            plateau_de_jeu[couple_humain[0]][couple_humain[1]] = HUMAIN
            print_tableau(plateau_de_jeu)
        
            if est_victoire(HUMAIN, plateau_de_jeu):
                print("Le joueur humain {} a gagné !".format(HUMAIN))
                game_over = True
        
            couple_ordi = input_ordi(plateau_de_jeu)
            plateau_de_jeu[couple_ordi[0]][couple_ordi[1]] = ORDI
            print_tableau(plateau_de_jeu)
            
            if est_victoire(ORDI, plateau_de_jeu):
                print("La machine {} a gagné ! Vous êtes nul... Allez jouer au snake ! Whahah".format(HUMAIN))
                game_over = True
def input_rejouer():
    """
    rien -> boolean
    
    Demande a l'utilisateur si il veut rejouer une partie 
    """
    while True:
        choix = input("Voulez-vous rejouer une nouvelle partie O/n").lower()
        
        if choix == 'o' or choix == "\n":
            return True
        if choix == 'n':
            return False
        
def main():
    
    continuer = True
    
    while continuer:
        joue_partie()
        continuer = input_rejouer()
main()
        
        
    

    
        