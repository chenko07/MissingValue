import csv

def read_csv(filename):
    with open(filename, 'r') as file:
        # Menampung objetk CSV atau file CSV
        csv_reader = csv.reader(file)
        # Melakukan pembacaan file
        header = next(csv_reader)
        # Menangkap list kosong dari CSV 
        data = []
        # Perua=langan untuk membaca file CSV
        for row in csv_reader:
            data.append(row)
    return header, data
    
#fungsi yang menampilkan data CSV
def tampilkan_data(data):
    for row in data:
        print(row)

#fungsi yang menampilkan missing_values (menghitung missing values)
def modifikasi_data(data, missing_values):
    for row in data:
        for i, value in enumerate(row):
            if value in missing_values:
                row[i] = None
    return data

#fungsi untuk mengecek nilai null
def check_null(data):
    null_count = 0
    for row in data:
        for value in row:
            if value is None:
                null_count += 1
    if null_count == 0:
        print("Tidak ada nilai null dalam data.")
    else:
        print(f"Total nilai null: {null_count}")

#fungsi untuk mengecek kolom null
def check_column_null(data, column_number, header):
    null_count = 0
    for row in data:
        if row[column_number-1] is None:
            null_count += 1
    print(f"Total nilai null pada kolom {header[column_number-1]}: {null_count}")
    
#fungsi utama dalam pemanggilan menu dan fungsi yang sudah dibuat
def main():
    filename = input("Masukkan nama file CSV: ") #dapat memasukkan nilai pada CSV yang dipilih 
    header, data = read_csv(filename)
    while True:
        print("\nMenu:")
        print("a. Tampilkan data asli")
        print("b. Tampilkan data modif")
        print("c. Mengecek null secara keseluruhan")
        print("d. Menghitung jumlah total null")
        print("e. Membaca perkolom dengan inputan user")
        print("f. Membaca perkolom dengan inputan user")
        print("q. Keluar")

        choice = input("Pilih menu: ") #inputan dengan validasi pada masing-masing cabang while
        if choice == 'a':
            tampilkan_data(data)
        
        elif choice == 'b':
            modified_data = modifikasi_data(data, ["--", "?"])
            tampilkan_data(modified_data)
        
        elif choice == 'c':
            check_null(data)
        
        elif choice == 'd':
            null_count = sum(row.count(None) for row in data)
            print(f"Total nilai null: {null_count}")
        

        elif choice == 'e':
            print("Kolom yang tersedia:")
            for i, col in enumerate(header):
                print(f"{i+1}. {col}")
            while True:
                column_choice = input("Pilih nomor kolom yang ingin dicek: ")
                try:
                    column_number = int(column_choice)
                    if column_number >= 1 and column_number <= len(header):
                        break
                    else:
                        print("Nomor kolom tidak valid.")
                except ValueError:
                    print("Input tidak valid.")
            check_column_null(data, column_number, header)
       

        elif choice == 'f':
          while True:
            input_nilai = input("masukan nilai yang ingin kamu ganti: ")
            
        elif choice == 'q':
            break
        else:
            print("Menu tidak valid. Silakan coba lagi.")

if __name__ == '__main__':
    main()    
