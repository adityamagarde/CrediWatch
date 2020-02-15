from flask import Flask, request, url_for

@app.route("/data", methods=["GET", "POST"])
def get_data():
	if request.method == "POST":
		formDictionary = {}
    	formDictionary['cin']=request.form['cin']
    	formDictionary['company_name']=request.form['company']
    	formDictionary['date_of_registration']=request.form['registration_date']
    	formDictionary['state']=request.form['state']
    	formDictionary['roc']=request.form['roc']
    	formDictionary['company_status']=request.form['status']
    	formDictionary['category']=request.form['category']
    	formDictionary['class']=request.form['class']
    	formDictionary['authorized_capital']=request.form['auth']
    	formDictionary['paidup_capital']=request.form['paid']
    	formDictionary['activity_code']=request.form['code']
    	formDictionary['activity_description']=request.form['desc']
    	formDictionary['registered_office_address']=request.form['address']
    	formDictionary['email']=request.form['email']
        
        
        month = formDictionary['date_of_registration'][:2]
        month_dictionary = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June',
        '07':'July','08':'August','09':'September','10':'October','11':'November','12':'December'}
        formDictionary['month_name']=month_dictionary[month]
        