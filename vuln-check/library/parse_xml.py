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


# Get and Print MACHINE VULN DATA
def process_xml(data,tolist=True):

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
        
        # Add checklist data to main list
        master_vuln_list.append(vuln_dict)
        i += 1

    # Return 1st item in checklist - return raw xml or a list of VULNS
    if tolist == True:
        return master_vuln_list
    if tolist == False:
        return VULNS

    #Return specific item in checklist
    #return [ vuln for vuln in master_vuln_list if '07-020110' in vuln['stigid'] ]


# Load the checklist file
def file_process(inputfile):
    #f = open(file='rhel7_05252019.ckl',mode='rb')
    f = open(file='rhel7_05252019.ckl',mode='rb')
    return f.read()


# Set the STATUS
def set_status(node):
    stig_id=node.getElementsByTagName("STIG_DATA")[4].childNodes[3].firstChild.nodeValue 
    node.getElementsByTagName("STATUS")[0].childNodes[0].nodeValue='TEST_VALUE'


# Iterate through VULNS that match a stig_id and process STATUS update
def mark_checklist(inputfile):
    data=file_process(inputfile) 
    rawxml=process_xml(data,False)

    #Set the STATUS of VULN per particular stig_id
    [ set_status(item) for item in 
        rawxml if '07-020110' in 
        item.getElementsByTagName("STIG_DATA")[4].childNodes[3].firstChild.nodeValue 
        ]
    #Print STATUS for VULN per particular stig_id
    [ print(item.getElementsByTagName("STATUS")[0].childNodes[0].nodeValue) 
        for item in rawxml 
        if '07-020110' in 
        item.getElementsByTagName("STIG_DATA")[4].childNodes[3].firstChild.nodeValue 
        ]

    #f"output_{ inputfile }"
    rawxml.toprettyxml()


inputfile = 'rhel7_05252019.ckl'
mark_checklist(inputfile)
  







