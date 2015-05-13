""" parse.py

Helper class of netio-parser.py

Author: crasbe, 04.10.2014
"""

class Parse:
    def __init__(self, rawfile):
        """ ___init___:
        """
        self.rawfile = rawfile
        
        self.results = { "RX" :  {  "1k"    : [], "2k"    : [],
                                    "4k"    : [], "8k"    : [], 
                                    "16k"   : [], "32k"   : [] },
                                    
                         "TX" :  {  "1k"    : [], "2k"    : [], 
                                    "4k"    : [], "8k"    : [], 
                                    "16k"   : [], "32k"   : [] } }
        
        self.avg = { "RX" :  {  "1k"    : 0.0, "2k"    : 0.0,
                                    "4k"    : 0.0, "8k"    : 0.0, 
                                    "16k"   : 0.0, "32k"   : 0.0 },
                                    
                         "TX" :  {  "1k"    : 0.0, "2k"    : 0.0, 
                                    "4k"    : 0.0, "8k"    : 0.0, 
                                    "16k"   : 0.0, "32k"   : 0.0 } }
        
        self.posdev = { "RX" :  {  "1k"    : 0.0, "2k"    : 0.0,
                                    "4k"    : 0.0, "8k"    : 0.0, 
                                    "16k"   : 0.0, "32k"   : 0.0 },
                                    
                         "TX" :  {  "1k"    : 0.0, "2k"    : 0.0, 
                                    "4k"    : 0.0, "8k"    : 0.0, 
                                    "16k"   : 0.0, "32k"   : 0.0 } }
                                    
        self.negdev = { "RX" :  {  "1k"    : 0.0, "2k"    : 0.0,
                                    "4k"    : 0.0, "8k"    : 0.0, 
                                    "16k"   : 0.0, "32k"   : 0.0 },
                                    
                         "TX" :  {  "1k"    : 0.0, "2k"    : 0.0, 
                                    "4k"    : 0.0, "8k"    : 0.0, 
                                    "16k"   : 0.0, "32k"   : 0.0 } }
                    
        self.statVersion    = str()
        self.invalid        = int()
        self.validTCP       = int()
        self.validUDP       = int()
        
    def calculate(self):        
        for line in self.rawfile:
            if(not "Packet size" in line):
                continue
            
            # example: "Packet size  1k bytes:  57.08 KByte/s Tx,  31.73 KByte/s Rx."
            tmp = line.rsplit("  ",2)            # ['Packet size  1k bytes:', '57.08 KByte/s Tx,', '31.73 KByte/s Rx.']
            if(len(tmp) != 3 or not "Rx" in tmp[-1]):
                invalid += 1
                continue
            
            txtmp = tmp[1].split(" ")[0]         # '57.08'
            rxtmp = tmp[2].split(" ")[0]         # '31.73'
            
            packetsize = tmp[0].rsplit(" ",2)[1] # '1k'
            
            self.results["TX"][packetsize].append(float(txtmp))
            self.results["RX"][packetsize].append(float(rxtmp))
        
        for rxtx in ["RX", "TX"]:
            dictkeys = sorted(self.results[rxtx].keys(), key=len)
            sortedrxtx = sorted(self.results[rxtx])

            for key in dictkeys:
                self.avg[rxtx][key] =   sum(self.results[rxtx][key]) / float(len(self.results[rxtx][key]))
                
                self.negdev[rxtx][key] = sortedrxtx[0] - self.avg[rxtx][key]                 # absolute negative deviation from tx average
                self.posdev[rxtx][key] = sortedrxtx[len(sortedrxtx)-1] - self.avg[rxtx][key]   # absolute positive deviation from tx average

    
    def average(self, rxtx, key):
        if(rxtx != "RX" and rxtx != "TX"):
            return
        if(key not in self.avg[rxtx]):
            return
        
        return self.avg[rxtx][key]
        
       
    def deviation(self, rxtx):
        if(rxtx != "RX" or rxtx != "TX"):
            return
            
        
        
    def stats(self, attribute):
        if(attribute == "version"):
            for line in linesplit:
                if("Version" in line):
                    self.version = line.rsplit(" ",1)[1]
                    break
            return self.version
        elif(attribute == "invalid"):
            return self.invalid
        elif(attribute == "validTCP"):
            return self.validTCP
        elif(attribute == "validUTP"):
            return self.validUTP

    
    def whatever(self):
        pass
