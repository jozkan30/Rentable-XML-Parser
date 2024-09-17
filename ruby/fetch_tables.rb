require 'aws-sdk-dynamodb'

def _get_table_data()
    dynamodb = Aws::DynamoDB::Resource.new(region: 'us-east-1')
    table_name = 'properties'
    table = dynamodb.table(table_name)
    data = table.scan()
    data[:items]
end

puts _get_table_data