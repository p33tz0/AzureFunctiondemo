import logging
import json
import azure.functions as func


def main(req: func.HttpRequest, doc:func.DocumentList) -> func.HttpResponse:
    
    logging.info('Python HTTP trigger function processed a request.')
    id = req.route_params.get('id')
    users_json = []

    for item in doc:
        if id == item["body"]["id"]:
            users_json.append(item["body"]) 

    return func.HttpResponse(
            json.dumps(users_json),
            status_code=200,
            mimetype="application/json"            
    )