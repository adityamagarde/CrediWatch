from flask import Flask, request, url_for

@app.route("/data", methods=["GET", "POST"])
def get_data():
	if request.method == "POST":
		formDictionary = {}
    	formDictionary['CIN']=request.form['cin']
    	formDictionary['COMPANY NAME']=request.form['company']
    	formDictionary['DATE OF REGISTRATION']=request.form['registration_date']
    	formDictionary['STATE']=request.form['state']
    	formDictionary['ROC']=request.form['roc']
    	formDictionary['COMPANY STATUS']=request.form['status']
    	formDictionary['CATEGORY']=request.form['category']
    	formDictionary['CLASS']=request.form['class']
        formDictionary['COMPANY TYPE']='Non-government'
    	formDictionary['AUTHORIZED CAPITAL']=request.form['auth']
    	formDictionary['PAIDUP CAPITAL']=request.form['paid']
    	formDictionary['ACTIVITY CODE']=request.form['code']
    	formDictionary['ACTIVITY DESCRIPTION']=request.form['desc']
    	formDictionary['REGISTERED OFFICE ADDRESS']=request.form['address']
    	formDictionary['EMAIL']=request.form['email']
        
        
        month = formDictionary['date_of_registration'][:2]
        month_dictionary = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June',
        '07':'July','08':'August','09':'September','10':'October','11':'November','12':'December'}
        formDictionary['MONTH NAME']=month_dictionary[month]
        