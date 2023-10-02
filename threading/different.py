import threading
import time

# Fungsi
def print_numbers(numbers):
    for i in numbers:
        print(f"Number {i}")
        time.sleep(1)

# Argument
numbers = [1, 2, 3, 4, 5]

# Sebelum menggunakan thread
print_numbers(numbers)

# Sesudah menggunakan thread
thread = threading.Thread(target=print_numbers, args=[numbers])
thread.start()