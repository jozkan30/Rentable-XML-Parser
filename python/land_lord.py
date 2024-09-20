import xml.etree.ElementTree as ET
import json

class LandLord:
    def __init__(self, xml_file_path, xpath_config, name):
        self.name = name
        self.xml_file_path = xml_file_path
        self.xpath_config = xpath_config

    def parse_xml_file(self):
        tree = ET.parse(self.xml_file_path)
        root = tree.getroot()
        return root

    def get_properties(self, root):
        properties_xpath = self.xpath_config.get('properties')
        properties = root.findall(properties_xpath)
        return properties

    def extract_property_data(self, property_element):
        property_id = property_element.find(self.xpath_config['property_data']['property_id']).attrib.get('IDValue')
        name = property_element.find(self.xpath_config['property_data']['name']).text.strip()
        email = property_element.find(self.xpath_config['property_data']['email']).text.strip()
        bedrooms = property_element.find(self.xpath_config['property_data']['bedrooms']).text.strip()
        city = property_element.find(self.xpath_config['property_data']['city']).text.strip()

        return {
            'property_id': property_id,
            'name': name,
            'email': email,
            'bedrooms': bedrooms,
            'city': city
        }

    # Filter by city set in config. 
    def filter_properties_by_city(self, properties, city):
        filtered_properties = {}
        for prop in properties:
            data = self.extract_property_data(prop)
            if data.get('city') == city:
                property_id = data.get('property_id')
                if property_id not in filtered_properties:
                    filtered_properties[property_id] = data
        return list(filtered_properties.values())
    
    def write_to_json(self, data, file_path):
        with open(file_path, 'w') as jsonfile:
            json.dump(data, jsonfile, indent=2)