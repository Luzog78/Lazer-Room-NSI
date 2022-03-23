from tkinter import *

#fonctions lancées quand on appuie sur les boutons jeux
def appui_bouton_amp1():
    global boucle_bouton1

    #si bouton appuyé alors
    #on ouvre le fichier et on met 1 à l'emplacement du bouton (voir fichier boutons)
    #et on relance la fonction au bout d'une seconde
    if boucle_bouton1==0:
        boucle_bouton1=1
        
        fichier=open("boutons.txt", "r")
        contenu=fichier.read()
        fichier.close()
        
        contenu_apres=contenu[1:8]
        contenu="1"+contenu_apres
        
        fichier=open("boutons.txt", "w")
        fichier.write(contenu)
        fichier.close()
        
        fenetre.after(1000,appui_bouton_amp1)

    #Après avoir relancé la fonction
    #on ouvre le fichier et on met 0 à l'emplacement du bouton (voir fichier boutons)
    else:
        boucle_bouton1=0
        
        fichier=open("boutons.txt", "r")
        contenu=fichier.read()
        fichier.close()
        
        contenu_apres=contenu[1:8]
        contenu="0"+contenu_apres
        
        fichier=open("boutons.txt", "w")
        fichier.write(contenu)
        fichier.close()

    #on print le contenu du fichier pour vérifier
    fichier=open("boutons.txt", "r")
    print(fichier.read())
    fichier.close()

def appui_bouton_amp2():
    global boucle_bouton2

    #si bouton appuyé alors
    #on ouvre le fichier et on met 1 à l'emplacement du bouton (voir fichier boutons)
    #et on relance la fonction au bout d'une seconde
    if boucle_bouton2==0:
        boucle_bouton2=1

        fichier=open("boutons.txt", "r")
        contenu=fichier.read()
        fichier.close()

        contenu_avant=contenu[0:1]
        contenu_apres=contenu[2:8]
        contenu=contenu_avant+"1"+contenu_apres
        
        fichier=open("boutons.txt", "w")
        fichier.write(contenu)
        fichier.close()
        
        fenetre.after(1000,appui_bouton_amp2)

    #Après avoir relancé la fonction
    #on ouvre le fichier et on met 0 à l'emplacement du bouton (voir fichier boutons)    
    else:
        boucle_bouton2=0

        fichier=open("boutons.txt", "r")
        contenu=fichier.read()
        fichier.close()

        contenu_avant=contenu[0:1]
        contenu_apres=contenu[2:8]
        contenu=contenu_avant+"0"+contenu_apres
        
        fichier=open("boutons.txt", "w")
        fichier.write(contenu)
        fichier.close()

    #on print le contenu du fichier pour vérifier
    fichier=open("boutons.txt", "r")
    print(fichier.read())
    fichier.close()

def appui_bouton_amp3():
    global boucle_bouton3

    #si bouton appuyé alors
    #on ouvre le fichier et on met 1 à l'emplacement du bouton (voir fichier boutons)
    #et on relance la fonction au bout d'une seconde
    if boucle_bouton3==0:
        boucle_bouton3=1

        fichier=open("boutons.txt", "r")
        contenu=fichier.read()
        fichier.close()

        contenu_avant=contenu[0:2]
        contenu_apres=contenu[3:8]
        contenu=contenu_avant+"1"+contenu_apres
        
        fichier=open("boutons.txt", "w")
        fichier.write(contenu)
        fichier.close()
        
        fenetre.after(1000,appui_bouton_amp3)
        
    #Après avoir relancé la fonction
    #on ouvre le fichier et on met 0 à l'emplacement du bouton (voir fichier boutons)    
    else:
        boucle_bouton3=0
        
        fichier=open("boutons.txt", "r")
        contenu=fichier.read()
        fichier.close()

        contenu_avant=contenu[0:2]
        contenu_apres=contenu[3:8]
        contenu=contenu_avant+"0"+contenu_apres
        
        fichier=open("boutons.txt", "w")
        fichier.write(contenu)
        fichier.close()

    #on print le contenu du fichier pour vérifier
    fichier=open("boutons.txt", "r")
    print(fichier.read())
    fichier.close()

