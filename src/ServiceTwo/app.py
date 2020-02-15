import sys

sys.path.append("..")
import utils_ab

import requests
import fast_json
from flask import Flask, render_template, request, redirect
from ServiceCall import 


app = Flask(__name__)

# TODO - Center the button if possible in user form
# TODO - Change the background if possible


def fetch_data(cin="U93000GJ2020NPL111833"):
    url = "http://127.0.0.1:5000/CustomerDetails/" + cin
    response = requests.get(url)

    return fast_json.loads(response.json())


@app.route('/testOTP')
def test_function_OTP():
    url = "http://127.0.0.1:5000/otp/9884202442"
    return redirect(url)


@app.route('/testAPICall')
def test_function(cin="U93000GJ2020NPL111833"):
    url = "http://127.0.0.1:5000/CustomerDetails/" + cin
    response = requests.get(url)

    print(fast_json.loads(response.json()))

    return 'It works bois'


@app.route('/testAbhinavCode')
def test_function_ab():
    return str(utils_ab.companyValidation("U93000GJ2020NPL111833", "SADBHAVNA SEVA FOUNDATION"))


@app.route('/home')
def user_form():
    return render_template('index.html', name='crediApp')


@app.route("/process", methods=["GET", "POST"])
def get_data():
    formDictionary = {}
    if request.method == "POST":
        formDictionary['CIN'] = request.form['cin']
        formDictionary['COMPANY NAME'] = request.form['company']
        formDictionary['DATE OF REGISTRATION'] = request.form['registration_date']
        formDictionary['STATE'] = request.form['state']
        formDictionary['ROC'] = request.form['roc']
        formDictionary['COMPANY STATUS'] = request.form['status']
        formDictionary['CATEGORY'] = request.form['category']
        formDictionary['CLASS'] = request.form['class']
        formDictionary['COMPANY TYPE'] = 'Non-government'
        formDictionary['AUTHORIZED CAPITAL'] = request.form['authorised']
        formDictionary['PAIDUP CAPITAL'] = request.form['paid']
        formDictionary['ACTIVITY CODE'] = request.form['code']
        formDictionary['ACTIVITY DESCRIPTION'] = request.form['desc']
        formDictionary['REGISTERED OFFICE ADDRESS'] = request.form['address']
        formDictionary['EMAIL'] = request.form['email']

        month = formDictionary['DATE OF REGISTRATION'][5:7]
        print(formDictionary['DATE OF REGISTRATION'])
        print(formDictionary['DATE OF REGISTRATION'][5:7])
        month_dictionary = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June',
                            '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}
        formDictionary['MONTH NAME'] = month_dictionary[month]

    # Call function for company validation
    if utils_ab.companyValidation(formDictionary["CIN"], formDictionary["COMPANY NAME"]):
        
        # TODO - FETCH Data
        serverData = fetch_data(formDictionary["CIN"])
        # TODO - Validation
        if dataValidation(serverData,formDictionary):
        # IF VALIDATED: render the OTP html page and call OTP function
        

    else:
        render_template('notauthentic.html')



if __name__ == '__main__':
    app.run(debug=True, port=8080)
