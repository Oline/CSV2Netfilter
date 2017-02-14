#!/usr/bin/env python3

'''This script will convert CSV files (with known format) to a netfilter/iptables-restore file.'''

import sys
import csv
# Getopt
import argparse
# Netfilter functions writer
from nfwriter import write_headers
from nfwriter import write_rules

# Local software information
__version__ = "0.1"
__author__ = "Sylvain Leroy"
myOutput = sys.stdout
inputFileName = "rules.csv"
defaultPolicy = "ACCEPT"

###########################################################################

# parser = argparse.ArgumentParser()
# parser.add_argument("echo", help="echo the string you use here")
# args = parser.parse_args()
# print(args.echo)

#

csvFile = open(inputFileName, 'r')

write_headers(inputFileName, myOutput)

#
rules = csv.DictReader(csvFile, delimiter=';')


# for row in rules:
#     if row['table'] == "filter":


write_rules("filter", rules, myOutput, defaultPolicy, __version__)
# write_rules("nat", rules)
# write_rules("mangle", rules)
# write_rules("raw", rules)

csvFile.close()
