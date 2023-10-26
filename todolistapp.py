# List kosong untuk menyimpan data yang diinput user
toDoList = []

# Fungsi untuk menampilkan daftar tugas


def displayToDoList():
    print("\nDaftar Tugas :")
    if toDoList == []:
        print("Tidak ada tugas saat ini.")
    else:
        for i, task in enumerate(toDoList, 1):
            print(f"{i}. {task}")

# Fungsi untuk menambahkan tugas


def addTask(task):
    toDoList.append(task)
    print(f"\nTugas '{task}' telah ditambahkan.")

# Fungsi untuk menghapus tugas


def deleteTask(index):
    if 1 <= index <= len(toDoList):
        task = toDoList.pop(index - 1)
        print(f"\nTugas '{task}' telah dihapus.")
    else:
        print("\nIndeks tugas tidak ada.")


# Loop menampilkan menu aplikasi
while True:
    print("\nAplikasi To-Do List")
    print("1. Tampilkan Daftar Tugas")
    print("2. Tambahkan Tugas")
    print("3. Hapus Tugas")
    print("4. Keluar")

    choice = input("Pilih opsi (1/2/3/4) : ")

    if choice == "1":
        displayToDoList()
    elif choice == "2":
        task = input("Masukkan tugas baru : ")
        addTask(task)
    elif choice == "3":
        displayToDoList()
        index = int(input("Masukkan nomor tugas yang ingin dihapus : "))
        deleteTask(index)
    elif choice == "4":
        print("\nTerima kasih! Aplikasi To-Do List akan ditutup.")
        break
    else:
        print("Opsi tidak valid. Silakan coba lagi.")
