with open("data.txt", "r") as f:

    for baris in f:

        angka = int(baris.strip())
        if angka % 2 == 0:
            print("genap")
        else:
            print("ganjil")
