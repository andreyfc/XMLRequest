import requests
import xml.etree.ElementTree as ET

xml_headers = { 'content-type': 'text/xml' }

xml_request = open( 'file.xml' ).read()

xml_response = requests.post( 'http://www.yourpage.com.br/ws/xxx.php', data=xml_request, headers=xml_headers )

tree = ET.fromstring( xml_response.content )

for elem in tree.iter():
    print ( elem.tag, ':', elem.text )
