#!/usr/bin/env python3.7

from xml.dom.minidom import parse, parseString, getDOMImplementation




###
#define Node class
###

class Node:
    def __init__(self, docElement, children):
    #def __init__(self, docElement, children):
       #self.docElement = docElement
       #self.children   = children
       self.impl   = getDOMImplementation()
       self.newdoc = self.impl.createDocument(None, "CHECKLIST", None)

    def appendChildrenList(self):
      [ self.docElement.appendChild(item) for item in self.children ]

    def gen_checklist(self):
        ###
        #define variables for all XML elements
        ###

        #body
        checklist = self.newdoc.documentElement

        #1st of 2 checklist_elements is asset
        asset = self.newdoc.createElement("ASSET")

        #all asset_elements
        role            = self.newdoc.createElement("ROLE")
        asset_type      = self.newdoc.createElement("ASSET_TYPE")
        host_name       = self.newdoc.createElement("HOST_NAME")
        host_ip         = self.newdoc.createElement("HOST_IP")
        host_mac        = self.newdoc.createElement("HOST_MAC")
        host_fqdn       = self.newdoc.createElement("HOST_FQDN")
        tech_area       = self.newdoc.createElement("TECH_AREA")
        target_key      = self.newdoc.createElement("TARGET_KEY")
        web_or_database = self.newdoc.createElement("WEB_OR_DATABASE")
        web_db_site     = self.newdoc.createElement("WEB_DB_SITE")
        web_db_instance = self.newdoc.createElement("WEB_DB_INSTANCE")

        #2nd of checklist_elements is stigs
        stigs     = self.newdoc.createElement("STIGS")

        #only stigs element is istig
        istig     = self.newdoc.createElement("iSTIG")

        #1st of 2 istig_elements is stig_info
        stig_info = self.newdoc.createElement("STIG_INFO")

        #only stig_info element is si_data
        si_data   = self.newdoc.createElement("SI_DATA")

        #all si_data_elements
        sid_name  = self.newdoc.createElement("SID_NAME")
        sid_data  = self.newdoc.createElement("SID_DATA")

        #2nd of 2 istig_elements is vuln
        vuln      = self.newdoc.createElement("VULN")

        #all vuln_elements
        stig_data              = self.newdoc.createElement("STIG_DATA")
        status                 = self.newdoc.createElement("STATUS")
        finding_details        = self.newdoc.createElement("FINDING_DETAILS")
        comments               = self.newdoc.createElement("COMMENTS")
        severity_override      = self.newdoc.createElement("SEVERITY_OVERRIDE")
        severity_justification = self.newdoc.createElement("SEVERITY_JUSTIFICATION")

        #all stig_data_elements
        vuln_attribute = self.newdoc.createElement("VULN_ATTRIBUTE")
        attribute_data = self.newdoc.createElement("ATTRIBUTE_DATA")

        ###
        #define all lists and appends
        ###

        Checklist = Node(checklist, [asset, stigs])
        Checklist.self.appendChildrenList()

        Asset = Node(asset, [role, asset_type, host_name, host_ip, host_mac, host_fqdn, tech_area, target_key, web_or_database, web_db_site, web_db_instance])
        Asset.self.appendChildrenList()

        Stigs = Node(stigs, [istig])
        Stigs.self.appendChildrenList()

        Istig = Node(istig, [stig_info, vuln])
        Istig.self.appendChildrenList()

        Stig_Info = Node(stig_info, [si_data])
        Stig_Info.self.appendChildrenList()

        Si_Data = Node(si_data, [sid_name, sid_data])
        Si_Data.self.appendChildrenList()

        Vuln = Node(vuln, [stig_data, status, finding_details, comments, severity_override, severity_justification])
        Vuln.self.appendChildrenList()

        Stig_Data = Node(stig_data, [vuln_attribute, attribute_data])
        Stig_Data.self.appendChildrenList()

        return self.newdoc.toprettyxml()

    def return_doc(self):
        print(self.gen_checklist())


checklist = Node()
checklist.return_doc()
