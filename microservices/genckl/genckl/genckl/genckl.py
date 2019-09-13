from xml.dom.minidom import parse, parseString, getDOMImplementation


###
#define Node class
###

class Node:
    def __init__(self):
        self.impl   = getDOMImplementation()
        self.newdoc = self.impl.createDocument(None, "CHECKLIST", None)

    def appendChildrenList(self,docElement,children):
        [ docElement.appendChild(item) for item in children ]

    def gen_checklist(self):
        ###
        #define variables for all XML elements
        ###

        #body
        checklist = self.newdoc.documentElement

        #1st of 2 checklist_elements is asset
        asset = self.newdoc.createElement("ASSET")

        #all asset_elements
        asset_elements = [
          self.newdoc.createElement("ROLE"),
          self.newdoc.createElement("ASSET_TYPE"),
          self.newdoc.createElement("HOST_NAME"),
          self.newdoc.createElement("HOST_IP"),
          self.newdoc.createElement("HOST_MAC"),
          self.newdoc.createElement("HOST_FQDN"),
          self.newdoc.createElement("TECH_AREA"),
          self.newdoc.createElement("TARGET_KEY"),
          self.newdoc.createElement("WEB_OR_DATABASE"),
          self.newdoc.createElement("WEB_DB_SITE"),
          self.newdoc.createElement("WEB_DB_INSTANCE")
        ]

        #2nd of checklist_elements is stigs
        stigs     = self.newdoc.createElement("STIGS")

        #only stigs element is istig
        istig     = self.newdoc.createElement("iSTIG")

        #1st of 2 istig_elements is stig_info
        stig_info = self.newdoc.createElement("STIG_INFO")

        #only stig_info element is si_data
        si_data   = self.newdoc.createElement("SI_DATA")

        #all si_data_elements
        si_data_elements = [
          self.newdoc.createElement("SID_NAME"),
          self.newdoc.createElement("SID_DATA")
        ]

        #2nd of 2 istig_elements is vuln
        vuln      = self.newdoc.createElement("VULN")

        #all stig_data_elements
        stig_data_elements = [
          self.newdoc.createElement("VULN_ATTRIBUTE"),
          self.newdoc.createElement("ATTRIBUTE_DATA")
        ]

        #all vuln_elements
        vuln_elements = [
          self.newdoc.createElement("STATUS"),
          self.newdoc.createElement("FINDING_DETAILS"),
          self.newdoc.createElement("COMMENTS"),
          self.newdoc.createElement("SEVERITY_OVERRIDE"),
          self.newdoc.createElement("SEVERITY_JUSTIFICATION")
        ]


        ###
        #define all lists and appends
        ###
        self.appendChildrenList(checklist, [asset, stigs])
        self.appendChildrenList(asset, asset_elements)
        self.appendChildrenList(stigs, [istig])
        self.appendChildrenList(istig, [stig_info, vuln])
        self.appendChildrenList(stig_info, [si_data])
        self.appendChildrenList(si_data, si_data_elements)
        i = 0
        stigs=[]
        while i < 27:
            stig_data = self.newdoc.createElement("STIG_DATA")
            stig_data.appendChild(self.newdoc.createElement("VULN_ATTRIBUTE"))
            stig_data.appendChild(self.newdoc.createElement("ATTRIBUTE_DATA"))
            self.appendChildrenList(vuln, [stig_data])
            i += 1
        self.appendChildrenList(vuln, vuln_elements)

        return self.newdoc.toprettyxml()

    def return_doc(self):
        print(self.gen_checklist())


#checklist = Node()
#checklist.return_doc()
