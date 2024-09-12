# import os
# import tkinter as tk
# from tkinter import filedialog

# class Finestra():
#     def __init__(self,root):
#         self.root = root
#         self.root.title("Organizzatore File")
#         self.root.geometry("800x300")

#     def creaFinestra(self):
#         self.titolo = tk.Label(self.root, text="Organizzatore File", font=("Arial", 20, "bold"), fg="green")
#         self.titolo.grid(row=0,column=0,columnspan=2)
#         #spazio
#         self.spazio=tk.Label(self.root,text="")
#         self.spazio.grid(row=1,column=1)
#         #bottone sfoglia per il percorso
#         self.bottoneSfoglia=tk.Button(self.root,text="Sfoglia",command=self.scegliPercorso)
#         self.bottoneSfoglia.grid(row=2,column=0)
               
#     def scegliPercorso(self):
#         self.percorso=tk.filedialog.askdirectory()
#         self.Foto=tk.IntVar()
#         self.Video=tk.IntVar()
#         self.Documenti=tk.IntVar()
#         self.Excel=tk.IntVar()
#         self.Presentazioni=tk.IntVar()
#         self.Aspen=tk.IntVar()
#         self.AutoCAD=tk.IntVar()
#         self.Altro=tk.IntVar()
            
#         if self.percorso:
#             self.percorsoLabel=tk.Label(self.root,text="Percorso selezionato: "+self.percorso)
#             self.percorsoLabel.grid(row=3,column=0,columnspan=5)
#             #checkbox per espire le preferenze delle cartelle da creare
#             self.FotoCheck=tk.Checkbutton(self.root,text="Foto",variable=self.Foto)
#             self.FotoCheck.grid(row=4,column=0)
#             self.VideoCheck=tk.Checkbutton(self.root,text="Video",variable=self.Video)
#             self.VideoCheck.grid(row=4,column=1)
#             self.DocumentiCheck=tk.Checkbutton(self.root,text="Documenti",variable=self.Documenti)
#             self.DocumentiCheck.grid(row=4,column=2)
#             self.ExcelCheck=tk.Checkbutton(self.root,text="Excel",variable=self.Excel)
#             self.ExcelCheck.grid(row=4,column=3)
#             self.PresentazioniCheck=tk.Checkbutton(self.root,text="Presentazioni",variable=self.Presentazioni)
#             self.PresentazioniCheck.grid(row=4,column=4)
#             self.AspenCheck=tk.Checkbutton(self.root,text="Aspen",variable=self.Aspen)
#             self.AspenCheck.grid(row=4,column=5)
#             self.AutoCADCheck=tk.Checkbutton(self.root,text="AutoCAD",variable=self.AutoCAD)
#             self.AutoCADCheck.grid(row=4,column=6)
#             self.AltroCheck=tk.Checkbutton(self.root,text="Altro",variable=self.Altro)
#             self.AltroCheck.grid(row=4,column=7)
#             #bottone per avviare la funzione
#             self.bottoneAvvia=tk.Button(self.root,text="Avvia",command=lambda:self.organizzaFile(self.percorso))
#             self.bottoneAvvia.grid(row=5,column=0)

#     def organizzaFile(self,percorso):
#         #lista dei file presenti nella cartella
#         listaFile=os.listdir(percorso)
#         for file in listaFile:
#             if os.path.isfile(percorso+"\\"+file):
#                 self.SeparazioneFile(percorso,file)
#         print("File organizzati")
#         self.avviso=tk.Label(self.root,text="File organizzati",fg="green")
#         self.avviso.grid(row=5,column=0)

