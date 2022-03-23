class GPIO:


    #méthode constructeur
    #on réinitialise le fichier voyant
    #voyant1/voyant2/voyant3/voyant4 0000
    def __init__(self):
        fichier=open("voyants.txt", "w")
        fichier.write("0000")
        fichier.close()
        print("simulation laser game")
        fichier=open("config.txt", "w")
        fichier.write("0000000000000")
        fichier.close()
        print("simulation laser game")



    #méthode affectation entrée sortie
    #vérifie si les composants sont bien affectés
    #en entrée sortie et sur les bons numéros de broche
    #variable typ contient les noms des fonctions IN et OUT
    #on récupère unique IN et OUT dans le nom
    def setup(composant,typ):
        typ=str(typ)
        typ=(typ[15:18])
        
        if composant==7 and typ=="IN ":
            fichier=open("config.txt", "r")
            contenu=fichier.read()
            fichier.close()
            contenu_avant=contenu[0:1]
            contenu_apres=contenu[2:13]
            contenu=contenu_avant+"1"+contenu_apres
            fichier=open("config.txt", "w")
            fichier.write(contenu)
            fichier.close()
            print("BP1 Actif")

        if composant==11 and typ=="IN ":
            fichier=open("config.txt", "r")
            contenu=fichier.read()
            fichier.close()
            contenu_avant=contenu[0:2]
            contenu_apres=contenu[3:13]
            contenu=contenu_avant+"1"+contenu_apres
            fichier=open("config.txt", "w")
            fichier.write(contenu)
            fichier.close()
            print("BP2 Actif")

        if composant==13 and typ=="IN ":
            fichier=open("config.txt", "r")
            contenu=fichier.read()
            fichier.close()
            contenu_avant=contenu[0:3]
            contenu_apres=contenu[4:13]
            contenu=contenu_avant+"1"+contenu_apres
            fichier=open("config.txt", "w")
            fichier.write(contenu)
            fichier.close()
            print("BP3 Actif")

        if composant==15 and typ=="IN ":
            fichier=open("config.txt", "r")
            contenu=fichier.read()
            fichier.close()
            contenu_avant=contenu[0:4]
            contenu_apres=contenu[5:13]
            contenu=contenu_avant+"1"+contenu_apres
            fichier=open("config.txt", "w")
            fichier.write(contenu)
            fichier.close()            
            print("BP4 Actif")

        if composant==29 and typ=="IN ":
            fichier=open("config.txt", "r")
            contenu=fichier.read()
            fichier.close()
            contenu_avant=contenu[0:5]
            contenu_apres=contenu[6:13]
            contenu=contenu_avant+"1"+contenu_apres
            fichier=open("config.txt", "w")
            fichier.write(contenu)
            fichier.close()
            print("LDR1 Actif")

        if composant==31 and typ=="IN ":
            fichier=open("config.txt", "r")
            contenu=fichier.read()
            fichier.close()
            contenu_avant=contenu[0:6]
            contenu_apres=contenu[7:13]
            contenu=contenu_avant+"1"+contenu_apres
            fichier=open("config.txt", "w")
            fichier.write(contenu)
            fichier.close()
            print("LDR2 Actif")

        if composant==33 and typ=="IN ":
            fichier=open("config.txt", "r")
            contenu=fichier.read()
            fichier.close()
            contenu_avant=contenu[0:7]
            contenu_apres=contenu[8:13]
            contenu=contenu_avant+"1"+contenu_apres
            fichier=open("config.txt", "w")
            fichier.write(contenu)
            fichier.close()
            print("LDR3 Actif")

        if composant==35 and typ=="IN ":
            fichier=open("config.txt", "r")
            contenu=fichier.read()
            fichier.close()
            contenu_avant=contenu[0:8]
            contenu_apres=contenu[9:13]
            contenu=contenu_avant+"1"+contenu_apres
            fichier=open("config.txt", "w")
            fichier.write(contenu)
            fichier.close()
            print("LDR4 Actif")

        if composant==32 and typ=="OUT":
            fichier=open("config.txt", "r")
            contenu=fichier.read()
            fichier.close()
            contenu_avant=contenu[0:9]
            contenu_apres=contenu[10:13]
            contenu=contenu_avant+"1"+contenu_apres
            fichier=open("config.txt", "w")
            fichier.write(contenu)
            fichier.close()
            print("Voyant1 Actif")

        if composant==36 and typ=="OUT":
            fichier=open("config.txt", "r")
            contenu=fichier.read()
            fichier.close()
            contenu_avant=contenu[0:10]
            contenu_apres=contenu[11:13]
            contenu=contenu_avant+"1"+contenu_apres
            fichier=open("config.txt", "w")
            fichier.write(contenu)
            fichier.close()
            print("Voyant2 Actif")

        if composant==38 and typ=="OUT":
            fichier=open("config.txt", "r")
            contenu=fichier.read()
            fichier.close()
            contenu_avant=contenu[0:11]
            contenu_apres=contenu[12:13]
            contenu=contenu_avant+"1"+contenu_apres
            fichier=open("config.txt", "w")
            fichier.write(contenu)
            fichier.close()
            print("Voyant3 Actif")

        if composant==40 and typ=="OUT":
            fichier=open("config.txt", "r")
            contenu=fichier.read()
            fichier.close()
            contenu_avant=contenu[0:12]
            contenu=contenu_avant+"1"
            fichier=open("config.txt", "w")
            fichier.write(contenu)
            fichier.close()
            print("Voyant4 Actif")

        fichier=open("config.txt", "r")
        print(fichier.read())
        fichier.close()

    #méthode pour savoir si les boutons sont appuyés ou pas
    #cette information est située dans le fichier boutons.txt
    #ce fichier est rempli par le programme de simulation
    def input(composant):
        fichier=open("boutons.txt", "r")
        contenu=fichier.read()
        fichier.close()
        
        if composant==7:
            if contenu[0:1]=="1":
                return True
            else:
                return False

        if composant==11:
            if contenu[1:2]=="1":
                return True
            else:
                return False

        if composant==13:
            if contenu[2:3]=="1":
                return True
            else:
                return False

        if composant==15:
            if contenu[3:4]=="1":
                return True
            else:
                return False

        if composant==29:
            if contenu[4:5]=="1":
                return True
            else:
                return False

        if composant==31:
            if contenu[5:6]=="1":
                return True
            else:
                return False

        if composant==33:
            if contenu[6:7]=="1":
                return True
            else:
                return False

        if composant==35:
            if contenu[7:8]=="1":
                return True
            else:
                return False

    def setmode(typ):
        typ=str(typ)
        typ=(typ[15:20])
        print(typ)
        fichier=open("config.txt", "r")
        contenu=fichier.read()
        fichier.close()
        contenu_apres=contenu[1:13]
        contenu="1"+contenu_apres
        fichier=open("config.txt", "w")
        fichier.write(contenu)
        fichier.close()
        fichier=open("config.txt", "r")
        print(fichier.read())
        fichier.close()
        print("carte Actif")
        return "BOARD"
    
    #méthodes récupérées par la méthode setup
    #sert à s'adapter à la vrai librairie GPIO
    def IN():
        return "IN"
    def OUT():
        return "OUT"

    #méthodes récupérées par la méthode setmode
    #sert à s'adapter à la vrai librairie GPIO
    def BOARD():
        return "BOARD"

    #méthode permettant allumée les voyants
    #l'état des voyants est écrits dans le fichier voyants.txt
    #il est récupéré par la suite par le programme de simulation
    def output(composant,etat):

        if composant==32 and etat==True:
            fichier=open("voyants.txt", "r")
            contenu=fichier.read()
            fichier.close()
            contenu_apres=contenu[1:4]
            contenu="1"+contenu_apres
            fichier=open("voyants.txt", "w")
            fichier.write(contenu)
            fichier.close()

        if composant==32 and etat==False:
            fichier=open("voyants.txt", "r")
            contenu=fichier.read()
            fichier.close()
            contenu_apres=contenu[1:4]
            contenu="0"+contenu_apres
            fichier=open("voyants.txt", "w")
            fichier.write(contenu)
            fichier.close()

        if composant==36 and etat==True:
            fichier=open("voyants.txt", "r")
            contenu=fichier.read()
            fichier.close()
            contenu_avant=contenu[0:1]
            contenu_apres=contenu[2:4]
            contenu=contenu_avant+"1"+contenu_apres
            fichier=open("voyants.txt", "w")
            fichier.write(contenu)
            fichier.close()
            

        if composant==36 and etat==False:
            fichier=open("voyants.txt", "r")
            contenu=fichier.read()
            fichier.close()
            contenu_avant=contenu[0:1]
            contenu_apres=contenu[2:4]
            contenu=contenu_avant+"0"+contenu_apres
            fichier=open("voyants.txt", "w")
            fichier.write(contenu)
            fichier.close()

        if composant==38 and etat==True:
            fichier=open("voyants.txt", "r")
            contenu=fichier.read()
            fichier.close()
            contenu_avant=contenu[0:2]
            contenu_apres=contenu[3:4]
            contenu=contenu_avant+"1"+contenu_apres
            fichier=open("voyants.txt", "w")
            fichier.write(contenu)
            fichier.close()

        if composant==38 and etat==False:
            fichier=open("voyants.txt", "r")
            contenu=fichier.read()
            fichier.close()
            contenu_avant=contenu[0:2]
            contenu_apres=contenu[3:4]
            contenu=contenu_avant+"0"+contenu_apres
            fichier=open("voyants.txt", "w")
            fichier.write(contenu)
            fichier.close()

        if composant==40 and etat==True:
            fichier=open("voyants.txt", "r")
            contenu=fichier.read()
            fichier.close()
            contenu_avant=contenu[0:3]
            contenu=contenu_avant+"1"
            fichier=open("voyants.txt", "w")
            fichier.write(contenu)
            fichier.close()

        if composant==40 and etat==False:
            fichier=open("voyants.txt", "r")
            contenu=fichier.read()
            fichier.close()
            contenu_avant=contenu[0:3]
            contenu=contenu_avant+"0"
            fichier=open("voyants.txt", "w")
            fichier.write(contenu)
            fichier.close()


        fichier=open("voyants.txt", "r")
        print(fichier.read())
        fichier.close()
            


