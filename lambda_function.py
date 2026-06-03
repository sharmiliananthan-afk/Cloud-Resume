import json
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('resume-visitor-counter')

def lambda_handler(event, context):
    
    # Update the count — add 1 every time this runs
    response = table.update_item(
        Key={'id': 'Visitors'},
        UpdateExpression='SET #count = if_not_exists(#count, :start) + :inc',
        ExpressionAttributeNames={'#count': 'count'},
        ExpressionAttributeValues={':inc': 1, ':start': 0},
        ReturnValues='UPDATED_NEW'
    )
    
    # Get the new count
    count = int(response['Attributes']['count'])
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Content-Type': 'application/json'
        },
        'body': json.dumps({'count': count})
    }
