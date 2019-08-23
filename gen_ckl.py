#!/usr/bin/env python3.7
from xml.dom.minidom import parse, parseString, getDOMImplementation

impl = getDOMImplementation()

newdoc = impl.createDocument(None, "CHECKLIST", None)
top_element = newdoc.documentElement
asset = newdoc.createElement("ASSET")
role = newdoc.createElement("ROLE")

asset_types = [
        newdoc.createElement("ASSET_TYPE"),
        newdoc.createElement("HOST_NAME"),
        newdoc.createElement("HOST_IP"),
        newdoc.createElement("HOST_MAC"),
        newdoc.createElement("HOST_FQDN"),
        newdoc.createElement("TECH_AREA"),
        newdoc.createElement("TARGET_KEY"),
        newdoc.createElement("WEB_OR_DATABASE"),
        newdoc.createElement("WEB_OR_DB_SITE"),
        newdoc.createElement("WEB_OR_DB_INSTANCE")
        ]
#text = newdoc.createTextNode('Some textual content.')
top_element.appendChild(asset)
[ asset.appendChild(item) for item in asset_types ]

stigs = newdoc.createElement("STIGS")
#top_element.appendChild()
istig = newdoc.createElement("iSTIG")
stig_info = newdoc.createElement("STIG_INFO")
stigs.appendChild(istig)
istig.appendChild(stig_info)

newdoc.createElement("STIG_INFO")

#[top_element.appendChild(item) for item in stigs]




print(newdoc.toprettyxml())
