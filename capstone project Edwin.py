from tabulate import tabulate

# Data siswa
students = [
    {"NIS": "20001", "Nama": "Indah", "Kelas": "10A", "Jurusan": "IPA", "Jenis Kelamin": "Perempuan", "Nilai Rata-rata": 80},
    {"NIS": "20002", "Nama": "Budi", "Kelas": "10B", "Jurusan": "IPS", "Jenis Kelamin": "Laki-laki", "Nilai Rata-rata": 50},
    {"NIS": "20003", "Nama": "Andi", "Kelas": "10C", "Jurusan": "IPA", "Jenis Kelamin": "Laki-laki", "Nilai Rata-rata": 90},
    {"NIS": "20004", "Nama": "Susi", "Kelas": "10A", "Jurusan": "IPS", "Jenis Kelamin": "Perempuan", "Nilai Rata-rata": 30},
    {"NIS": "20005", "Nama": "Alfonzo", "Kelas": "10B", "Jurusan": "IPA", "Jenis Kelamin": "Laki-laki", "Nilai Rata-rata": 90},
    {"NIS": "20006", "Nama": "Anita", "Kelas": "10C", "Jurusan": "IPS", "Jenis Kelamin": "Perempuan", "Nilai Rata-rata": 70},
    {"NIS": "20007", "Nama": "Santoso", "Kelas": "10A", "Jurusan": "IPS", "Jenis Kelamin": "Perempuan", "Nilai Rata-rata": 70},
    {"NIS": "20008", "Nama": "Dewi", "Kelas": "10A", "Jurusan": "IPA", "Jenis Kelamin": "Perempuan", "Nilai Rata-rata": 85},
    {"NIS": "20009", "Nama": "Rizky", "Kelas": "10B", "Jurusan": "IPS", "Jenis Kelamin": "Laki-laki", "Nilai Rata-rata": 60},
    {"NIS": "20010", "Nama": "Joko", "Kelas": "10C", "Jurusan": "IPA", "Jenis Kelamin": "Laki-laki", "Nilai Rata-rata": 95},
    {"NIS": "20011", "Nama": "Citra", "Kelas": "10A", "Jurusan": "IPS", "Jenis Kelamin": "Perempuan", "Nilai Rata-rata": 40},
    {"NIS": "20012", "Nama": "Bayu", "Kelas": "10B", "Jurusan": "IPA", "Jenis Kelamin": "Laki-laki", "Nilai Rata-rata": 75},
    {"NIS": "20013", "Nama": "Siti", "Kelas": "10C", "Jurusan": "IPS", "Jenis Kelamin": "Perempuan", "Nilai Rata-rata": 65},
    {"NIS": "20014", "Nama": "Arif", "Kelas": "10A", "Jurusan": "IPA", "Jenis Kelamin": "Laki-laki", "Nilai Rata-rata": 55},
    {"NIS": "20015", "Nama": "Melati", "Kelas": "10B", "Jurusan": "IPS", "Jenis Kelamin": "Perempuan", "Nilai Rata-rata": 88},
    {"NIS": "20016", "Nama": "Doni", "Kelas": "10C", "Jurusan": "IPA", "Jenis Kelamin": "Laki-laki", "Nilai Rata-rata": 92},
    {"NIS": "20017", "Nama": "Lina", "Kelas": "10A", "Jurusan": "IPS", "Jenis Kelamin": "Perempuan", "Nilai Rata-rata": 72},
    {"NIS": "20018", "Nama": "Tono", "Kelas": "10B", "Jurusan": "IPA", "Jenis Kelamin": "Laki-laki", "Nilai Rata-rata": 68},
    {"NIS": "20019", "Nama": "Yulia", "Kelas": "10C", "Jurusan": "IPS", "Jenis Kelamin": "Perempuan", "Nilai Rata-rata": 78},
    {"NIS": "20020", "Nama": "Kevin", "Kelas": "10A", "Jurusan": "IPA", "Jenis Kelamin": "Laki-laki", "Nilai Rata-rata": 83}
]
# Fungsi untuk mencari siswa berdasarkan NIS
def cari_siswa(nis):
    for student in students:
        if student["NIS"] == nis:
            return student
    return None

#Fungsi untuk menampilkan data dalam table
def tampilkan_data_tabel(data):
    if not data:
        print("Tidak ada data yang ditemukan.")
        return

    headers = ["NIS", "Nama", "Kelas", "Jurusan", "Jenis Kelamin", "Nilai Rata-rata"]
    rows = [[s["NIS"], s["Nama"], s["Kelas"], s["Jurusan"], s["Jenis Kelamin"], s["Nilai Rata-rata"]] for s in data]
    print(tabulate(rows, headers=headers, tablefmt="grid"))

