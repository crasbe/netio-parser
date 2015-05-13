#! /usr/bin/python3
""" netio-parser.py

parses the output of a batch of netio-results
Author: crasbe, 01.10.2014
"""

import sys

import libs.parse

#def addtable(swidth, txwidth, rxwidth, svalue='', txvalue='', rxvalue='', \
#            sep="|"):
#    """ a little function to help with the table
#    
#    swidth  - with of the size column
#    svalue - value for the size column
#    txwidth,txvalue,... the same
#    """
    
#    print("{:<{space}}{}".format(svalue, sep, space=swidth),end="")
#    print("{:^{space}}{}".format(txvalue, sep, space=txwidth),end="")
#    print("{:^{space}}{}".format(rxvalue, sep, space=rxwidth))    


#RX = {  "1k"    : [], "2k"    : [], "4k"    : [],    # result buffer
#        "8k"    : [], "16k"   : [], "32k"   : [] }

#TX = {  "1k"    : [], "2k"    : [], "4k"    : [],
#        "8k"    : [], "16k"   : [], "32k"   : [] }


if(len(sys.argv) != 2):
    sys.exit("Usage: netio-parser.py input.txt")
    
inputfile = open(sys.argv[1], "r")
netioinput = inputfile.read()
inputfile.close()

linesplit = netioinput.split("\n") # declaration of "lines"

parser = libs.parse.Parse(linesplit)

parser.calculate()
print(parser.average("TX", "1k"))

#invalid = 0
#for line in linesplit:
#    if(not "Packet size" in line):
#        continue
#    
    # example: "Packet size  1k bytes:  57.08 KByte/s Tx,  31.73 KByte/s Rx."
#    tmp = line.rsplit("  ",2)            # ['Packet size  1k bytes:', '57.08 KByte/s Tx,', '31.73 KByte/s Rx.']
#    if(len(tmp) != 3 or not "Rx" in tmp[-1]):
#        invalid += 1
#        continue
    
#    txtmp = tmp[1].split(" ")[0]         # '57.08'
#    rxtmp = tmp[2].split(" ")[0]         # '31.73'
#    
#    packetsize = tmp[0].rsplit(" ",2)[1] # '1k'
    
#    TX[packetsize].append(float(txtmp))
#    RX[packetsize].append(float(rxtmp))

#sys.exit()
    
print("NETIO-Speedresults")
print("------------------")
print("Datasets: {}".format(linesplit.count("Done.")))
print(" - invalid: {}".format(invalid))
print(" - TCP: {}".format(linesplit.count("TCP connection established.")))
print(" - UDP: {}".format(linesplit.count("UDP connection established.")))

print("Average:")
addtable(5,9,9, "Size", "TX", "RX")
addtable(5,9,9, "-"*5,"-"*9,"-"*9,"+")

dictkeys = sorted(TX.keys(), key=len)
avgTX = dict()
avgRX = dict()

for key in dictkeys:
    avgTX[key] = sum(TX[key]) / float(len(TX[key]))
    avgRX[key] = sum(RX[key]) / float(len(RX[key]))
    
    addtable(5, 9, 9, key,  "{:7.2f}".format(avgTX[key]), \
                            "{:7.2f}".format(avgRX[key]))
      

print("\nBiggest Deviation From Average:")
addtable(5,18,18,"Size","TX","RX")
addtable(5,18,18,"-"*5,"-"*18,"-"*18,"+")

for key in dictkeys:
    sortedTX = sorted(TX[key])
    sortedRX = sorted(RX[key])    
    
    absNegDevTX = sortedTX[0] - avgTX[key]                 # absolute negative deviation from tx average
    absPosDevTX = sortedTX[len(sortedTX)-1] - avgTX[key]   # absolute positive deviation from tx average
    absNegDevRX = sortedRX[0] - avgRX[key]
    absPosDevRX = sortedRX[len(sortedRX)-1] - avgRX[key]
    
    addtable(5,18,18, key,  "{:+8.2f} {:+8.2%}".format(absNegDevTX, absNegDevTX/avgTX[key]), \
                            "{:+8.2f} {:+8.2%}".format(absNegDevRX, absNegDevRX/avgRX[key]))
    
    addtable(5,18,18, "",   "{:+8.2f} {:+8.2%}".format(absPosDevTX, absPosDevTX/avgTX[key]), \
                            "{:+8.2f} {:+8.2%}".format(absPosDevRX, absPosDevRX/avgRX[key]))
   
    addtable(5,18,18,"-"*5,"-"*18,"-"*18,"+")
