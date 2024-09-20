import argparse
import json
from land_lord import LandLord

def main():
    parser = argparse.ArgumentParser(description='Run data dump for specific landlord from config')
    parser.add_argument('name', help='Name of the landlord (from config.json)')
    args = parser.parse_args()

    with open('python/configs.json', 'r') as f:
        config = json.load(f)

    if args.name in config['landlords']:
        config = config['landlords'][args.name]
        print(f"Fetching config for {args.name}")
        # Using direct path to existing data but would use path/to/{args.name}.xml if multiple files.
        landlord = LandLord(f'python/rentable_input_data.xml', config, args.name)
        data  = landlord.parse_xml_file()
        properties = landlord.get_properties(data)
        filtered_properties = landlord.filter_properties_by_city(properties, 'Madison')
        landlord.write_to_json(filtered_properties, f'python/{args.name}_data.json')
        print(f"Data dump for {args.name} completed")
    else:
        print(f"Invalid landlord name: {args.name}. Available options:")
        for name in config['landlords'].keys():
            print(f"- {name}")

if __name__ == '__main__':
    main()