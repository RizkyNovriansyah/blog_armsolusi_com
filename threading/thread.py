import threading
import time

# Menyiapkan fungsi yang akan dieksekusi pada thread
def print_numbers(numbers):
    for i in numbers:
        print(f"Number {i}")
        time.sleep(1)

def print_letters(letters):
    for letter in letters:
        print(f"Letter {letter}")
        time.sleep(2)

# Membuat data yang akan diproses
numbers = [1, 2, 3, 4, 5]
letters = "abcde"

# Membuat dua thread
thread1 = threading.Thread(target=print_numbers, args=[numbers])
thread2 = threading.Thread(target=print_letters, args=[letters])

# Memulai kedua thread
thread1.start()
thread2.start()

# Menunggu kedua thread selesai
thread1.join()
thread2.join()
print("Selesai")