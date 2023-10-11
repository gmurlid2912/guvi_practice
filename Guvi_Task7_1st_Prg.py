import time

def timestamp():
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S") # Getting the current timestamp
    file_name = f"file-{timestamp}.txt"  # Setting the file name with the timestamp
    with open(file_name, "w") as file:  # Create and write the timestamp into the file
        file.write(timestamp)

if __name__ == "__main__":
    timestamp()
