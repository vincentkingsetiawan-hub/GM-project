# Opsi upgrade primer
roti = [
    "roti murah (0)",
    "roti sesame (50)",
    "roti manis (100)",
    "roti donat (150)"
]

daging = [
    "daging sapi (0)",
    "daging ayam (0)",
    "daging ikan (50)",
    "katsu ayam (100)", 
    "sosis (150)"
]

isian = [
    "keju (0)",
    "tomat (0)",
    "selada (50)",
    "bawang (100)",
    "saus tomat (150)",
    "saus tiram (200)"
]

pendamping = [
    "air es (0)",
    "air lemon (50)",
    "soda jeruk (100)",
    "keripik (150)",
    "cheese balls (200)"
]

sudah_diupgrade = [
    "roti murah (0)", 
    "daging sapi (0)", 
    "daging ayam (0)", 
    "keju (0)", 
    "tomat (0)", 
    "air es (0)",
    "kayu (0)",
    "tidak ada (0)",
    "satu mata (0)",
    "kantong plastik (0)"
]

# Opsi upgrade sekunder
meja = [
    "kayu (0)",
    "kayu jati (100)",
    "plastik (200)",
    "logam stainless (300)"
]

kaca_etalase = [
    "tidak ada (0)",
    "kaca murah (200)",
    "kaca akrilik (500)"
]

kompor = [
    "satu mata (0)",
    "dua mata (150)",
    "tiga mata (900)",
    "gas -> listrik (2000)"
]

bungkus = [
    "kantong plastik (0)",
    "kertas (200)",
    "karton (550)"
]

# Opsi marketing
marketing = [
    "mulut ke mulut (0)",
    "brosur (50)",
    "poster (200)",
    "papan iklan (300)",
    "papan LED (400)",
    "iklan TV (600)",
    "iklan medsos (1000)"
]

# Nilai setiap opsi
nilai_upgrade = sudah_diupgrade.count(sudah_diupgrade)
isi_pemasaran = []
nilai_pemasaran = isi_pemasaran.count(isi_pemasaran)

# Fungsi pemasaran
def pemasaran(opsi_pemasaran):
    if opsi_pemasaran not in isi_pemasaran:
        isi_pemasaran.append(opsi_pemasaran)
        print(f"\n--- {opsi_pemasaran} berhasil diterapkan untuk hari ini! ---")
    else:
        print(f"\n--- {opsi_pemasaran} sudah aktif dipakai hari ini! ---")

# Fungsi pembantu untuk menampilkan kategori
def tampilkan_kategori(nama_kategori):
    print("\n--- Daftar Item ---")
    for i, item in enumerate(nama_kategori, start=1):
        if item in sudah_diupgrade:
            print(f"{i}. {item} (Sudah dibeli)")
        else:
            print(f"{i}. {item}")
    print("\n0. Kembali")
    print("Apa yang ingin dibeli?")

    sub_input_1 = input("")
    while True:
        if sub_input_1 == "0":
            break
        elif sub_input_1.isdigit():
            pilihan_angka = int(sub_input_1)

            if 1 <= pilihan_angka <= len(nama_kategori):
                item_terpilih = nama_kategori[pilihan_angka - 1]

                if item_terpilih not in sudah_diupgrade:
                    sudah_diupgrade.append(item_terpilih)
                    print(f"\n--- {item_terpilih} berhasil dibeli! ---")
                else:
                    print(f"\n--- {item_terpilih} sudah ada/pernah dibeli! ---")
        else:
            print("Ketik angka yang benar")




# Fungsi untuk sub-program nomor 1
def fungsi_1():
    while True:
        print(
            "\nSelamat datang di demo game burger stall."
            "\nSilahkan ketik c untuk melanjutkan permainan."
        )
        user_input = input("Pilihan: ")

        if user_input.lower() == "c":
            while True:
                print(
                    "\nOpsi in-game menu Burger Stall"
                    "\n1. Opsi upgrade primer"
                    "\n2. Opsi upgrade sekunder"
                    "\n3. Opsi pemasaran"
                    "\n4. Memulai game"
                    "\n0. Kembali ke menu awal"
                )
                user_input = input("Pilihan menu: ")

                if user_input == "1":
                    while True:
                        print(
                            "\n--- Menu Upgrade Primer ---"
                            "\n1. Roti"
                            "\n2. Daging"
                            "\n3. Isian"
                            "\n4. Pendamping"
                            "\n0. Kembali"
                        )
                        sub_input = input("Pilihan upgrade: ")

                        if sub_input == "1":
                            tampilkan_kategori(roti)
                        elif sub_input == "2":
                            tampilkan_kategori(daging)
                        elif sub_input == "3":
                            tampilkan_kategori(isian)
                        elif sub_input == "4":
                            tampilkan_kategori(pendamping)
                        elif sub_input == "0":
                            break
                        else:
                            print("\nKetik yang benar!!!")

                elif user_input == "2":
                    while True:
                        print(
                            "\n--- Menu Upgrade Sekunder ---"
                            "\n1. Meja"
                            "\n2. Kaca Etalase"
                            "\n3. Kompor"
                            "\n4. Bungkus"
                            "\n0. Kembali"
                        )
                        sub_input = input("Pilihan upgrade: ")

                        if sub_input == "1":
                            tampilkan_kategori(meja)
                        elif sub_input == "2":
                            tampilkan_kategori(kaca_etalase)
                        elif sub_input == "3":
                            tampilkan_kategori(kompor)
                        elif sub_input == "4":
                            tampilkan_kategori(bungkus)
                        elif sub_input == "0":
                            break
                        else:
                            print("\nKetik yang benar!!!")

                            sub_input = input("")

                elif user_input == "3":
                    while True:
                        print("\n--- Menu Pemasaran ---")
                        for i, item in enumerate(marketing, start=1):
                            if item in isi_pemasaran:
                                print(f"{i}. {item} sudah ada untuk dipakai untuk satu hari")
                            else:
                                print(f"{i}. {item}")
                        print("0. Kembali")
                        sub_input = input("Pilihan pemasaran: ")

                        if sub_input == "1":
                            pemasaran("mulut ke mulut (0)")
                        elif sub_input == "2":
                            pemasaran("brosur (50)")
                        elif sub_input == "3":
                            pemasaran("poster (200)")
                        elif sub_input == "4":
                            pemasaran("papan iklan (300)")
                        elif sub_input == "5":
                            pemasaran("papan LED (400)")
                        elif sub_input == "6":
                            pemasaran("iklan TV (600)")
                        elif sub_input == "7":
                            pemasaran("iklan medsos (1000)")
                        elif sub_input == "0":
                            break
                        else:
                            print("\nKetik yang benar!!!")

                            sub_input = input("")

                elif user_input == "4":
                    print("\nMohon maaf tapi gameya masih dalam proses pengembangan~~~")
                elif user_input == "0":
                    break
                else:
                    print("Ketik yang benar!")
        else:
            break

# Program Utama (GM Login)
print("user : root")
user_input = input("password : ")

if user_input == "1234":
    print("\n-----------------------------------------------------------Selamat datang di program GM----------------------------------------------------------------------------------")
    print("Silahkan memilih salah satu dari sub-program yang tersedia~")
    print("1. Burger Stall")
    print("0. keluar")
    user_input = input("Pilihan GM: ")

    if user_input == "1":
        fungsi_1()