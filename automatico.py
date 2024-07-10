import os    

def organizzaFile(percorso):
        #lista dei file presenti nella cartella
        listaFile=os.listdir(percorso)
        for file in listaFile:
            if os.path.isfile(percorso+"\\"+file):
                SeparazioneFile(percorso,file)

def SeparazioneFile(path,file):
    # in base all'estensione del file dividi in cartelle tipo: Foto, Video, Documenti, Altro
    estensione=file.split(".")[1]
    if estensione in ["jpg","png","gif"]:
        if not os.path.exists(path+"\\Foto"):
            os.mkdir(path+"\\Foto")
            #sposta il file
            os.rename(path+"\\"+file,path+"\\Foto\\"+file)
    elif estensione in ["mp4","avi","mov"]:
        if not os.path.exists(path+"\\Video"):
            os.mkdir(path+"\\Video")
            #sposta il file
            os.rename(path+"\\"+file,path+"\\Video\\"+file)
    elif estensione in ["doc","docx","pdf","txt","tex"]:
        if not os.path.exists(path+"\\Documenti"):
            os.mkdir(path+"\\Documenti")
            #sposta il file
            os.rename(path+"\\"+file,path+"\\Documenti\\"+file)
    elif estensione in ["xls","xlsx","csv"]:
        if not os.path.exists(path+"\\Excel"):
            os.mkdir(path+"\\Excel")
            #sposta il file
            os.rename(path+"\\"+file,path+"\\Excel\\"+file)
    elif estensione in ["ppt","pptx"]:
        if not os.path.exists(path+"\\Presentazioni"):
            os.mkdir(path+"\\Presentazioni")
            #sposta il file
            os.rename(path+"\\"+file,path+"\\Presentazioni\\"+file)
    elif estensione in ["apwz","apw"]:
        if not os.path.exists(path+"\\Aspen"):
            os.mkdir(path+"\\Aspen")
            #sposta il file
            os.rename(path+"\\"+file,path+"\\Aspen\\"+file)
    elif estensione in ["dwg","dxf"]:
        if not os.path.exists(path+"\\AutoCAD"):
            os.mkdir(path+"\\AutoCAD")
            #sposta il file
            os.rename(path+"\\"+file,path+"\\AutoCAD\\"+file)
    else:
        if not os.path.exists(path+"\\Altro"):
            os.mkdir(path+"\\Altro")
            #sposta il file
            os.rename(path+"\\"+file,path+"\\Altro\\"+file)

def checkCartelle(percorso):
    # Ottieni tutti gli elementi nel percorso specificato
    elementi = os.listdir(percorso)

    # Filtra solo le cartelle
    listaCartelle = [elemento for elemento in elementi if os.path.isdir(os.path.join(percorso, elemento))]
    if "Foto" in listaCartelle or "Video" in listaCartelle or "Documenti" in listaCartelle or "Excel" in listaCartelle or "Presentazioni" in listaCartelle or "Aspen" in listaCartelle or "AutoCAD" in listaCartelle or "Altro" in listaCartelle:
        return False
    else:
        return True

def ConfrontoCartelle(percorso):
    elementi = os.listdir(percorso)
    listaCartelle = [elemento for elemento in elementi if os.path.isdir(os.path.join(percorso, elemento))]
    cartellePermesse = ["Foto", "Video", "Documenti", "Excel", "Presentazioni", "Aspen", "AutoCAD", "Altro"]
    
    dentro = False
    for cartella in listaCartelle:
        if cartella not in cartellePermesse:
            dentro = True
            break  # Interrompe il ciclo una volta trovata una cartella non permessa

    return dentro

def BottomCartella(percorso,cartelleFatte):
    elementi = os.listdir(percorso)
    listaCartelle = [elemento for elemento in elementi if os.path.isdir(os.path.join(percorso, elemento))]
    cartellePermesse = ["Foto", "Video", "Documenti", "Excel", "Presentazioni", "Aspen", "AutoCAD", "Altro"]
    CartelleMancanti = [cartella for cartella in listaCartelle if cartella not in cartellePermesse]
    CartelleMancanti = [cartella for cartella in CartelleMancanti if cartella not in cartelleFatte]
    if CartelleMancanti:
        percorso = percorso + "\\" + CartelleMancanti[0]
        bottom = True
        # Correzione: utilizza lo slicing per rimuovere il primo elemento dalla lista
        listaCartelle.append(CartelleMancanti[0])
    else:
        bottom = False
        percorso = percorso
        listaCartelle = None
    return percorso, bottom, listaCartelle

def checkSottocartelle(percorso, cartelleOrdine):
    if not os.path.exists(percorso):
        return False
    else:
        elementi = os.listdir(percorso)
        listaCartelle = [elemento for elemento in elementi if os.path.isdir(os.path.join(percorso, elemento))]
        cartellePermesse = [cartella for cartella in listaCartelle if cartella not in cartelleOrdine]
        if cartellePermesse:
            return True
        else:
            return False


percorsi_principali=[r"C:\Users\galloni\Downloads"]

for percorso in percorsi_principali:
    print(percorso)
    percorsoMod=percorso
    CartelleDaFare = []
    listCartelle = []
    elementi = os.listdir(percorso)
    listaCartelle = [elemento for elemento in elementi if os.path.isdir(os.path.join(percorso, elemento))]
    CartelleOrdine=["Foto","Video","Documenti","Excel","Presentazioni","Aspen","AutoCAD","Altro"]
    CartelleDaFare = [cartella for cartella in listaCartelle if cartella not in CartelleOrdine]
    print(CartelleDaFare)
    finito = False
    while finito == False:
        print("percorsoMod:", percorsoMod)
        print("CartelleDaFare:", CartelleDaFare)
        print("checkSottocartelle result:", checkSottocartelle(percorsoMod, CartelleOrdine))
        print("percorso:", percorso)
        if checkSottocartelle(percorsoMod,CartelleOrdine) and CartelleDaFare:
            elementi = os.listdir(percorsoMod)
            listaCartelle = [elemento for elemento in elementi if os.path.isdir(os.path.join(percorsoMod, elemento))]
            CartelleDaFare=[cartella for cartella in listaCartelle if cartella not in CartelleOrdine]
            print(CartelleDaFare)
            percorsoMod = os.path.join(percorsoMod,CartelleDaFare[0])
            print("Deep level")
        elif checkSottocartelle(percorsoMod,CartelleOrdine) == False and CartelleDaFare:
            while CartelleDaFare:
                percorsoMod = os.path.join(percorsoMod,CartelleDaFare[0])
                CartelleDaFare = CartelleDaFare[1:]
                print("Deep level")
                print(CartelleDaFare)

        elif checkSottocartelle(percorsoMod,CartelleOrdine) == False and CartelleDaFare == [] and percorsoMod != percorso:
            percorsoMod = os.path.dirname(percorsoMod)
            print(percorsoMod)
            print("Upper level")
        else :
            finito = True