x= GPIO()

'''
GPIO
print(GPIO.input(BP1))
if not GPIO.input(BP1):
    print("ok")
BP1 = 7
BP2 = 11
BP3 = 13
BP4 = 15
LDR1 = 29
LDR2 = 31
LDR3 = 33
LDR4 = 35
Voyant1 = 32
Voyant2 = 36
Voyant3 = 38
Voyant4 = 40
GPIO.setup(BP1,GPIO.IN)
GPIO.setup(BP2,GPIO.IN)
GPIO.setup(BP3,GPIO.IN)
GPIO.setup(BP4,GPIO.IN)
GPIO.setup(LDR1,GPIO.IN)
GPIO.setup(LDR2,GPIO.IN)
GPIO.setup(LDR3,GPIO.IN)
GPIO.setup(LDR4,GPIO.IN)
GPIO.setup(Voyant1,GPIO.OUT)
GPIO.setup(Voyant2,GPIO.OUT)
GPIO.setup(Voyant3,GPIO.OUT)
GPIO.setup(Voyant4,GPIO.OUT)
GPIO.output(32,True)
GPIO.output(36,True)
GPIO.output(38,True)
GPIO.output(40,True)
GPIO.output(32,False)
GPIO.output(36,False)
GPIO.output(38,False)
GPIO.output(40,False)
'''
