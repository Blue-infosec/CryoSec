#!/usr/bin/env python3
from shutil import copyfile
from xml.dom.minidom import parse
import xml.dom.minidom
from pathlib import Path

"""
OBJECTIVES
[x] Get data that you want
[] Create new stig with old data 
[] Change encoding to UTF-8
[] Export data that you want to a new file
[] display data the way that you want
[] Search for data that you want
"""

# POPLULATE NEW CHECKLIST
"""
#newtree.write('NEW_output.xml')
"""

def file_process():
    f = open(file='rhel7_05252019.ckl',mode='rb')
    return f.read()
    #print(f.readlines())


# Get and Print MACHINE VULN DATA
def process_xml(data):
    # Create main list
    master_vuln_list = []
    
    # Open XML document using minidom parser
    DOMTree = xml.dom.minidom.parseString(data)
    collection = DOMTree.documentElement

    VULNS = collection.getElementsByTagName("VULN")
    vuln_count = len(VULNS)

    i = 0
    while i < vuln_count:

        # IF XML ELEMENT CONTAINS DATA THEN PRINT THE DATA IF NOT PRINT "NO DATA"
        def chkval(value):
            if value.childNodes.length == 0:
                return str("NO DATA")
            else:
                return str(value.childNodes[0].data)

        elements=VULNS[i].getElementsByTagName
        xml_attri=elements("ATTRIBUTE_DATA")
        # DEFINE CHECKLIST DATA ELEMENTS
        vuln_dict = {
            "stigid":          chkval(xml_attri[4]),
            "vulnid":          chkval(xml_attri[0]),
            "severity":        chkval(xml_attri[1]), 
            "vulndiscuss":     chkval(xml_attri[6]),
            "checkcontent":    chkval(xml_attri[8]),
            "fixtext":         chkval(xml_attri[9]),
            "stigref":         chkval(xml_attri[21]),
            "status":          chkval(elements("STATUS")[0]),
            "finding_details": chkval(elements("FINDING_DETAILS")[0]),
            "comments":        chkval(elements("COMMENTS")[0])
        }
        
        # add list to main list
        master_vuln_list.append(vuln_dict)
        
        i += 1
    # Return 1st item in checklist
    return master_vuln_list
    #Return specific item in checklist
    #return [ vuln for vuln in master_vuln_list if '07-020110' in vuln['stigid'] ]

data=file_process() 
print(process_xml(data))



"""
   print("Description: %s" % description.childNodes[0].data)
"""
"""
    i = 0
    while i < number_of_VULNS:
        status = VULN[i].find('STATUS').text
        #newroot.remove(VULN[i])
        #newroot.remove(V)
        print(VULN[i].tag)
        print(VULN[i])
        newroot.remove(iSTIG[0][i])
        i += 1
"""