#     def SeparazioneFile(self,path,file):
#         # in base all'estensione del file dividi in cartelle tipo: Foto, Video, Documenti, Altro
#         estensione=file.split(".")[1]
#         cartella_provenienza=os.path.dirname(file)
#         print(cartella_provenienza)
#         if estensione in ["jpg","png","gif"]:
#             if self.Foto.get():
#                 if cartella_provenienza=="Foto":
#                     return
#                 else:
#                     if not os.path.exists(path+"\\Foto"):
#                         os.mkdir(path+"\\Foto")
#                         #sposta il file
#                         os.rename(path+"\\"+file,path+"\\Foto\\"+file)
#         elif estensione in ["mp4","avi","mov"]:
#             if self.Video.get():
#                 if not os.path.exists(path+"\\Video"):
#                     os.mkdir(path+"\\Video")
#                     #sposta il file
#                     os.rename(path+"\\"+file,path+"\\Video\\"+file)
#         elif estensione in ["doc","docx","pdf","txt","tex"]:
#             if self.Documenti.get():
#                 if not os.path.exists(path+"\\Documenti"):
#                     os.mkdir(path+"\\Documenti")
#                     #sposta il file
#                     os.rename(path+"\\"+file,path+"\\Documenti\\"+file)
#         elif estensione in ["xls","xlsx","csv"]:
#             if self.Excel.get():
#                 if not os.path.exists(path+"\\Excel"):
#                     os.mkdir(path+"\\Excel")
#                     #sposta il file
#                     os.rename(path+"\\"+file,path+"\\Excel\\"+file)
#         elif estensione in ["ppt","pptx"]:
#             if self.Presentazioni.get():
#                 if not os.path.exists(path+"\\Presentazioni"):
#                     os.mkdir(path+"\\Presentazioni")
#                     #sposta il file
#                     os.rename(path+"\\"+file,path+"\\Presentazioni\\"+file)
#         elif estensione in ["apwz","apw"]:
#             if self.Aspen.get():
#                 if not os.path.exists(path+"\\Aspen"):
#                     os.mkdir(path+"\\Aspen")
#                     #sposta il file
#                     os.rename(path+"\\"+file,path+"\\Aspen\\"+file)
#         elif estensione in ["dwg","dxf"]:
#             if self.AutoCAD.get():
#                 if not os.path.exists(path+"\\AutoCAD"):
#                     os.mkdir(path+"\\AutoCAD")
#                     #sposta il file
#                     os.rename(path+"\\"+file,path+"\\AutoCAD\\"+file)
#         else:
#             if self.Altro.get():
#                 if not os.path.exists(path+"\\Altro"):
#                     os.mkdir(path+"\\Altro")
#                     #sposta il file
#                     os.rename(path+"\\"+file,path+"\\Altro\\"+file)


# if __name__ == "__main__":
#     root = tk.Tk()
#     finestra = Finestra(root)
#     finestra.creaFinestra()
#     root.mainloop()
import os
import tkinter as tk
from tkinter import filedialog
import ctypes

