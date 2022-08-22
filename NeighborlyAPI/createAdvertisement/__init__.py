import azure.functions as func
import pymongo

def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            url = "mongodb://neighborly-app-thinhtth-mongo-db:RSiKFDlMWk1AAu5Ux84E8oJEsxENWOvKp2WjPWIQ1e1w40dl2BUSCsqXZ2Pt5XzYmZOOHUyaf7bqyFYKrSCocw==@neighborly-app-thinhtth-mongo-db.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighborly-app-thinhtth-mongo-db@"  
            client = pymongo.MongoClient(url)
            database = client['neighborly-thinhtth-db']
            collection = database['advertisement']

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )