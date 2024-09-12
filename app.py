# from PIL import Image

# def convert_jpg_to_ico(source_path, target_path):
#     # Carica l'immagine JPG
#     img = Image.open(source_path)
    
#     # Converti l'immagine in formato ICO
#     img.save(target_path, format='ICO', sizes=[(256, 256)])

# # Percorso del file sorgente JPG e del file destinazione ICO
# source_path = r"C:\Users\galloni\Downloads\Foto\foto.jpg"
# target_path = r"C:\Users\galloni\Downloads\Foto\foto.ico"

# # Chiama la funzione di conversione
# convert_jpg_to_ico(source_path, target_path)

from PIL import Image

def convert_png_to_ico(png_file_path, ico_file_path):
    # Carica l'immagine PNG
    image = Image.open(png_file_path)
    # Converti e salva come ICO
    image.save(ico_file_path, format='ICO')

# Esempio di utilizzo
convert_png_to_ico(r"C:\Users\galloni\Downloads\cart.jpg", r"C:\Users\galloni\Desktop\Altro\Icone\altro.ico")