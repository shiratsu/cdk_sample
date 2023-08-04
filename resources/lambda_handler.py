import json
import os
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
TABLE_NAME = os.environ['TABLE_NAME']

def handler(event, context):
    table = dynamodb.Table(TABLE_NAME)
    statusCode = 200
    try:
        result = table.scan()
        body = json.dumps(result)
    except ClientError as e:
        statusCode = 400
        body = str(e)
    response = {
        'statusCode': statusCode,
        'body': body,
        'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
             }
    }
    return response