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

# Memanggil fungsi yang akan dieksekusi
print_numbers(numbers)
print_letters(letters)

print("Selesai")

# check berapa lama waktu yang dibutuhkan untuk mengeksekusi program
# $ time python3 threading/nonthread.py 