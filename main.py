from foo import Foo
import json


def response(message, status_code):
    print("Status Code", status_code)
    return {
        "statusCode": str(status_code),
        "body": json.dumps(message),
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        },
    }


def hello(event, context):
    """ this is an example """
    foo = Foo()
    results = foo.yo(event)
    return response({"message": results}, 200)
