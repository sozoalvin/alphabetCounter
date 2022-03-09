import argparse

parser = argparse.ArgumentParser(description='check your string\'s alphabet count')
parser.add_argument('--input', dest='input', type=str, required=True, help='your entire input string')
args = parser.parse_args()

my_dict = {}

for letter in args.input:

    letter = letter.upper()

    # letter will always renew
    if letter == " ":
        letter = "space"

    if letter in my_dict:
        my_dict[letter] += 1
    else:
        my_dict[letter] = 1

for key, value in my_dict.items():
    print("{} : {}".format(key, value))
