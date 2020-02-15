import json
import fast_json

from random import randint
from flask import Flask, request
from flask_restplus import Api, Resource, fields

pathDict = {
    'jsonFilePath': r'../data/dataJson.json'
}

OTP_global = dict()

flaskApp = Flask(__name__)
app = Api(app=flaskApp, version="1.0", title="DataFetcher",
          description="Fetch and display data as per the CIN")

nameSpace = app.namespace('CustomerDetails', description="Random Des.")

with open(pathDict['jsonFilePath'], 'r') as myFile:
    listOfCustomers = json.loads(json.load(myFile))


model = app.model('Data Model', {'COMPANY NAME': fields.String(required=True, description='Name of the company', help="Company name cannot be blank."),
                                 'DATE OF REGISTRATION': fields.String(required=True, description="Date of registration of company", help="Date in the format yyyy-mm-dd"),
                                 'MONTH NAME': fields.String(required=True, description="Month of the registration of company", help="The full spelling must be specified"),
                                 'STATE': fields.String(required=True, description="The state of registration", help="The full name of state shall be provided"),
                                 'ROC': fields.String(required=True, description="The Registrar of Company, the office where the company was registered", help="The RoC (city) shall be specified"),
                                 'COMPANY STATUS': fields.String(required=True, description="If the company is Active or Not", help="String stating Active or Not available for efiling"),
                                 'CATEGORY': fields.String(required=True, description="The category of company defined as limited by shares or guarentee", help="String value defining the category"),
                                 'CLASS': fields.String(required=True, description="The class of company if it is public or private", help="String value defining the class"),
                                 'COMPANY TYPE': fields.String(required=True, description="The company type represents if the company is a Government or Non-Government company", help=""),
                                 'AUTHORIZED CAPITAL': fields.String(required=True, description="The authorized capital of the company", help=""),
                                 'PAIDUP CAPITAL': fields.String(required=True, description="", help=""),
                                 'ACTIVITY MODE': fields.String(required=True, description="", help=""),
                                 'ACTIVITY DESCRIPTION': fields.String(required=True, description="", help=""),
                                 'REGISTERED OFFICE ADDRESS': fields.String(required=True, description="", help=""),
                                 'EMAIL': fields.String(required=True, description="", help="")})


@nameSpace.route("/<cin>")
class MainClass(Resource):
    @app.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'}, params={'id': 'Specify the Id associated with the person'})
    def get(self, cin):
        try:
            information = listOfCustomers[cin]
            a = fast_json.dumps({
                "status": "Information retrieved",
                "company name": information["COMPANY NAME"],
                "date": information["DATE OF REGISTRATION"],
                "state": information["STATE"]
            })

            # return {
            #     "status": "Information retrieved",
            #     "company name": information["COMPANY NAME"],
            #     "date": information["DATE OF REGISTRATION"],
            #     "state": information["STATE"]
            # }
            return a
        except KeyError as e:
            nameSpace.abort(
                500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            nameSpace.abort(
                400, e.__doc__, status="Could not retrieve information", statusCode="400")


def otp_generator():
    '''
        A function that uses the random function in python to generate OTP

        Parameters:
            None
        Returns:
            OTP - The randomly generated OTP
    '''
    OTP = randint(10000, 99999)
    return OTP


@flaskApp.route('/otp/<mob>')
def A(mob):
    # TODO - Add abhinav's function
    otp = otp_generator()
