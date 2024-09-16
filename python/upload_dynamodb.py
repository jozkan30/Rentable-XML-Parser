import boto3
from data_dump import parse_xml_file, get_properties, filter_properties_by_city
import time

dynamodb = boto3.resource('dynamodb')
table_name = 'rentable_properties'

table = dynamodb.Table(table_name)

def add_properties_to_table():
    file_path = 'python/rentable_input_data.xml'
    root = parse_xml_file(file_path)
    properties = get_properties(root)
    print("Total properties:", len(properties))
    filtered_properties = filter_properties_by_city(properties, 'Madison')
    print("Total properties in city:", len(filtered_properties))
    start_time = time.time()

    for prop in filtered_properties:
        table.put_item(Item=prop)

    end_time = time.time()
    run_time = end_time - start_time
    print(f'Run completed in {run_time:.2f} seconds')

add_properties_to_table()