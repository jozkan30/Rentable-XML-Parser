import xml.etree.ElementTree as ET
import json
from get_weather import get_weather


def parse_xml_file(file_path):
    # Grab file from directory. If the link to didn't have an error, we would have imported requests and added "https://s3.amazonaws.com/abodo-misc/sample_abodo_feed.xml" as the endpoint.
    tree = ET.parse(file_path)
    root = tree.getroot()
    return root

def get_properties(root):
    properties = root.findall('.//Property')
    return properties

def extract_property_data(property_element):
    # Extract values for dump defined in task excercise.
    # import ipdb; ipdb.set_trace()
    property_id = property_element.find('.//PropertyID/Identification').attrib.get('IDValue')
    name = property_element.find('.//PropertyID/MarketingName').text
    email = property_element.find('.//PropertyID/Email').text
    address = property_element.find('.//PropertyID/Address[@AddressType="property"]')
    bedrooms = property_element.find('.//Floorplan/Room/Count').text
    latitude = property_element.find('.//ILS_Identification/Latitude').text
    longitude = property_element.find('.//ILS_Identification/Longitude').text

    if address is not None:
        city = address.find('.//City').text
    else:
        city = None
    return {
        'property_id': property_id,
        'name': name,
        'email': email,
        'bedrooms': bedrooms,
        'city': city,
        'latitude': latitude,
        'longitude': longitude
        }

def filter_properties_by_city(properties, city):
    # Define a function for filtering by city. In this case using Madison. Fetch the weather after.
    filtered_properties = {}
    for prop in properties:
        data = extract_property_data(prop)
        if data['city'] == city:
            weather = get_weather(data['latitude'], data['longitude'])
            property_id = data['property_id']
            if property_id not in filtered_properties:
                filtered_properties[property_id] = {
                    'property_id': property_id,
                    'name': data['name'],
                    'email': data['email'],
                    'bedrooms': data['bedrooms'],
                    'weather': weather
                }
    return list(filtered_properties.values())

def write_to_json(data, file_path):
    # Write data to json
    with open(file_path, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=2)

def main():
    file_path = 'python/rentable_input_data.xml'
    root = parse_xml_file(file_path)
    properties = get_properties(root)
    print("Total properties:", len(properties))
    filtered_properties = filter_properties_by_city(properties, 'Madison')
    print("Total properties in city:", len(filtered_properties))
    write_to_json(filtered_properties, 'python/python_output.json')

if __name__ == '__main__':
    main()