# Fungsi untuk menampilkan data siswa
def tampilkan_data():
    while True:
        print("\nMenu Tampilkan Data:")
        print("1. Tampilkan semua data siswa")
        print("2. Cari siswa berdasarkan NIS")
        print("3. Cari siswa berdasarkan Jurusan")
        print("4. Cari siswa berdasarkan Kelas")
        print("5. Cari siswa berdasarkan Jenis Kelamin")
        print("6. Tampilkan data siswa yang urut")
        print("7. Tampilkan siswa yang lulus (nilai rata-rata >= 75)")
        print("8. Tampilkan nilai rata-rata siswa per kelas atau jurusan")
        print("9. Tampilkan nilai tertinggi siswa")
        print("10. Kembali ke Menu Utama")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            # Tampilkan semua data siswa
            if not students:
                print("Belum ada data siswa.")
            else:
                print("\nDaftar Semua Siswa:")
                table_siswa = tabulate(students,headers = "keys", tablefmt="grid")
                print(table_siswa)

        elif pilihan == "2":
            # Cari siswa berdasarkan NIS
            nis = input("Masukkan NIS siswa yang ingin dicari: ")
            siswa = cari_siswa(nis)
            if siswa:
                print("\nData Siswa Ditemukan:")
                table = tabulate([siswa], headers="keys", tablefmt="grid")
                print(table)
            else:
                print("Siswa dengan NIS tersebut tidak ditemukan.")
        elif pilihan == "3":
            # Cari siswa berdasarkan jurusan
            jurusan = input("Masukkan jurusan: ").upper()
            filtered_students = list(filter(lambda x: x["Jurusan"] == jurusan, students))
            tampilkan_data_tabel(filtered_students)
        elif pilihan == "4":
            # Cari siswa berdasarkan kelas
            kelas = input("Masukkan kelas: ").upper()
            filtered_students = list(filter(lambda x: x["Kelas"] == kelas, students))
            tampilkan_data_tabel(filtered_students)
        elif pilihan == "5":
            # Cari siswa berdasarkan jenis kelamin
            kelamin = input("Masukkan jenis kelamin (Laki-laki/Perempuan): ").strip().capitalize()
            filtered_students = list(filter(lambda x: x["Jenis Kelamin"] == kelamin, students))
            tampilkan_data_tabel(filtered_students)
        
        elif pilihan == "6":
            # Mengurutkan siswa
            print("\nPilih kriteria:")
            print("1. Berdasarkan Nama")
            print("2. Berdasarkan Nilai Rata-rata")
            kriteria = input("Pilih menu: ")
            if kriteria == "1":
                sorted_students = sorted(students, key=lambda x: x["Nama"])
            elif kriteria == "2":
                sorted_students = sorted(students, key=lambda x: x["Nilai Rata-rata"])
            else:
                print("Pilihan tidak valid")
                return
            tampilkan_data_tabel(sorted_students) 
             

        elif pilihan == "7":
            # Tampilkan siswa yang lulus (nilai rata-rata >= 75)
            siswa_lulus = list(filter(lambda x: x["Nilai Rata-rata"] >= 75, students))
            if siswa_lulus:
                print("\nDaftar Siswa yang Lulus:")
                tampilkan_data_tabel(siswa_lulus)
            else:
                print("Tidak ada siswa yang lulus.")

        elif pilihan == "8":
            # Tampilkan nilai rata-rata siswa per kelas atau jurusan
            print("\nPilih kriteria:")
            print("1. Per Kelas")
            print("2. Per Jurusan")
            kriteria = input("Pilih menu: ")

            if kriteria == "1":
                # Hitung nilai rata-rata per kelas
                kelas_nilai = {}
                for s in students:
                    if s["Kelas"] in kelas_nilai:
                        kelas_nilai[s["Kelas"]].append(s["Nilai Rata-rata"])
                    else:
                        kelas_nilai[s["Kelas"]] = [s["Nilai Rata-rata"]]
                print("\nNilai Rata-rata per Kelas:")
                for kelas, nilai in kelas_nilai.items():
                    rata_rata = sum(nilai) / len(nilai)
                    print(f"{kelas}: {rata_rata:.2f}") #format 2 angka desimal

            elif kriteria == "2":
                # Hitung nilai rata-rata per jurusan
                jurusan_nilai = {}
                for s in students:
                    if s["Jurusan"] in jurusan_nilai:
                        jurusan_nilai[s["Jurusan"]].append(s["Nilai Rata-rata"])
                    else:
                        jurusan_nilai[s["Jurusan"]] = [s["Nilai Rata-rata"]]
                print("\nNilai Rata-rata per Jurusan:")
                for jurusan, nilai in jurusan_nilai.items():
                    rata_rata = sum(nilai) / len(nilai)
                    print(f"{jurusan}: {rata_rata:.2f}")

            else:
                print("Pilihan tidak valid.")

        elif pilihan == "9":
            # Lihat siswa dengan nilai tertinggi berdasarkan jurusan/kelas
            print("\nPilih kriteria:")
            print("1. Berdasarkan Jurusan")
            print("2. Berdasarkan Kelas")
            kriteria = input("Pilih menu: ")

            if kriteria == "1":
                # Cari siswa dengan nilai tertinggi per jurusan
                jurusan_nilai_tertinggi = {}
                for s in students:
                    if s["Jurusan"] not in jurusan_nilai_tertinggi or s["Nilai Rata-rata"] > jurusan_nilai_tertinggi[s["Jurusan"]]["Nilai Rata-rata"]:
                        jurusan_nilai_tertinggi[s["Jurusan"]] = s
                print("\nSiswa dengan Nilai Tertinggi per Jurusan:")
                tampilkan_data_tabel(jurusan_nilai_tertinggi.values())

            elif kriteria == "2":
                # Cari siswa dengan nilai tertinggi per kelas
                kelas_nilai_tertinggi = {}
                for s in students:
                    if s["Kelas"] not in kelas_nilai_tertinggi or s["Nilai Rata-rata"] > kelas_nilai_tertinggi[s["Kelas"]]["Nilai Rata-rata"]:
                        kelas_nilai_tertinggi[s["Kelas"]] = s
                print("\nSiswa dengan Nilai Tertinggi per Kelas:")
                tampilkan_data_tabel(kelas_nilai_tertinggi.values())

            else:
                print("Pilihan tidak valid.")

        elif pilihan == "10":
            # Kembali ke Menu Utama
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Fungsi untuk menambahkan siswa baru
def tambah_siswa():
    nis = input("Masukkan NIS: ")
    if cari_siswa(nis):
        print("Data sudah ada.")
        return
    nama = input("Masukkan Nama: ")
    kelas = input("Masukkan Kelas: ")
    jurusan = input("Masukkan Jurusan: ")
    jenis_kelamin = input("Masukkan Jenis Kelamin (Laki-laki/Perempuan) :  ")
    nilai_rata_rata = int(input("Masukkan Nilai Rata-rata: "))

    confirm = input("Lanjut menambahkan? (yes/no): ").lower()
    if confirm == "yes":
        students.append({"NIS": nis, "Nama": nama, "Kelas": kelas, "Jurusan": jurusan, "Jenis Kelamin": jenis_kelamin, "Nilai Rata-rata": nilai_rata_rata})
        print("Data sudah disaved.")
    else:
        print("Penambahan dibatalkan.")
    



