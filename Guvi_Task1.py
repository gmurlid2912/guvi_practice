#name = input("Enter the name:-")
name = "Guvi Geeks Network Private Limited"
name = name.lower()   # Convert the given name to lowercase
print(name)
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0
for char in name:  # checking the vowels in the given name
    if char == 'a':
        count_a += 1
    elif char == 'e':
        count_e += 1
    elif char == 'i':
        count_i += 1
    elif char == 'o':
        count_o += 1
    elif char == 'u':
        count_u += 1
total_vowels = count_a + count_e + count_i + count_o + count_u # calculating the no. of vowels
print("Total number of vowels:", total_vowels)
print("Count of 'A':", count_a)
print("Count of 'E':", count_e)
print("Count of 'I':", count_i)
print("Count of 'O':", count_o)
print("Count of 'U':", count_u)
