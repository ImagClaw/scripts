 #!/usr/bin/env python3
#
# Author: dal.whelpley@gmail.com
#
# This script is used to convert ascii to decimal 
#
# I.E. A == 065

import math, argparse

parser = argparse.ArgumentParser()
parser.add_argument("--phrase", action='store', dest='phrase', help="Enter the phrase you want converted to Decimal", required=True)
args = parser.parse_args()

phrase = []

for i in args.phrase:
    phrase.append(ord(i))

print(phrase)