# Rentable Integrations XML Parser

![Rentable](https://mms.businesswire.com/media/20210803005327/en/895740/23/Rentable_Logo.jpg)

### Overview:
- This project is a script that parses XML data from a file, extracts relevant information about Rentable properties located in Madison, and stores it in a DynamoDB database hosted in AWS. The application also fetches weather data for each property from the [National Weather Service API](https://www.weather.gov/documentation/services-web-api) and updates the database with the retrieved weather data. 

### Requirements:
- For Python
    - [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) library for interacting with DynamoDB
    - Requests library for making HTTP requests
    - [Xml.etree.ElementTree](https://docs.python.org/3/library/xml.etree.elementtree.html) library for parsing XML data
    - JSON library for parsing JSON data
- For Ruby
    - aws-sdk-dynamodb gem for interacting with DynamoDB
    - [Nokogiri](https://nokogiri.org)  gem for parsing XML data
    - Open-uri gem for making HTTP requests
    - JSON gem for parsing JSON data

### Getting Started with Python:
1. Install the required libraries: `pip install boto3 requests xml.etree.ElementTree json`
2. Set up your [AWS credentials](https://docs.aws.amazon.com/keyspaces/latest/devguide/access.credentials.html) by creating a file named `~/.aws/credentials` with the following format:
```
[default]
aws_access_key_id = YOUR_ACCESS_KEY_ID
aws_secret_access_key = YOUR_SECRET_ACCESS_KEY
```
3. Navigate to [DynamoDB](https://aws.amazon.com/dynamodb/) and create a table named "rentable_properties"

### Usage Python:
1. After dependencies are installed, to dump data locally run `python3 python/data_dump.py ` This should dump a JSON object to the local directory under the file name 'python_output.json' taking into our requirements.
2. Once credentials are set under the file named `~/.aws/credentials` and a table is created named "rentable_properties" run the following command to upload DynamoDB: `python3 python/upload_dynamodb.py`
3. Visit [DynamoDB](https://aws.amazon.com/dynamodb/) and view the rentable_properties table. This should reflect the following attributes:
    * property_id (primary key)
    * name
    * email
    * bedrooms
    * weather
4. Alternatively, run ``python3 python/fetch_tables.py `` to print a scan of the table

### Getting Started with Ruby:
1. Install the required libraries: `gem install aws-sdk-dynamodb nokogiri open-uri json`
2. Set up your [AWS credentials](https://docs.aws.amazon.com/keyspaces/latest/devguide/access.credentials.html) by creating a file named `~/.aws/credentials` with the following format:
``` 
[default]
aws_access_key_id = YOUR_ACCESS_KEY_ID
aws_secret_access_key = YOUR_SECRET_ACCESS_KEY
```
3. Create a [DynamoDB](https://aws.amazon.com/dynamodb/) table named 'properties'

### Usage Ruby:
1. After dependencies are installed, to dump data locally run `ruby ruby/data_dump.rb ` This should dump a JSON object to the local directory under the file name 'ruby_output.json'. 
2. Once credentials are set under the file named `~/.aws/credentials` and a table is created named "rentable_properties" run the following command to upload to DynamoDB: `ruby ruby/upload_dynamodb.rb`
3. Visit [DynamoDB](https://aws.amazon.com/dynamodb/) and view the rentable_properties table. This should reflect the following attributes:
    * property_id (primary key)
    * name
    * email
    * bedrooms
    * weather
4. Alternatively, run `ruby ruby/fetch_tables.rb ` to print a scan of the table

## Functions and Methods:

`get_properties(root)`
  - Extracts all Property elements from the XML root element and returns them as a list 

`extract_property_data(property_element)`
  - Extracts relevant data (property ID, name, email, bedrooms, city, latitude, and longitude) from a single Property element and returns it as a dictionary.

`filter_properties_by_city(properties, city)`
  - Filters a list of properties by a specific city, extracts the relevant data, fetches the weather data for each property, and returns a list of filtered properties with weather data.

 `get_weather(lat, long)`
  - Fetches the current weather forecast for a given location (specified by latitude and longitude) from the National Weather Service API and returns the detailed forecast for the current day. For more information see: [National Weather Service API](https://www.weather.gov/documentation/services-web-api)

 `add_properties_to_table`
 - Parses an XML file, extracts properties located in Madison, and adds them to a DynamoDB table named 'rentable_properties'. It also measures and prints the execution time of the script.

# Notes:
* Make sure to replace YOUR_ACCESS_KEY_ID and YOUR_SECRET_ACCESS_KEY with your actual AWS credentials.
* The script assumes that the XML file rentable_input_data.xml is located in the same directory as the script.