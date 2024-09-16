require 'aws-sdk-dynamodb'
require 'nokogiri'
require_relative 'data_dump'
require 'pry'

def add_properties_to_table()
    dynamodb = Aws::DynamoDB::Resource.new(region: 'us-east-1')
    table_name = 'properties'
    table = dynamodb.table(table_name)
    file_path = 'ruby/rentable_input_data.xml'
    doc = parse_xml_file(file_path)
    properties = get_properties(doc)
    filtered_properties = filter_properties_by_city(properties, 'Madison')
    
    filtered_properties.each do |prop|
        table.put_item({ item: prop })
    end
end

add_properties_to_table
