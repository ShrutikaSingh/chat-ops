import json
import boto3

def lambda_handler(event, context):
    print('LambdaA received event:', json.dumps(event))

    client = boto3.client('lambda', endpoint_url='http://localhost:3001', region_name='us-east-1')

    try:
        response = client.invoke(
            FunctionName='LambdaB',
            InvocationType='RequestResponse',
            Payload=json.dumps(event)
        )
        data = json.loads(response['Payload'].read().decode('utf-8'))
        print('LambdaB invocation result:', data)
        return {
            'statusCode': 200,
            'body': json.dumps(data)
        }
    except Exception as e:
        print('Error invoking LambdaB:', e)
        raise e
