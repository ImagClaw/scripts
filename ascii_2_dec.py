import math, argparse

parser = argparse.ArgumentParser()
parser.add_argument("--phrase", action='store', dest='phrase', help="Enter the phrase you want converted to Decimal", required=True)
args = parser.parse_args()

phrase = []

for i in args.phrase:
    phrase.append(ord(i))

print(phrase)