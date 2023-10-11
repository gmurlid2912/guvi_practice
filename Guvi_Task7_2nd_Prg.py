file_name = "file2023-10-11_22-35-33.txt"  #declaring the file name
# file_name = "C:\\Users\\muralidharang\\PycharmProjects\\basic_of_python\\file2023-10-11_22-35-33.txt"
def files(file_name):
    try:
        with open(file_name, 'r') as file:
            data = file.read()
            print(data)
    except FileNotFoundError:
        print(f"File '{file_name}' is not present.")


files(file_name)
