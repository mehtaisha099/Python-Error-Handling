try:
    file = open("data.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("Error: File not found")

finally:
    print("File operation completed")