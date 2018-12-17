import json
import datetime


def handler(event, context):
    data = {
        'output': 'Hello World from MS1 - handler',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}

def handler2(event, context):
    data = {
        'output': 'Hello World from MS1 - handler2',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}