class Finestra():
    def __init__(self, root):
        self.root = root
        self.root.title("Organizzatore File")
        self.root.geometry("800x300")

    def creaFinestra(self):
        self.titolo = tk.Label(self.root, text="Organizzatore File", font=("Arial", 20, "bold"), fg="green")
        self.titolo.grid(row=0, column=0, columnspan=2)
        # spazio
        self.spazio = tk.Label(self.root, text="")
        self.spazio.grid(row=1, column=1)
        # bottone sfoglia per il percorso
        self.bottoneSfoglia = tk.Button(self.root, text="Sfoglia", command=self.scegliPercorso)
        self.bottoneSfoglia.grid(row=2, column=0)

    def scegliPercorso(self):
        self.percorso = tk.filedialog.askdirectory()
        self.Foto = tk.IntVar()
        self.Video = tk.IntVar()
        self.Documenti = tk.IntVar()
        self.Excel = tk.IntVar()
        self.Presentazioni = tk.IntVar()
        self.Aspen = tk.IntVar()
        self.AutoCAD = tk.IntVar()
        self.Altro = tk.IntVar()
        self.selezionaTutto=tk.IntVar()

        if self.percorso:
            self.percorsoLabel = tk.Label(self.root, text="Percorso selezionato: " + self.percorso)
            self.percorsoLabel.grid(row=3, column=0, columnspan=5)
            # checkbox per esprimere le preferenze delle cartelle da creare

                    # Funzione per selezionare/deselezionare tutti i checkbox
            def seleziona_tutti():
                stato = self.selezionaTutto.get()
                self.Foto.set(stato)
                self.Video.set(stato)
                self.Documenti.set(stato)
                self.Excel.set(stato)
                self.Presentazioni.set(stato)
                self.Aspen.set(stato)
                self.AutoCAD.set(stato)
                self.Altro.set(stato)
                # Checkbox "Seleziona tutto"
            self.SelezionaTuttoCheck = tk.Checkbutton(self.root, text="Seleziona tutto", variable=self.selezionaTutto, command=seleziona_tutti)
            self.SelezionaTuttoCheck.grid(row=4, column=0, columnspan=2)

            self.FotoCheck = tk.Checkbutton(self.root, text="Foto", variable=self.Foto)
            self.FotoCheck.grid(row=5, column=0)
            self.VideoCheck = tk.Checkbutton(self.root, text="Video", variable=self.Video)
            self.VideoCheck.grid(row=5, column=1)
            self.DocumentiCheck = tk.Checkbutton(self.root, text="Documenti", variable=self.Documenti)
            self.DocumentiCheck.grid(row=5, column=2)
            self.ExcelCheck = tk.Checkbutton(self.root, text="Excel", variable=self.Excel)
            self.ExcelCheck.grid(row=5, column=3)
            self.PresentazioniCheck = tk.Checkbutton(self.root, text="Presentazioni", variable=self.Presentazioni)
            self.PresentazioniCheck.grid(row=5, column=4)
            self.AspenCheck = tk.Checkbutton(self.root, text="Aspen", variable=self.Aspen)
            self.AspenCheck.grid(row=5, column=5)
            self.AutoCADCheck = tk.Checkbutton(self.root, text="AutoCAD", variable=self.AutoCAD)
            self.AutoCADCheck.grid(row=5, column=6)
            self.AltroCheck = tk.Checkbutton(self.root, text="Altro", variable=self.Altro)
            self.AltroCheck.grid(row=5, column=7)
            # bottone per avviare la funzione
            self.bottoneAvvia = tk.Button(self.root, text="Avvia", command=lambda: self.organizzaFile(self.percorso))
            self.bottoneAvvia.grid(row=6, column=0)

    def organizzaFile(self, percorso):
        # lista dei file presenti nella cartella
        listaFile = os.listdir(percorso)
        for file in listaFile:
            if os.path.isfile(os.path.join(percorso, file)):
                self.SeparazioneFile(percorso, file)
        print("File organizzati")
        self.avviso = tk.Label(self.root, text="File organizzati", fg="green")
        self.avviso.grid(row=5, column=0)
        # Recupera tutte le cartelle presenti nel percorso
        listaCartelle = [d for d in os.listdir(percorso) if os.path.isdir(os.path.join(percorso, d))]
        print(listaCartelle)
        for cartella in listaCartelle:
            self.riordinaFilePerUltimaModifica(os.path.join(percorso, cartella))

    def cambia_icona_cartella(self, percorso_cartella, percorso_icona):
        desktop_ini = os.path.join(percorso_cartella, "desktop.ini")
        with open(desktop_ini, "w") as f:
            f.write("[.ShellClassInfo]\n")
            f.write(f"IconResource={percorso_icona},0\n")
        ctypes.windll.kernel32.SetFileAttributesW(desktop_ini, 0x2 | 0x4)
        ctypes.windll.kernel32.SetFileAttributesW(percorso_cartella, 0x4)
        ctypes.windll.shell32.SHChangeNotify(0x08000000, 0x0000, None, None)

    def SeparazioneFile(self, path, file):
        estensione = file.split(".")[-1]
        mappaEstensioni = {
            "Foto": {"estensioni": ["jpg", "png", "gif"], "icona": r"C:\Users\galloni\OneDrive\Immagini\Icone\foto.ico"},
            "Video": {"estensioni": ["mp4", "avi", "mov"], "icona":r"C:\Users\galloni\OneDrive\Immagini\Icone\video.ico" },
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
                percorso_file = os.path.join(path, file)
                percorso_destinazione = os.path.join(percorsoCartellaDestinazione, file)
                cartella_provenienza = os.path.basename(os.path.dirname(percorso_file))
                print(cartella_provenienza)
                # Controlla se il file è già nella cartella di destinazione
                if cartella_provenienza == cartella:
                    print(f"Il file {file} è già nella cartella {cartella}. Operazione annullata.")
                    return

                # Crea la cartella se non esiste
                if not os.path.exists(percorsoCartellaDestinazione):
                    os.mkdir(percorsoCartellaDestinazione)
                    self.cambia_icona_cartella(percorsoCartellaDestinazione, dati["icona"])

                # Sposta il file nella cartella di destinazione
                os.rename(percorso_file, percorso_destinazione)
                print(f"Spostato il file {file} nella cartella {cartella}.")
                return

        # Se l'estensione non corrisponde a nessuna categoria, sposta nella cartella "Altro"
        if self.Altro.get():
            cartellaDestinazione = "Altro"
            percorsoCartellaDestinazione = os.path.join(path, cartellaDestinazione)
            percorso_file = os.path.join(path, file)
            percorso_destinazione = os.path.join(percorsoCartellaDestinazione, file)

            # Controlla se il file è già nella cartella di destinazione
            if os.path.dirname(percorso_file) == percorsoCartellaDestinazione:
                print(f"Il file {file} è già nella cartella {cartellaDestinazione}. Operazione annullata.")
                return

            # Crea la cartella se non esiste
            if not os.path.exists(percorsoCartellaDestinazione):
                os.mkdir(percorsoCartellaDestinazione)
                self.cambia_icona_cartella(percorsoCartellaDestinazione, mappaEstensioni[cartellaDestinazione]["icona"])

            # Sposta il file nella cartella di destinazione
            os.rename(percorso_file, percorso_destinazione)
            print(f"Spostato il file {file} nella cartella {cartellaDestinazione}.")

    def riordinaFilePerUltimaModifica(self, percorso_cartella):
            # Ottieni la lista dei file nella cartella
            listaFile = [f for f in os.listdir(percorso_cartella) if os.path.isfile(os.path.join(percorso_cartella, f))]
            
            # Ordina i file in base all'ultima modifica
            listaFile.sort(key=lambda x: os.path.getmtime(os.path.join(percorso_cartella, x)))

            # Stampa i file ordinati (puoi modificare questa parte per fare altre operazioni)
            # print(f"File nella cartella {percorso_cartella} ordinati per ultima modifica:")
            # # for file in listaFile:
            # #     print(file)

if __name__ == "__main__":
    root = tk.Tk()
    finestra = Finestra(root)
    finestra.creaFinestra()
    root.mainloop()