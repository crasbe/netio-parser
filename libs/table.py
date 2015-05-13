""" table.py

Helper class of netio-parser.py

Author: crasbe, 04.10.2014
"""

class Table:
    
    def __init__(self):
        pass

    def addtable(swidth, txwidth, rxwidth, svalue='', txvalue='', rxvalue='', \
            sep="|"):
    """ a little function to help with the table
    
    swidth  - with of the size column
    svalue - value for the size column
    txwidth,txvalue,... the same
    """
    
    print("{:<{space}}{}".format(svalue, sep, space=swidth),end="")
    print("{:^{space}}{}".format(txvalue, sep, space=txwidth),end="")
    print("{:^{space}}{}".format(rxvalue, sep, space=rxwidth))    
