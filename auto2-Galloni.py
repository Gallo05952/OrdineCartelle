# import os
# import winshell

# def crea_shortcut(percorso_cartella, nome_cartella):
#     percorso_icona = "C:\\Percorso\\Alla\\Icona\\icona.ico"  # Percorso all'icona personalizzata
#     nome_shortcut = nome_cartella + " Shortcut"
#     shortcut_path = os.path.join(winshell.desktop(), nome_shortcut + ".lnk")
#     with winshell.shortcut(shortcut_path) as shortcut:
#         shortcut.path = percorso_cartella
#         shortcut.icon_location = (percorso_icona, 0)
#         shortcut.description = "Shortcut a " + percorso_cartella

# def organizzaFile(percorso):
#     listaFile = os.listdir(percorso)
#     cartelleDaSaltare = ["Foto", "Video", "Documenti", "Excel", "Presentazioni", "Aspen", "AutoCAD", "Altro"]
#     for file in listaFile:
#         percorsoCompleto = os.path.join(percorso, file)
#         if os.path.isfile(percorsoCompleto):
#             SeparazioneFile(percorso, file)
#         elif os.path.isdir(percorsoCompleto):
#             if file in cartelleDaSaltare:
#                 # Applica solo rimuoviCartelleVuote se la cartella è in cartelleDaSaltare
#                 rimuoviCartelleVuote(percorsoCompleto)
#             else:
#                 # Prosegue con la logica originale se la cartella non è in cartelleDaSaltare
#                 organizzaFile(percorsoCompleto)
#     # Dopo aver organizzato i file, prova a rimuovere eventuali cartelle vuote dalla cartella radice
#     rimuoviCartelleVuote(percorso)

# def SeparazioneFile(path, file):
#     # Estrae l'estensione del file in modo sicuro
#     _, estensione = os.path.splitext(file)
#     estensione = estensione[1:]  # Rimuove il punto dall'estensione
#     cartellaDestinazione = ""
#     # Dizionario per mappare estensioni a cartelle
#     # mappaEstensioni = {
#     #     "Foto": ["jpg", "png", "gif"],
#     #     "Video": ["mp4", "avi", "mov"],
#     #     "Documenti": ["doc", "docx", "pdf", "txt", "tex"],
#     #     "Excel": ["xls", "xlsx", "csv"],
#     #     "Presentazioni": ["ppt", "pptx"],
#     #     "Aspen": ["apwz", "apw"],
#     #     "AutoCAD": ["dwg", "dxf"],
#     # }
#     mappaEstensioni = {
#     "Foto": {"estensioni": ["jpg", "png", "gif"], "colore": "rosso"},
#     "Video": {"estensioni": ["mp4", "avi", "mov"], "colore": "blu"},
#     "Documenti": {"estensioni": ["doc", "docx", "pdf", "txt", "tex"], "colore": "verde"},
#     "Excel": {"estensioni": ["xls", "xlsx", "csv"], "colore": "giallo"},
#     "Presentazioni": {"estensioni": ["ppt", "pptx"], "colore": "arancione"},
#     "Aspen": {"estensioni": ["apwz", "apw"], "colore": "viola"},
#     "AutoCAD": {"estensioni": ["dwg", "dxf"], "colore": "ciano"},
#     "Altro": {"estensioni": [], "colore": "grigio"} 
#     }

#     # Esempio di come accedere alle estensioni e al colore
#     for cartella, dati in mappaEstensioni.items():
#         estensioni = dati["estensioni"]
#         colore = dati["colore"]
#     # Qui puoi implementare la logica per utilizzare le estensioni e il colore
#     # Trova la cartella di destinazione in base all'estensione
#     # for cartella, estensioni in mappaEstensioni.items():
#         if estensione in estensioni:
#             cartellaDestinazione = cartella
#             coloreCartella = colore
#             break
#     else:
#         cartellaDestinazione = "Altro"
#         coloreCartella = "default"
#     # Crea la cartella se non esiste e sposta il file, evitando duplicati come ./Foto/Foto
#     percorsoCartellaDestinazione = os.path.join(path, cartellaDestinazione)
#     if not os.path.exists(percorsoCartellaDestinazione):
#         if cartellaDestinazione != os.path.basename(path):  # Aggiunto controllo per evitare duplicati
#             os.mkdir(percorsoCartellaDestinazione)
#         else:
#             # Se la cartella di destinazione è la stessa della cartella corrente, non fare nulla
#             # o gestisci come preferisci, ad esempio stampando un messaggio
#             print(f"La cartella {cartellaDestinazione} è già presente in {path}. Operazione annullata.")
#             crea_shortcut(percorsoCartellaDestinazione, cartellaDestinazione)
#     else:
#         # Sposta il file solo se la cartella di destinazione non è la stessa della cartella corrente
#         if cartellaDestinazione != os.path.basename(path):
#             os.rename(os.path.join(path, file), os.path.join(percorsoCartellaDestinazione, file))
#         else:
#             # Gestisci il caso in cui la cartella di destinazione esiste ed è la stessa della cartella corrente
#             print(f"La cartella {cartellaDestinazione} è già presente in {path}. Operazione annullata.")

# def rimuoviCartelleVuote(percorso):
#     # Se la cartella è vuota, la elimina
#     if not os.listdir(percorso):
#         os.rmdir(percorso)
#         return
#     # Altrimenti, controlla ricorsivamente le sottocartelle
#     for file in os.listdir(percorso):
#         percorsoCompleto = os.path.join(percorso, file)
#         if os.path.isdir(percorsoCompleto):
#             rimuoviCartelleVuote(percorsoCompleto)
#             # Dopo aver controllato le sottocartelle, verifica nuovamente se la cartella corrente è vuota (potrebbe esserlo dopo aver eliminato sottocartelle vuote)
#             if not os.listdir(percorso):
#                 os.rmdir(percorso)

