import azure.functions as func
import pymongo
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = "mongodb://neighborly-app-thinhtth-mongo-db:RSiKFDlMWk1AAu5Ux84E8oJEsxENWOvKp2WjPWIQ1e1w40dl2BUSCsqXZ2Pt5XzYmZOOHUyaf7bqyFYKrSCocw==@neighborly-app-thinhtth-mongo-db.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighborly-app-thinhtth-mongo-db@"  # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url)
        database = client['neighborly-thinhtth-db']
        collection = database['advertisement']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

