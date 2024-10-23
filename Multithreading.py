import threading
import time

# Define a function to be executed in a thread
def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        # time.sleep(1)  # Simulate a delay

# Define another function to be executed in a thread
def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(f"Letter: {letter}")
        # time.sleep(0.5)  # Simulate a different delay

# Create threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start threads
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()

print("Both threads have completed.")
