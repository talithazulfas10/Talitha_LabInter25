Rahasia = "jennie"
Tebak = input("Tebak salah satu huruf:"). lower()

if len(Tebak) != 1:
    print ("Masukin satu huruf aja coba")
if Tebak in Rahasia: 
    print ("yeay benar!")
else :
    print ("yah tidak ada, ayo coba lagi!")