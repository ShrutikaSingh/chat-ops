import json
import boto3

def lambda_handler(event, context):
    body = json.loads(event['body'])
    integration_input = body.get('input', None)
    print(integration_input,"integration input")
    result = integration_logic(integration_input)
    response = call_print_hello_world_lambda(result)
    

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }

def integration_logic(input_data):
    print(input_data,"input data123")
    return input_data * 2

def call_print_hello_world_lambda(result):
    print('test12')
    lambda_client = boto3.client('lambda')
    print('test12', lambda_client)
    # Invoke PrintHelloWorldLambdaFunction
    response = lambda_client.invoke(
        FunctionName='PrintHelloWorldLambdaFunction',
        InvocationType='RequestResponse',
        Payload=json.dumps({'result': result})
    )

    return json.load(response['Payload'])
