import os
import tkinter as tk
from tkinter import filedialog

class Finestra():
    def __init__(self,root):
        self.root = root
        self.root.title("Organizzatore File")
        self.root.geometry("800x300")

    def creaFinestra(self):
        self.titolo = tk.Label(self.root, text="Organizzatore File", font=("Arial", 20, "bold"), fg="green")
        self.titolo.grid(row=0,column=0,columnspan=2)
        #spazio
        self.spazio=tk.Label(self.root,text="")
        self.spazio.grid(row=1,column=1)
        #bottone sfoglia per il percorso
        self.bottoneSfoglia=tk.Button(self.root,text="Sfoglia",command=self.scegliPercorso)
        self.bottoneSfoglia.grid(row=2,column=0)
        
        
    def scegliPercorso(self):
        self.percorso=tk.filedialog.askdirectory()
        self.Foto=tk.IntVar()
        self.Video=tk.IntVar()
        self.Documenti=tk.IntVar()
        self.Excel=tk.IntVar()
        self.Presentazioni=tk.IntVar()
        self.Aspen=tk.IntVar()
        self.AutoCAD=tk.IntVar()
        self.Altro=tk.IntVar()
            
        if self.percorso:
            self.percorsoLabel=tk.Label(self.root,text="Percorso selezionato: "+self.percorso)
            self.percorsoLabel.grid(row=3,column=0,columnspan=5)
            #checkbox per espire le preferenze delle cartelle da creare
            self.FotoCheck=tk.Checkbutton(self.root,text="Foto",variable=self.Foto)
            self.FotoCheck.grid(row=4,column=0)
            self.VideoCheck=tk.Checkbutton(self.root,text="Video",variable=self.Video)
            self.VideoCheck.grid(row=4,column=1)
            self.DocumentiCheck=tk.Checkbutton(self.root,text="Documenti",variable=self.Documenti)
            self.DocumentiCheck.grid(row=4,column=2)
            self.ExcelCheck=tk.Checkbutton(self.root,text="Excel",variable=self.Excel)
            self.ExcelCheck.grid(row=4,column=3)
            self.PresentazioniCheck=tk.Checkbutton(self.root,text="Presentazioni",variable=self.Presentazioni)
            self.PresentazioniCheck.grid(row=4,column=4)
            self.AspenCheck=tk.Checkbutton(self.root,text="Aspen",variable=self.Aspen)
            self.AspenCheck.grid(row=4,column=5)
            self.AutoCADCheck=tk.Checkbutton(self.root,text="AutoCAD",variable=self.AutoCAD)
            self.AutoCADCheck.grid(row=4,column=6)
            self.AltroCheck=tk.Checkbutton(self.root,text="Altro",variable=self.Altro)
            self.AltroCheck.grid(row=4,column=7)
            #bottone per avviare la funzione
            self.bottoneAvvia=tk.Button(self.root,text="Avvia",command=lambda:self.organizzaFile(self.percorso))
            self.bottoneAvvia.grid(row=5,column=0)

    def organizzaFile(self,percorso):
        #lista dei file presenti nella cartella
        listaFile=os.listdir(percorso)
        for file in listaFile:
            if os.path.isfile(percorso+"\\"+file):
                self.SeparazioneFile(percorso,file)
        print("File organizzati")
        self.avviso=tk.Label(self.root,text="File organizzati",fg="green")
        self.avviso.grid(row=5,column=0)

    def SeparazioneFile(self,path,file):
        # in base all'estensione del file dividi in cartelle tipo: Foto, Video, Documenti, Altro
        estensione=file.split(".")[1]
        if estensione in ["jpg","png","gif"]:
            if self.Foto.get():
                if not os.path.exists(path+"\\Foto"):
                    os.mkdir(path+"\\Foto")
                    #sposta il file
                    os.rename(path+"\\"+file,path+"\\Foto\\"+file)
        elif estensione in ["mp4","avi","mov"]:
            if self.Video.get():
                if not os.path.exists(path+"\\Video"):
                    os.mkdir(path+"\\Video")
                    #sposta il file
                    os.rename(path+"\\"+file,path+"\\Video\\"+file)
        elif estensione in ["doc","docx","pdf","txt","tex"]:
            if self.Documenti.get():
                if not os.path.exists(path+"\\Documenti"):
                    os.mkdir(path+"\\Documenti")
                    #sposta il file
                    os.rename(path+"\\"+file,path+"\\Documenti\\"+file)
        elif estensione in ["xls","xlsx","csv"]:
            if self.Excel.get():
                if not os.path.exists(path+"\\Excel"):
                    os.mkdir(path+"\\Excel")
                    #sposta il file
                    os.rename(path+"\\"+file,path+"\\Excel\\"+file)
        elif estensione in ["ppt","pptx"]:
            if self.Presentazioni.get():
                if not os.path.exists(path+"\\Presentazioni"):
                    os.mkdir(path+"\\Presentazioni")
                    #sposta il file
                    os.rename(path+"\\"+file,path+"\\Presentazioni\\"+file)
        elif estensione in ["apwz","apw"]:
            if self.Aspen.get():
                if not os.path.exists(path+"\\Aspen"):
                    os.mkdir(path+"\\Aspen")
                    #sposta il file
                    os.rename(path+"\\"+file,path+"\\Aspen\\"+file)
        elif estensione in ["dwg","dxf"]:
            if self.AutoCAD.get():
                if not os.path.exists(path+"\\AutoCAD"):
                    os.mkdir(path+"\\AutoCAD")
                    #sposta il file
                    os.rename(path+"\\"+file,path+"\\AutoCAD\\"+file)
        else:
            if self.Altro.get():
                if not os.path.exists(path+"\\Altro"):
                    os.mkdir(path+"\\Altro")
                    #sposta il file
                    os.rename(path+"\\"+file,path+"\\Altro\\"+file)


if __name__ == "__main__":
    root = tk.Tk()
    finestra = Finestra(root)
    finestra.creaFinestra()
    root.mainloop()