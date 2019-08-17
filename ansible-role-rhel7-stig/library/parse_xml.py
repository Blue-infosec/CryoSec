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
class checkList:

    def __init__(self,input_file,output_file,stig_id,status):
        self.input_file = input_file
        self.output_file = output_file
        self.stig_id = stig_id
        self.status = status
        self.DOMTree = xml.dom.minidom.parse(input_file)


    def process_xml(self):
        # Create main list
        master_vuln_list = []

        # Open XML document using minidom parser
        collection = self.DOMTree.documentElement

        VULNS = collection.getElementsByTagName("VULN")
        vuln_count = len(VULNS)

        i = 0
        while i < vuln_count:

            # IF XML ELEMENT CONTAINS DATA THEN PRINT THE DATA IF NOT PRINT "NO DATA"
            def chk_has_val(value):
                if value.childNodes.length == 0:
                    return str("NO DATA")
                else:
                    return str(value.childNodes[0].data)

            elements=VULNS[i].getElementsByTagName
            xml_attri=elements("ATTRIBUTE_DATA")

            # DEFINE CHECKLIST DATA ELEMENTS
            vuln_dict = {
                "stigid":          chk_has_val(xml_attri[4]),
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
        #if tolist == True:
        #    return master_vuln_list
        #if tolist == False:
        #    return VULNS

        return VULNS
        #return master_vuln_list


    # Set the STATUS
    def set_status(self,node):
        stig_id=node.getElementsByTagName("STIG_DATA")[4].childNodes[3].firstChild.nodeValue
        node.getElementsByTagName("STATUS")[0].childNodes[0].nodeValue = self.status
        _node = node.getElementsByTagName("STATUS")[0].childNodes[0].nodeValue
        print(_node)


    # Iterate through VULNS that match a stig_id and process STATUS update
    def mark_checklist(self):
        xml=self.process_xml()

        #Set the STATUS of VULN per particular stig_id
        [ self.set_status(item) for item in
            xml if self.stig_id in
            item.getElementsByTagName("STIG_DATA")[4].childNodes[3].firstChild.nodeValue
            ]


    def write_checklist(self):
        f = open(self.output_file,'w+')
        f.write(self.DOMTree.toprettyxml())
        f.close()



ckl = checkList('rhel7_05252019.ckl','rhel7_05252019.ckl.output','07-020110','NEW_VALUE')
ckl.status = 'NEW_VALUE'
ckl.output_file
ckl.input_file
ckl.mark_checklist()
ckl.status = 'NEW_VALUE2'
ckl.mark_checklist()
ckl.write_checklist()









