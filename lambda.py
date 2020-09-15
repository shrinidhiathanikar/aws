def lambda_handler(event, context):
    print("In lambda handler")
    
    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
        },
        "body": " Hello Team Checking Lambda"
    }
    
    return response