def appui_bouton_amp4():
    global boucle_bouton4

    #si bouton appuyé alors
    #on ouvre le fichier et on met 1 à l'emplacement du bouton (voir fichier boutons)
    #et on relance la fonction au bout d'une seconde
    if boucle_bouton4==0:
        boucle_bouton4=1

        fichier=open("boutons.txt", "r")
        contenu=fichier.read()
        fichier.close()

        contenu_avant=contenu[0:3]
        contenu_apres=contenu[4:8]
        contenu=contenu_avant+"1"+contenu_apres
        
        fichier=open("boutons.txt", "w")
        fichier.write(contenu)
        fichier.close()
        
        fenetre.after(1000,appui_bouton_amp4)

    #Après avoir relancé la fonction
    #on ouvre le fichier et on met 0 à l'emplacement du bouton (voir fichier boutons)    
    else:
        boucle_bouton4=0

        fichier=open("boutons.txt", "r")
        contenu=fichier.read()
        fichier.close()

        contenu_avant=contenu[0:3]
        contenu_apres=contenu[4:8]
        contenu=contenu_avant+"0"+contenu_apres
        
        fichier=open("boutons.txt", "w")
        fichier.write(contenu)
        fichier.close()

    #on print le contenu du fichier pour vérifier
    fichier=open("boutons.txt", "r")
    print(fichier.read())
    fichier.close()


#fonctions lancées quand on appuie sur les boutons lasers
def appui_bouton_las1():
    global laser1
    #si on appuie sur le bouton laser avec laser allumé
    #on change l'image en laser éteint
    #on ouvre le fichier et on met 0 à l'emplacement du laser (voir fichier boutons)
    if laser1==1:
        canvas.create_image(10,180,image=dic_image["laser eteint"],anchor="nw")
        laser1=0
        
        fichier=open("boutons.txt", "r")
        contenu=fichier.read()
        fichier.close()

        contenu_avant=contenu[0:4]
        contenu_apres=contenu[5:8]
        contenu=contenu_avant+"1"+contenu_apres
        
        fichier=open("boutons.txt", "w")
        fichier.write(contenu)
        fichier.close()

    #si on appuie sur le bouton laser avec laser éteint
    #on change l'image en laser allumé
    #on ouvre le fichier et on met 1 à l'emplacement du laser (voir fichier boutons)
    else:
        canvas.create_image(10,180,image=dic_image["laser allume"],anchor="nw")
        laser1=1

        fichier=open("boutons.txt", "r")
        contenu=fichier.read()
        fichier.close()

        contenu_avant=contenu[0:4]
        contenu_apres=contenu[5:8]
        contenu=contenu_avant+"0"+contenu_apres
        
        fichier=open("boutons.txt", "w")
        fichier.write(contenu)
        fichier.close()

    #on print le contenu du fichier pour vérifier
    fichier=open("boutons.txt", "r")
    print(fichier.read())
    fichier.close()

def appui_bouton_las2():
    global laser2
    #si on appuie sur le bouton laser avec laser allumé
    #on change l'image en laser éteint
    #on ouvre le fichier et on met 0 à l'emplacement du laser (voir fichier boutons)
    if laser2==1:
        canvas.create_image(10,250,image=dic_image["laser eteint"],anchor="nw")
        laser2=0

        fichier=open("boutons.txt", "r")
        contenu=fichier.read()
        fichier.close()

        contenu_avant=contenu[0:5]
        contenu_apres=contenu[6:8]
        contenu=contenu_avant+"1"+contenu_apres
        
        fichier=open("boutons.txt", "w")
        fichier.write(contenu)
        fichier.close()

    #si on appuie sur le bouton laser avec laser éteint
    #on change l'image en laser allumé
    #on ouvre le fichier et on met 1 à l'emplacement du laser (voir fichier boutons)    
    else:
        canvas.create_image(10,250,image=dic_image["laser allume"],anchor="nw")
        laser2=1

        fichier=open("boutons.txt", "r")
        contenu=fichier.read()
        fichier.close()

        contenu_avant=contenu[0:5]
        contenu_apres=contenu[6:8]
        contenu=contenu_avant+"0"+contenu_apres
        
        fichier=open("boutons.txt", "w")
        fichier.write(contenu)
        fichier.close()

    #on print le contenu du fichier pour vérifier
    fichier=open("boutons.txt", "r")
    print(fichier.read())
    fichier.close()

