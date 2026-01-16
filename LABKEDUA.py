kata_rahasia = "jennie"
tebak_huruf = []
kesempatan = 6

print ("Selamat Datang di Hangman 2.0")
print ("Kesempatan Mengisi 6 kali ya")

while kesempatan > 0:
    tampilan_kata = ""

    for huruf in kata_rahasia:
        if huruf in tebak_huruf:
            tampilan_kata += huruf 
        else :
            tampilan_kata += "_"
    print ("Kata:", tampilan_kata)
    print ("Huruf sudah ditebak ya", tebak_huruf)
    print("Kesempatan bersisa:", kesempatan)
    
    if "_" not in tampilan_kata:
        print("yeay, selamat kamu menang!")
        break
    
    tebakan = input("Masukan satu huruf saja: ").lower()
    
    if len(tebakan) != 1 or not tebakan.isalpha():
        print("Input harus satu huruf saja ya")
        continue
    if tebakan in tebak_huruf:
        print("Yah huruf ini sudah ditebak")
        continue 
    tebak_huruf.append(tebakan)
    kesempatan -= 1

if kesempatan == 0:
    print("Permainan Berakhir!")
    print ("Kata yang benar adalah:", kata_rahasia)
