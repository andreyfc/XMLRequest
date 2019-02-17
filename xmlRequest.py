import requests
import xml.etree.ElementTree as ET

xml_headers = { 'content-type': 'text/xml' }

xml_request = open( 'request.xml' ).read()

xml_response = requests.post( 'http://www.ahgora.com.br/ws/pontoweb.php', data=xml_request, headers=xml_headers )

tree = ET.fromstring( xml_response.content )

for elem in tree.iter():
    # if elem.tag == 'status':
        print ( elem.tag, ':', elem.text )