def appui_bouton_las3():
    global laser3
    #si on appuie sur le bouton laser avec laser allumé
    #on change l'image en laser éteint
    #on ouvre le fichier et on met 0 à l'emplacement du laser (voir fichier boutons)
    if laser3==1:
        canvas.create_image(10,320,image=dic_image["laser eteint"],anchor="nw")
        laser3=0

        fichier=open("boutons.txt", "r")
        contenu=fichier.read()
        fichier.close()

        contenu_avant=contenu[0:6]
        contenu_apres=contenu[7:8]
        contenu=contenu_avant+"1"+contenu_apres
        
        fichier=open("boutons.txt", "w")
        fichier.write(contenu)
        fichier.close()

    #si on appuie sur le bouton laser avec laser éteint
    #on change l'image en laser allumé
    #on ouvre le fichier et on met 1 à l'emplacement du laser (voir fichier boutons)    
    else:
        canvas.create_image(10,320,image=dic_image["laser allume"],anchor="nw")
        laser3=1

        fichier=open("boutons.txt", "r")
        contenu=fichier.read()
        fichier.close()

        contenu_avant=contenu[0:6]
        contenu_apres=contenu[7:8]
        contenu=contenu_avant+"0"+contenu_apres
        
        fichier=open("boutons.txt", "w")
        fichier.write(contenu)
        fichier.close()

    #on print le contenu du fichier pour vérifier
    fichier=open("boutons.txt", "r")
    print(fichier.read())
    fichier.close()

def appui_bouton_las4():
    global laser4
    #si on appuie sur le bouton laser avec laser allumé
    #on change l'image en laser éteint
    #on ouvre le fichier et on met 0 à l'emplacement du laser (voir fichier boutons)
    if laser4==1:
        canvas.create_image(10,390,image=dic_image["laser eteint"],anchor="nw")
        laser4=0

        fichier=open("boutons.txt", "r")
        contenu=fichier.read()
        fichier.close()

        contenu_avant=contenu[0:7]
        contenu=contenu_avant+"1"
        
        fichier=open("boutons.txt", "w")
        fichier.write(contenu)
        fichier.close()

    #si on appuie sur le bouton laser avec laser éteint
    #on change l'image en laser allumé
    #on ouvre le fichier et on met 1 à l'emplacement du laser (voir fichier boutons)    
    else:
        canvas.create_image(10,390,image=dic_image["laser allume"],anchor="nw")
        laser4=1

        fichier=open("boutons.txt", "r")
        contenu=fichier.read()
        fichier.close()

        contenu_avant=contenu[0:7]
        contenu=contenu_avant+"0"
        
        fichier=open("boutons.txt", "w")
        fichier.write(contenu)
        fichier.close()

    #on print le contenu du fichier pour vérifier
    fichier=open("boutons.txt", "r")
    print(fichier.read())
    fichier.close()

