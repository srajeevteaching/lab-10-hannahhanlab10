# Hannah Hodges
# CS 151, Dr. Rajeev
# Lab 10
# 12/2/2021


def main():
    morsecode_dict = load_morse_dict()
    file = input("Enter file to decode:")
    decoded_result = decode_file(file, morsecode_dict)
    print(decoded_result)


def load_morse_dict():
    morsedict = {}
    open("mosecode.txt", "r")
    morsedict = readfile("morsecode.txt")
    lines = readfile.readlines()
    for line in lines:
        key, value = line.split()
        morsedict[key] = value
        return morsedict


def decode_file(file, morsecode_dict):
    code = ''
    morsecode_dict = dict(morsecode_dict)
    open(file)
    for line in file():
        code += line + ''
    decode_val = ''
    letter = ''
    for letter in code:
        counter = 0
        if letter == '':
            letter += letter
        else:
            counter = counter + 1
            if counter == 2:
                decode_val = decode_val + ''
        return decode_val


main()
