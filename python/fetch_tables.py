import boto3
# Script to ensure that data is in table and able to be accessed. 

def _get_table_data():
    dynamodb = boto3.resource('dynamodb')
    table_name = 'rentable_properties'
    table = dynamodb.Table(table_name)
    data = table.scan()
    return data['Items']
print(_get_table_data())