#Boucle infini pour vérifier l'état des LED
def jeu():
    global choix, dic_image

    fichier=open("voyants.txt", "r")
    contenu=fichier.read()
    fichier.close()
    
    if contenu[0:1]=="1" :
        image=dic_image["ampoule allume"]
        canvas.create_image(50,30,image=image,anchor="nw")
        
    else:
        image=dic_image["ampoule eteinte"]
        canvas.create_image(50,30,image=image,anchor="nw")
        
    if contenu[1:2]=="1" :
        image=dic_image["ampoule allume"]
        canvas.create_image(500,30,image=image,anchor="nw")
        
    else:
        image=dic_image["ampoule eteinte"]
        canvas.create_image(500,30,image=image,anchor="nw")
        
    if contenu[2:3]=="1" :
        image=dic_image["ampoule allume"]
        canvas.create_image(50,460,image=image,anchor="nw")
        
    else:
        image=dic_image["ampoule eteinte"]
        canvas.create_image(50,460,image=image,anchor="nw")

    if contenu[3:4]=="1" :
        image=dic_image["ampoule allume"]
        canvas.create_image(500,460,image=image,anchor="nw")
        
    else:
        image=dic_image["ampoule eteinte"]
        canvas.create_image(500,460,image=image,anchor="nw")

    fichier=open("config.txt", "r")
    contenu=fichier.read()
    fichier.close()

    if contenu[0:1]=="1":
        Lab_Carte.config(bg="green")
    else:
        Lab_Carte.config(bg="red")

    if contenu[1:2]=="1":
        Lab_BP1.config(bg="green")
    else:
        Lab_BP1.config(bg="red")
        
    if contenu[2:3]=="1":
        Lab_BP2.config(bg="green")
    else:
        Lab_BP2.config(bg="red")

    if contenu[3:4]=="1":
        Lab_BP3.config(bg="green")
    else:
        Lab_BP3.config(bg="red")

    if contenu[4:5]=="1":
        Lab_BP4.config(bg="green")
    else:
        Lab_BP4.config(bg="red")

    if contenu[5:6]=="1":
        Lab_Capt1.config(bg="green")
    else:
        Lab_Capt1.config(bg="red")

    if contenu[6:7]=="1":
        Lab_Capt2.config(bg="green")
    else:
        Lab_Capt2.config(bg="red")

    if contenu[7:8]=="1":
        Lab_Capt3.config(bg="green")
    else:
        Lab_Capt3.config(bg="red")

    if contenu[8:9]=="1":
        Lab_Capt4.config(bg="green")
    else:
        Lab_Capt4.config(bg="red")

    if contenu[9:10]=="1":
        Lab_Voy1.config(bg="green")
    else:
        Lab_Voy1.config(bg="red")

    if contenu[10:11]=="1":
        Lab_Voy2.config(bg="green")
    else:
        Lab_Voy2.config(bg="red")

    if contenu[11:12]=="1":
        Lab_Voy3.config(bg="green")
    else:
        Lab_Voy3.config(bg="red")

    if contenu[12:13]=="1":
        Lab_Voy4.config(bg="green")
    else:
        Lab_Voy4.config(bg="red")

    fenetre.after(1000,jeu)  


#Création de la fenêtre avec le canvas
fenetre = Tk()
fenetre.geometry("850x700")
fenetre.config(bg = "white")
canvas = Canvas(fenetre, width=700, height=700, bg="white")
canvas.place(x=0,y=0)
choix=0

#Réinitialise le fichier bouton : laser allumé et boutons jeux non appuyés
#bouton1/bouton2/bouton3/bouton4/laser1/laser2/laser3/laser4 00001111
fichier=open("boutons.txt", "w")
fichier.write("00000000")
fichier.close()

#Placement des images des ampoules et des lasers dans le dictionnaire d'images
dic_image={}
dic_image["ampoule allume"]=PhotoImage(file="ampoule allume.gif")
dic_image["ampoule eteinte"]=PhotoImage(file="ampoule eteinte.gif")
dic_image["laser eteint"]=PhotoImage(file="laser eteint.gif")
dic_image["laser allume"]=PhotoImage(file="laser allume.gif")

