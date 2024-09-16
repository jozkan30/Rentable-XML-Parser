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
    puts "Total properties: #{properties.size}"
    filtered_properties = filter_properties_by_city(properties, 'Madison')
    puts "Total properties in city: #{filtered_properties.size}"
    start_time = Time.now

    filtered_properties.each do |prop|
        table.put_item({ item: prop })
    end
    end_time = Time.now
    run_time = end_time - start_time
    puts "Run completed in #{run_time.round(2)} seconds"
end

add_properties_to_table
