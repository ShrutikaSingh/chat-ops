# LambdaB/app.py

def lambda_handler(event, context):
    print('LambdaB received event:', event)
    return {
        'statusCode': 200,
        'body': 'Hello World from LambdaB!'
    }
