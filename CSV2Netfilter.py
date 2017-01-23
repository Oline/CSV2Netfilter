#!/usr/bin/env python3

import csv

with open('rules.csv', newline='') as csvfile:
    rulereader = csv.DictReader(csvfile, delimiter=';')
    for row in rulereader:
        if row['chain']:
            print('-A ' + row['chain'], end=" ")
        if row['protocol']:
            print('-p ' + row['protocol'], end=" ")
        if row['ipsource']:
            print('-s ' + row['ipsource'], end=" ")
        if row['ipdest']:
            print('-d ' + row['ipdest'], end=" ")
        if row['srcport']:
            print('--sport ' + row['srcport'], end=" ")
        if row['destport']:
            print('--dport ' + row['destport'], end=" ")
        if row['rule']:
            print('-j ' + row['rule'])