#Affichage des images de laser
canvas.create_image(10,180,image=dic_image["laser allume"],anchor="nw")
canvas.create_image(10,250,image=dic_image["laser allume"],anchor="nw")
canvas.create_image(10,320,image=dic_image["laser allume"],anchor="nw")
canvas.create_image(10,390,image=dic_image["laser allume"],anchor="nw")

#Indique que les bouton sont non appuyés par défaut
#boucle_bouton=0 bouton non appuyé
#boucle_bouton=1 bouton appuyé
boucle_bouton1=0
boucle_bouton2=0
boucle_bouton3=0
boucle_bouton4=0

#Création des boutons ampoules
bouton_amp1=Button(fenetre,text="Bouton 1",command=appui_bouton_amp1)
bouton_amp1.place(x=70,y=130)
bouton_amp2=Button(fenetre,text="Bouton 2",command=appui_bouton_amp2)
bouton_amp2.place(x=520,y=130)
bouton_amp3=Button(fenetre,text="Bouton 3",command=appui_bouton_amp3)
bouton_amp3.place(x=70,y=560)
bouton_amp4=Button(fenetre,text="Bouton 4",command=appui_bouton_amp4)
bouton_amp4.place(x=520,y=560)

#Indique que les lasers sont allumés par défaut
#laser=0 laser éteint
#laser=1 laser allumé
laser1=1
laser2=1
laser3=1
laser4=1

#Création des boutons laser
bouton_las1=Button(fenetre,text="laser 1",command=appui_bouton_las1)
bouton_las1.place(x=30,y=190)
bouton_las2=Button(fenetre,text="laser 2",command=appui_bouton_las2)
bouton_las2.place(x=30,y=260)
bouton_las3=Button(fenetre,text="laser 3",command=appui_bouton_las3)
bouton_las3.place(x=30,y=330)
bouton_las4=Button(fenetre,text="laser 4",command=appui_bouton_las4)
bouton_las4.place(x=30,y=400)

#Emplacement des labels pour indiquer si les composants sont actifs
Lab_BP1=Label(fenetre,text="Bouton1")
Lab_BP1.config(bg="red")
Lab_BP1.place(x=750,y=20)
Lab_BP2=Label(fenetre,text="Bouton2")
Lab_BP2.config(bg="red")
Lab_BP2.place(x=750,y=60)
Lab_BP3=Label(fenetre,text="Bouton3")
Lab_BP3.config(bg="red")
Lab_BP3.place(x=750,y=100)
Lab_BP4=Label(fenetre,text="Bouton4")
Lab_BP4.config(bg="red")
Lab_BP4.place(x=750,y=140)
Lab_Capt1=Label(fenetre,text="Capteur1")
Lab_Capt1.config(bg="red")
Lab_Capt1.place(x=750,y=180)
Lab_Capt2=Label(fenetre,text="Capteur2")
Lab_Capt2.config(bg="red")
Lab_Capt2.place(x=750,y=220)
Lab_Capt3=Label(fenetre,text="Capteur3")
Lab_Capt3.config(bg="red")
Lab_Capt3.place(x=750,y=260)
Lab_Capt4=Label(fenetre,text="Capteur4")
Lab_Capt4.config(bg="red")
Lab_Capt4.place(x=750,y=300)
Lab_Voy1=Label(fenetre,text="Voyant1")
Lab_Voy1.config(bg="red")
Lab_Voy1.place(x=750,y=340)
Lab_Voy2=Label(fenetre,text="Voyant2")
Lab_Voy2.config(bg="red")
Lab_Voy2.place(x=750,y=380)
Lab_Voy3=Label(fenetre,text="Voyant3")
Lab_Voy3.config(bg="red")
Lab_Voy3.place(x=750,y=420)
Lab_Voy4=Label(fenetre,text="Voyant4")
Lab_Voy4.config(bg="red")
Lab_Voy4.place(x=750,y=460)
Lab_Carte=Label(fenetre,text="Carte")
Lab_Carte.config(bg="red")
Lab_Carte.place(x=750,y=500)

jeu()
mainloop()

