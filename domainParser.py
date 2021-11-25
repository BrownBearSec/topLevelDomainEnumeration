from os import sep
import sys

if len(sys.argv) != 3:
    print("bad arguements. usage: python domainParser.py <file> <tld>")
    exit()

dirtyFile = sys.argv[1]
tld = sys.argv[2]


with open(dirtyFile, "r") as f:
    urls = f.readlines()

    for i in urls:
        try:
            seperated = i.split(".")
            #print(seperated)
            seperated = [s.strip() for s in seperated]
            position = seperated.index(tld)
            domain = seperated[position - 1] + f".{tld}\n" 
            #print(domain)

            with open("rootdomains.txt", "a") as output:
                output.write(domain)
        except:
            print(f"I'm tired and cant be asked to catch and clean excemptions, so here they are and do them yourself. Hopefully its not too many:\n {i} ")