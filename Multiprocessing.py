import multiprocessing
import time

# Define a function to be executed in a separate process
def print_numbers():
    for i in range(50):
        print(f"Number: {i}")
        time.sleep(0.1)  # Simulate a delay

# Define another function to be executed in a separate process
def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(f"Letter: {letter}")  
        time.sleep(0.1)  # Simulate a different delay

if __name__ == "__main__":
    # Create processes
    process1 = multiprocessing.Process(target=print_numbers)
    process2 = multiprocessing.Process(target=print_letters)

    # Start processes
    process1.start()
    process2.start()

    # Wait for both processes to complete
    process1.join()
    process2.join()

    print("Both processes have completed.")
