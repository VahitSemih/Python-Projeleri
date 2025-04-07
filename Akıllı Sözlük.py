import json
import difflib

veriler = json.load(open("data.json"))


def kontrol(kelime):
    kelime = kelime.lower()

    if kelime in veriler:
        return veriler[kelime]

    olasi_kelimeler = difflib.get_close_matches(kelime, veriler.keys(), n=1, cutoff=0.8)

    if olasi_kelimeler:
        dogru_kelime = olasi_kelimeler[0]
        cevap = input(f"{kelime} veritabanında bulunamadı. İstediğiniz kelime {dogru_kelime} mi? (E/H): ")
        if cevap.lower() == 'e':
            return veriler[dogru_kelime]
        else:
            return "Bu kelime veritabanında yok."
    else:
        return "Bu kelime veritabanında yok."


print("Kelime aramak için yazın. Çıkmak için 'q' yazın.\n")

while True:
    kelime = input("Enter word: ")

    if kelime.lower() == 'q':
        print("Programdan çıkılıyor...")
        break

    output = kontrol(kelime)

    if type(output) == list:
        for i in output:
            print("-", i)
    else:
        print(output)

    print() # bir satır boşluk için
