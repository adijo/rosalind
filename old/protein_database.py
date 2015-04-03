import re
import urllib2

dna = raw_input()
url = "http://www.uniprot.org/uniprot/%s.txt" % dna

database = urllib2.urlopen(url)


regex = r"P\:(?:[A-Za-z\-]+\ ?)+\;"
for line in database:
    val = re.findall(regex,line)
    if len(val) > 0:
        print val[0][2:-1]
    
                   
                   
                   


