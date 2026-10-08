# Opsi upgrade
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
    "katsu ayam (100)", # Koma sudah ditambahkan di sini
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
    "air es (0)"
]

# Opsi gaya
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

# Fungsi pembantu untuk menampilkan kategori upgrade dengan rapi
def tampilkan_kategori(nama_kategori):
    print("\n--- Daftar Item ---")
    for item in nama_kategori:
        if item in sudah_diupgrade:
            print(f"- {item} (Sudah dibeli)")
        else:
            print(f"- {item}")
    print("\nApa yang ingin dibeli?")

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
                    "\n1. Opsi upgrade"
                    "\n2. Opsi gaya restoran"
                    "\n3. Opsi pemasaran"
                    "\n0. Kembali ke menu awal"
                )
                user_input = input("Pilihan menu: ")

                if user_input == "1":
                    while True:
                        print(
                            "\n--- Menu Upgrade ---"
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
                            print("Pilihan tidak valid, silakan coba lagi.")

                elif user_input == "2":
                    print("\n[Fitur Opsi Gaya Restoran belum dibuat]")
                elif user_input == "3":
                    print("\n[Fitur Opsi Pemasaran belum dibuat]")
                elif user_input == "0":
                    break
                else:
                    print("Ketik yang benar interaksinya!")
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