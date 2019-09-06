#!/usr/bin/env python3.7

from xml.dom.minidom import parse, parseString, getDOMImplementation



impl =                          getDOMImplementation()
newdoc =                        impl.createDocument(None, "CHECKLIST", None)

###
#define Node class
###

class Node:
        def __init__(self, docElement, children):
                self.docElement =       docElement
                self.children =         children

        def appendChildrenList(self):
                [ self.docElement.appendChild(item) for item in self.children ]


###
#define variables for all XML elements
###

#body
checklist =                     newdoc.documentElement

#1st of 2 checklist_elements is asset
asset =                         newdoc.createElement("ASSET")

#all asset_elements
role =          	        newdoc.createElement("ROLE")
asset_type =                    newdoc.createElement("ASSET_TYPE")           
host_name =                     newdoc.createElement("HOST_NAME")            
host_ip =                       newdoc.createElement("HOST_IP")              
host_mac =                      newdoc.createElement("HOST_MAC")             
host_fqdn =                     newdoc.createElement("HOST_FQDN")           
tech_area =                     newdoc.createElement("TECH_AREA")            
target_key =                    newdoc.createElement("TARGET_KEY")           
web_or_database =               newdoc.createElement("WEB_OR_DATABASE")              
web_db_site =                   newdoc.createElement("WEB_DB_SITE")         
web_db_instance =               newdoc.createElement("WEB_DB_INSTANCE")

#2nd of checklist_elements is stigs
stigs =                         newdoc.createElement("STIGS")

#only stigs element is istig
istig =                         newdoc.createElement("iSTIG")

#1st of 2 istig_elements is stig_info
stig_info =                     newdoc.createElement("STIG_INFO")

#only stig_info element is si_data
si_data =                       newdoc.createElement("SI_DATA")

#all si_data_elements
sid_name =                      newdoc.createElement("SID_NAME")
sid_data =                      newdoc.createElement("SID_DATA")

#2nd of 2 istig_elements is vuln
vuln =                          newdoc.createElement("VULN")

#all vuln_elements
stig_data =                     newdoc.createElement("STIG_DATA")
status =                        newdoc.createElement("STATUS")
finding_details =               newdoc.createElement("FINDING_DETAILS")
comments =                      newdoc.createElement("COMMENTS")
severity_override =             newdoc.createElement("SEVERITY_OVERRIDE")
severity_justification =        newdoc.createElement("SEVERITY_JUSTIFICATION")

#all stig_data_elements
vuln_attribute =                newdoc.createElement("VULN_ATTRIBUTE")
attribute_data =                newdoc.createElement("ATTRIBUTE_DATA")

###
#define all lists and appends
###

"""
checklist_elements = [
        asset,
        stigs
]
[ checklist.appendChild(item) for item in checklist_elements ]
"""
Checklist = Node(checklist, [asset, stigs])
Checklist.appendChildrenList()

"""
asset_elements = [
        role,
        asset_type,
        host_name,
        host_ip,
        host_mac,
        host_fqdn,
        tech_area,
        target_key,
        web_or_database,
        web_db_site,
        web_db_instance
        ]
[ asset.appendChild(item) for item in asset_elements ]
"""
Asset = Node(asset, [role, asset_type, host_name, host_ip, host_mac, host_fqdn, tech_area, target_key, web_or_database, web_db_site, web_db_instance])
Asset.appendChildrenList()

"""
stigs.appendChild(istig)
"""
Stigs = Node(stigs, [istig])
Stigs.appendChildrenList()

"""
istig_elements = [
        stig_info,
        vuln
]
[ istig.appendChild(item) for item in istig_elements ]
"""
Istig = Node(istig, [stig_info, vuln])
Istig.appendChildrenList()

"""
stig_info.appendChild(si_data)
"""
Stig_Info = Node(stig_info, [si_data])
Stig_Info.appendChildrenList()

"""
si_data_elements =[
	sid_name,
	sid_data
] 
[ si_data.appendChild(item) for item in si_data_elements ]
"""
Si_Data = Node(si_data, [sid_name, sid_data])
Si_Data.appendChildrenList()

"""
vuln_elements = [
	stig_data,
	status,
	finding_details,
	comments,
        severity_override,
        severity_justification
]
[ vuln.appendChild(item) for item in vuln_elements ]
"""
Vuln = Node(vuln, [stig_data, status, finding_details, comments, severity_override, severity_justification])
Vuln.appendChildrenList()

"""
stig_data_elements = [
	vuln_attribute,
	attribute_data
]
[ stig_data.appendChild(item) for item in stig_data_elements]
"""
Stig_Data = Node(stig_data, [vuln_attribute, attribute_data])
Stig_Data.appendChildrenList()


#text = newdoc.createTextNode('Some textual content.')

print(newdoc.toprettyxml())
