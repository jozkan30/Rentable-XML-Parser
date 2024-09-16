require 'nokogiri'
require 'json'
require_relative 'get_weather'
require 'pry'

def parse_xml_file(file_path)
  # Load the XML file
  xml = File.read(file_path)
  doc = Nokogiri::XML(xml)
  doc.root
end

def get_properties(root)
  # Find all Property elements
  root.xpath('.//Property')
end

def extract_property_data(property_element)
  # Extract values for dump defined in task excercise.
  property_id = property_element.at_xpath('.//PropertyID/Identification/@IDValue').value
  name = property_element.at_xpath('.//PropertyID/MarketingName').text
  email = property_element.at_xpath('.//PropertyID/Email').text
  address = property_element.at_xpath('.//PropertyID/Address[@AddressType="property"]')
  bedrooms = property_element.at_xpath('.//Floorplan/Room/Count').text
  latitude = property_element.at_xpath('.//ILS_Identification/Latitude').text
  longitude = property_element.at_xpath('.//ILS_Identification/Longitude').text

  if address
    city = address.at_xpath('.//City').text
  else
    city = nil
  end
  {
    'property_id' => property_id,
    'name' => name,
    'email' => email,
    'bedrooms' => bedrooms,
    'city' => city,
    'latitude' => latitude,
    'longitude' => longitude
  }
end

def filter_properties_by_city(properties, city)
  # Define a function for filtering by city. In this case using Madison. Fetch the weather after.
  filtered_properties = {}
  properties.each do |prop|
    data = extract_property_data(prop)
    if data['city'] == city
      weather = get_weather(data['latitude'], data['longitude'])
      property_id = data['property_id']
      if !filtered_properties.key?(property_id)
        filtered_properties[property_id] = {
          'property_id' => property_id,
          'name' => data['name'],
          'email' => data['email'],
          'bedrooms' => data['bedrooms'],
          'weather' => weather
        }
      end
    end
  end
  filtered_properties.values
end

def write_to_json(data, file_path)
  # Write data to JSON
  File.open(file_path, 'w') do |f|
    f.write(JSON.pretty_generate(data))
  end
end

def main
  file_path = 'ruby/rentable_input_data.xml'
  root = parse_xml_file(file_path)
  properties = get_properties(root)
  puts "Total properties: #{properties.size}"
  filtered_properties = filter_properties_by_city(properties, 'Madison')
  puts "Total properties in city: #{filtered_properties.size}"
  write_to_json(filtered_properties, 'ruby/ruby_output.json')
end

main