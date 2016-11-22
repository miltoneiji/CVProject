import os
import glob

def findWord(word, files):
    print("Looking for the word: " + word)

    for idx in range(0, len(files)):
        file = open(files[idx], 'r')
        
        text = file.read()
        text = text.lower()
        if text.find(word) != -1:
            print("Image " + files[idx][:-4] + ".jpg contains the word " + word)
            os.system("input\\" + files[idx][:-4] + ".jpg")

        file.close()

if __name__ == "__main__":

    # Parte1: Obtendo os textos das imagens
    # Obtem os textos contidos nas images presentes na pasta input
    # os textos sao nomeados com o mesmo nome das images mas com extensao .txt
    imageNames = glob.glob('input/*.jpg')
    files = []
    for i in range(0, len(imageNames)):
        files.append(imageNames[i][6:-4] + ".txt")
        os.system("tesseract " + imageNames[i] + " " + imageNames[i][6:-4])
        #os.system(imageNames[i][6:-4] + ".txt")
    os.system("cls")
    # Parte2: Busca
    # Pergunta ao usuario que palavra ele busca
    while True:
        print("Enter the word that you are looking for: ")
        word = raw_input('')
        findWord(word, files)
