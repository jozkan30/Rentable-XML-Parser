import boto3
from data_dump import parse_xml_file, get_properties, filter_properties_by_city

dynamodb = boto3.resource('dynamodb')
table_name = 'rentable_properties'

table = dynamodb.Table(table_name)

def add_properties_to_table():
    file_path = 'python/rentable_input_data.xml'
    root = parse_xml_file(file_path)
    properties = get_properties(root)
    filtered_properties = filter_properties_by_city(properties, 'Madison')

    for prop in filtered_properties:
        table.put_item(Item=prop)

add_properties_to_table()