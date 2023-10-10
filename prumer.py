import sys

def prumer():
    soucet = 0
    for cislo in sys.argv[1:]:
        soucet += int(cislo)
    print(soucet/len(sys.argv[1:]))

prumer()
