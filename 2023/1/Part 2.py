import os

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to the file
file_path = os.path.join(script_dir, "test.txt")

# Now open the file
try:
    file = open(file_path, "r")
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")


def replace_string_with_digits(string):
    tempstring = ""
    length = len(string)

    # The right calibration values for string "eighthree" is 83 and for "sevenine" is 79.
    # We replace each occurence of the word with the digit and leave the last letter.

    # iterate through the string and check if the string contains any of the words
    for i in range(length):
        tempstring += string[i]
        status = string_matcher(tempstring)
        match status:
            case 1:
                tempstring = tempstring.replace("one", "1e")
            case 2:
                tempstring = tempstring.replace("two", "2o")
            case 3:
                tempstring = tempstring.replace("three", "3e")
            case 4:
                tempstring = tempstring.replace("four", "4r")
            case 5:
                tempstring = tempstring.replace("five", "5e")
            case 6:
                tempstring = tempstring.replace("six", "6x")
            case 7:
                tempstring = tempstring.replace("seven", "7n")
            case 8:
                tempstring = tempstring.replace("eight", "8t")
            case 9:
                tempstring = tempstring.replace("nine", "9e")

    return tempstring


def string_matcher(string):
    # check if the string contains any of the words
    if string.find("one") != -1:
        return 1
    elif string.find("two") != -1:
        return 2
    elif string.find("three") != -1:
        return 3
    elif string.find("four") != -1:
        return 4
    elif string.find("five") != -1:
        return 5
    elif string.find("six") != -1:
        return 6
    elif string.find("seven") != -1:
        return 7
    elif string.find("eight") != -1:
        return 8
    elif string.find("nine") != -1:
        return 9
    else:
        return -1


result = 0
for line in file.readlines():
    line = line.strip()

    print(line)
    line = replace_string_with_digits(line)
    print(line)

    for char in line:
        if char.isalpha() or char.isspace():
            line = line.replace(char, "")
    print(line)

    temp_result = 0
    if len(line) == 1:
        temp_result = int(line) * 11
    else:
        temp_result = int(line[0]) * 10 + int(line[-1:])
    print(temp_result)
    result += temp_result

print(result)
