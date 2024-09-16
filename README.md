# Rentable Integrations XML Parser

### Overview:
- This project is a script that parses XML data from a file, extracts relevant information about Rentable properties, and stores it in a DynamoDB database. The application also fetches weather data for each property from the National Weather Service API and updates the database with the retrieved weather data. 

### Requirements:
- For Python
    - Boto3 library for interacting with DynamoDB
    - Requests library for making HTTP requests
    - [Xml.etree.ElementTree]('https://docs.python.org/3/library/xml.etree.elementtree.html') library for parsing XML data
    - Json library for parsing JSON data
- For Ruby
    - Aws-sdk-dynamodb gem for interacting with DynamoDB
    - [Nokogiri]('https://nokogiri.org')  gem for parsing XML data
    - Open-uri gem for making HTTP requests
    - Json gem for parsing JSON data

### Getting Started with Python:
1. Install the required libraries: `pip install boto3 requests xml.etree.ElementTree json`
2. Set up your [AWS credentials]('https://docs.aws.amazon.com/keyspaces/latest/devguide/access.credentials.html') by creating a file named `~/.aws/credentials` with the following format:
``` 
[default]
aws_access_key_id = YOUR_ACCESS_KEY_ID
aws_secret_access_key = YOUR_SECRET_ACCESS_KEY
```
3. Create a [DynamoDB]('https://aws.amazon.com/dynamodb/') table named 'retable_properties'


### Usage Python:
1. After dependecies are installed, to dump data locally run `python3 python/data_dump.py ` This should dump a JSON object to the locally directory under the file name 'python_output.json'. 
2. Once credntials are set under the file named `~/.aws/credentials` and a table is created named "rentable_properties" run the following command to upload the the dynamodb: `python3 python/upload_dynamodb.py`
3. Visit [DynamoDB]('https://aws.amazon.com/dynamodb/') and view the rentable_properties table. This should reflect the following attributes:
    * property_id (primary key)
    * name
    * email
    * bedrooms
    * city
    * weather


### Usage Ruby:
1. After dependecies are installed, to dump data locally run `ruby ruby/data_dump.rb ` This should dump a JSON object to the locally directory under the file name 'ruby_output.json'. 
2. Once credntials are set under the file named `~/.aws/credentials` and a table is created named "rentable_properties" run the following command to upload the the dynamodb: `ruby ruby/upload_dynamodb.rb`
3. Visit [DynamoDB]('https://aws.amazon.com/dynamodb/') and view the rentable_properties table. This should reflect the following attributes:
    * property_id (primary key)
    * name
    * email
    * bedrooms
    * city
    * weather

Notes:

* Make sure to replace YOUR_ACCESS_KEY_ID and YOUR_SECRET_ACCESS_KEY with your actual AWS credentials.
* The script assumes that the XML file rentable_input_data.xml is located in the same directory as the script.