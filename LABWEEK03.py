def updateText(kata, list_tebakan):
    hasil_tampil = []

    for i in range(len(kata)):
        if kata[i] in list_tebakan:
            hasil_tampil.append(kata[i])
        else:
            hasil_tampil.append("_")

    return hasil_tampil

def main():
    kata_rahasia = "salvatore"
    tebakan = []
    kesempatan = 5 

    print("Selamat Datang di Game Hangman")

    while kesempatan > 0: 
        tampil = updateText(kata_rahasia, tebakan)

        print("Kata:", end=" ")
        for huruf in tampil:
            print(huruf, end=" ")
        print()

        if "_" not in tampil :
            print("Yeay, kamu menang!")
            break

        huruf = input("Masukkan huruf:").lower()

        if huruf in tebakan:
            print("huhu huruf sudah di tebak")
            continue
        tebakan.append(huruf)

        if huruf in kata_rahasia:
            print("yuhu benar!")
        else: 
            kesempatan -= 1
            print("salah deh, sisa kesempatan:", kesempatan)

    else:
        print("Maaf kamu kalah")
        print ("jawabannya adalah", kata_rahasia)

main()
        
