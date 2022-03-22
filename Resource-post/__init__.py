import logging
import uuid
import azure.functions as func


def main(req: func.HttpRequest, doc: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    req_body = req.get_json()
    id = req_body.get('id')

    if id:
        newdocs = func.DocumentList() 
        req_body = req.get_json()
        y = {"id":id}
        req_body.update(y)
        newproduct_dict = {
            "body": req_body
        }
        newdocs.append(func.Document.from_dict(newproduct_dict))
        doc.set(newdocs)
        
        return func.HttpResponse(f"Hello . This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "Anna vittu ID",
             status_code=200
        )