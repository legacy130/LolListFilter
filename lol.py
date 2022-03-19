import os
Region = input("Choose your region : ")
file_name = input("File Name ? : ")

with open(file_name, "r") as input:
    with open("editedfile.txt", "w") as output:
        # iterate all lines from file
        for line in input:
            # if substring contain in a line then don't write it
            if Region in line.strip("\n"):
                output.write(line)

# replace file with original name

