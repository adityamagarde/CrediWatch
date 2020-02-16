import sys
import fast_json
import requests
import urllib

sys.path.append("..")
import utils_ab
import ServiceCall

from flask import Flask, render_template, request, redirect




app = Flask(__name__)

formDictionary = {}


def fetchScore(cin="U93000GJ2020NPL111833"):
    url = "http://127.0.0.1:5000/CustomerDetails/score/" + cin
    response = requests.get(url)

    print(response)

    return fast_json.loads(response.json())

def fetch_data(cin="U93000GJ2020NPL111833"):
    url = "http://127.0.0.1:5000/CustomerDetails/" + cin
    response = requests.get(url)

    return fast_json.loads(response.json())


def test_function_OTP(number):
    url = "http://127.0.0.1:5000/otp/" + number
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
        formDictionary['PHONE'] = request.form['phone']

        month = formDictionary['DATE OF REGISTRATION'][5:7]
        month_dictionary = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June',
                            '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}
        formDictionary['MONTH NAME'] = month_dictionary[month]

    if utils_ab.companyValidation(formDictionary["CIN"], formDictionary["COMPANY NAME"]):
        serverData = fetch_data(formDictionary["CIN"])
        
        if ServiceCall.dataValidation(serverData, formDictionary):
            urllib.request.urlopen('http://127.0.0.1:5000/otp/' + formDictionary["PHONE"])
            return render_template('otpVerify_tarun.html', name="otpwalacode")
        else:
            return render_template('validationFail.html', name="not authenticated")
    else:
        return render_template('validationFail.html', name="not authenticated")


@app.route('/otpProcess', methods=["GET", "POST"])
def validate_otp():
    if request.method == "POST":
        formDictionary["OTP"] = request.form['otp']
    
    validation = urllib.request.urlopen("http://127.0.0.1:5000/otpValidate/" + formDictionary["PHONE"] + '/' + formDictionary["OTP"]).read().decode('utf-8')

    print(validation)
    if validation == 'True':
        #TODO - Get scores
        score1 = fetchScore(formDictionary['CIN'])
        score2 = ServiceCall.calculateTotalOtherScore(ServiceCall.calculateIndividualOtherScore(formDictionary['REGISTERED OFFICE ADDRESS'],formDictionary['CIN'],formDictionary['COMPANY NAME'],formDictionary['STATE'],formDictionary['ACTIVITY DESCRIPTION']))
        
        if score1['SCORE'] + score2 > 3.8:
            judgment = "PASS"
        else:
            judgment = "FAIL"
        return render_template('finalResult.html', score1 = score1["SCORE"], score2 = score2, judgment = judgment)
    else:
        #TODO - Fail HTML
        pass

if __name__ == '__main__':
    app.run(debug=True, port=8080)