# Fungsi untuk mengupdate data siswa
def update_siswa():
    nis = input("Masukkan NIS siswa yang ingin diupdate: ")
    data_siswa = cari_siswa(nis)
    if not data_siswa:
        print("Data siswa tidak ada")
        return
    else:
        print("\nData Siswa Ditemukan:")
        tampilkan_data_tabel([data_siswa])

    # Tanyakan apakah ingin melanjutkan pembaruan (dipindahkan ke sini)
    update = input("Apakah Anda ingin melanjutkan pembaruan? (yes/no): ").lower()
    if update != "yes":
        print("Pembaruan dibatalkan.")
        return

    # Jika pengguna memilih "yes", lanjutkan dengan pembaruan
    kolom = input("Masukkan kolom yang ingin diupdate (Nama, Kelas, Jurusan, Jenis Kelamin, Nilai Rata-rata): ").capitalize()
    if kolom not in data_siswa:
        print("Kolom tidak valid.")
        return
    nilai_baru = input(f"Masukkan {kolom} baru: ")
    if kolom == "Nilai Rata-rata":
        nilai_baru = int(nilai_baru)

    # Tanyakan konfirmasi sebelum melakukan pembaruan
    confirm = input("Apa Anda ingin mengudapte data? (yes/no): ").lower()
    if confirm == "yes":
        data_siswa[kolom] = nilai_baru
        print("Data sudah diupdate.")
    else:
        print("Pembaruan dibatalkan.")

# Fungsi untuk menghapus data siswa
def hapus_siswa():
    nis = input("Masukkan NIS siswa yang ingin dihapus: ")
    siswa = cari_siswa(nis)
    if not siswa:
        print("Data siswa tidak ada.")
        return

    # Tampilkan data siswa yang akan dihapus
    print("\nData Siswa yang Akan Dihapus:")
    tampilkan_data_tabel([siswa])

    # Tanyakan konfirmasi penghapusan
    confirm_delete = input("Apakah Anda yakin ingin menghapus data ini? (yes/no): ").lower()
    if confirm_delete == "yes":
        students.remove(siswa)
        print("Data sukses dihapus.")
    else:
        print("Penghapusan data dibatalkan.")


# Menu utama
def menu_utama():
    while True:
        print("\nMenu Utama:")
        print("1. Lihat Siswa")
        print("2. Tambah Siswa")
        print("3. Update Siswa")
        print("4. Hapus Siswa")
        print("5. Keluar")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            tampilkan_data()
        elif pilihan == "2":
            tambah_siswa()
        elif pilihan == "3":
            update_siswa()
        elif pilihan == "4":
            hapus_siswa()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Jalankan program
menu_utama()