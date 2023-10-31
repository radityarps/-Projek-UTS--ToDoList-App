# Fungsi mengetahui tanggal sekarang
import datetime
dateTimeNow = datetime.datetime.now()

# List kosong untuk menyimpan data yang diinput user
toDoList = []


# Fungsi untuk menampilkan daftar tugas
def displayToDoList():
    print("\nTanggal saat ini " + "(" + dateTimeNow.strftime("%d/%m/%Y") + ")")
    print("Daftar Tugas :")
    if toDoList == []:
        print("Tidak ada tugas saat ini.")
    else:
        for i, task in enumerate(toDoList, 1):
            print(f"{i}. {task}")


# Fungsi untuk menambahkan tugas
def addTask(task):
    # Fungsi untuk menambahkan deadline
    def addDeadline():
        addDeadline = input("Berikan deadline? (y/n) : ").lower()
        if addDeadline == "y":
            dateDay = input("Masukkan tanggal deadline : ")
            dateMonth = input("Masukkan bulan deadline : ")
            dateYear = input("Masukkan tahun deadline : ")
            toDoList.append(
                f"{task}, Deadline ({dateDay}/{dateMonth}/{dateYear}).")
        elif addDeadline == "n":
            toDoList.append(task)
        else:
            print("Input salah, seharusya (y/n)")
            toDoList.append(task)
    addDeadline()
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
    print("|" + ("-"*47) + "|\n|\t\tAplikasi To-Do List\t\t|\n" + "|" + ("-"*47) + "|")
    print("|\t1. Tampilkan Daftar Tugas\t\t|")
    print("|\t2. Tambahkan Tugas\t\t\t|")
    print("|\t3. Hapus Tugas\t\t\t\t|")
    print("|\t4. Keluar\t\t\t\t|\n" + "|" + ("-"*47) + "|")

    choice = input("Pilih opsi (1/2/3/4) : ")

    if choice == "1":
        while True:
            displayToDoList()
            doneViewing = input("\nSudah selesai melihat?(y) : ")
            if doneViewing == "y":
                break
    elif choice == "2":
        task = input("Masukkan tugas baru : ")
        addTask(task)
    elif choice == "3":
        if toDoList == []:
            print("\t\tTidak ada tugas saat ini.")
        else:
            displayToDoList()
            index = int(input("Masukkan nomor tugas yang ingin dihapus : "))
            deleteTask(index)
    elif choice == "4":
        print("\nTerima kasih! Aplikasi To-Do List akan ditutup.")
        break
    else:
        print("Opsi tidak valid. Silakan coba lagi.")