# # Esempio di chiamata della funzione
# percorsi_principali=[r"C:\Users\galloni\Desktop"]
# for percorsi in percorsi_principali:
#     organizzaFile(percorsi)

import os
import winshell
import ctypes

def cambia_icona_cartella(percorso_cartella, percorso_icona):
    if not os.path.isdir(percorso_cartella):
        print(f"La cartella {percorso_cartella} non esiste.")
        return
    desktop_ini = os.path.join(percorso_cartella, "desktop.ini")
    with open(desktop_ini, "w") as f:
        f.write("[.ShellClassInfo]\n")
        f.write(f"IconResource={percorso_icona},0\n")
    ctypes.windll.kernel32.SetFileAttributesW(desktop_ini, 0x2 | 0x4)
    ctypes.windll.kernel32.SetFileAttributesW(percorso_cartella, 0x4)
    ctypes.windll.shell32.SHChangeNotify(0x08000000, 0x0000, None, None)

def crea_shortcut(percorso_cartella, nome_cartella):
    percorso_icona = "C:\\Percorso\\Alla\\Icona\\icona.ico"  # Percorso all'icona personalizzata
    nome_shortcut = nome_cartella + " Shortcut"
    shortcut_path = os.path.join(winshell.desktop(), nome_shortcut + ".lnk")
    with winshell.shortcut(shortcut_path) as shortcut:
        shortcut.path = percorso_cartella
        shortcut.icon_location = (percorso_icona, 0)
        shortcut.description = "Shortcut a " + percorso_cartella

def organizzaFile(percorso):
    listaFile = os.listdir(percorso)
    cartelleDaSaltare = ["Foto", "Video", "Documenti", "Excel", "Presentazioni", "Aspen", "AutoCAD", "Altro"]
    for file in listaFile:
        percorsoCompleto = os.path.join(percorso, file)
        if os.path.isfile(percorsoCompleto):
            SeparazioneFile(percorso, file)
        elif os.path.isdir(percorsoCompleto) and file not in cartelleDaSaltare:
            organizzaFile(percorsoCompleto)
    rimuoviCartelleVuote(percorso)

def SeparazioneFile(path, file):
    _, estensione = os.path.splitext(file)
    estensione = estensione[1:]  # Rimuove il punto dall'estensione
    mappaEstensioni = {
        "Foto": {"estensioni": ["jpg", "png", "gif"], "icona": r"C:\Users\galloni\OneDrive\Immagini\Icone\foto.ico"},
        "Video": {"estensioni": ["mp4", "avi", "mov"], "icona": r"C:\Users\galloni\OneDrive\Immagini\Icone\video.ico"},
        "Documenti": {"estensioni": ["doc", "docx", "pdf", "txt", "tex"], "icona": r"C:\Users\galloni\OneDrive\Immagini\Icone\documenti.ico"},
        "Excel": {"estensioni": ["xls", "xlsx", "csv"], "icona": r"C:\Users\galloni\OneDrive\Immagini\Icone\excel.ico"},
        "Presentazioni": {"estensioni": ["ppt", "pptx"], "icona": r"C:\Users\galloni\OneDrive\Immagini\Icone\presentazioni.ico"},
        "Aspen": {"estensioni": ["apwz", "apw"], "icona": r"C:\Users\galloni\OneDrive\Immagini\Icone\aspen.ico"},
        "AutoCAD": {"estensioni": ["dwg", "dxf"], "icona": r"C:\Users\galloni\OneDrive\Immagini\Icone\cad.ico"},
        "Altro": {"estensioni": [], "icona": r"C:\Users\galloni\OneDrive\Immagini\Icone\altro.ico"}
    }
    for cartella, dati in mappaEstensioni.items():
        if estensione in dati["estensioni"]:
            percorsoCartellaDestinazione = os.path.join(path, cartella)
            if not os.path.exists(percorsoCartellaDestinazione):
                os.makedirs(percorsoCartellaDestinazione, exist_ok=True)
                cambia_icona_cartella(percorsoCartellaDestinazione, dati["icona"])
            os.rename(os.path.join(path, file), os.path.join(percorsoCartellaDestinazione, file))
            break
    else:
        cartellaDestinazione = "Altro"
        percorsoCartellaDestinazione = os.path.join(path, cartellaDestinazione)
        if not os.path.exists(percorsoCartellaDestinazione):
            os.makedirs(percorsoCartellaDestinazione, exist_ok=True)
            cambia_icona_cartella(percorsoCartellaDestinazione, mappaEstensioni[cartellaDestinazione]["icona"])
        os.rename(os.path.join(path, file), os.path.join(percorsoCartellaDestinazione, file))

def rimuoviCartelleVuote(percorso):
    if not os.listdir(percorso):
        os.rmdir(percorso)
        return
    for file in os.listdir(percorso):
        percorsoCompleto = os.path.join(percorso, file)
        if os.path.isdir(percorsoCompleto):
            rimuoviCartelleVuote(percorsoCompleto)
            if not os.listdir(percorso):
                os.rmdir(percorso)

percorsi_principali = [r"C:\Users\galloni\Desktop"]
for percorsi in percorsi_principali:
    organizzaFile(percorsi)