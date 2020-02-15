import re
import requests

from bs4 import BeautifulSoup


def companyValidation(actualCin, actualCompanyName):
    '''
       This function does validation for CIN number and Company Name given by the user

       Parameter:
           actualCin - CIN number given by user,actualCompanyName-Company name given by user
       Returns:
           rating of the customer based on whether they are genuine or not 
    '''
    URL = "https://www.quickcompany.in/company?utf8=%E2%9C%93&q="+actualCin

    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    findCompanyName = soup.find_all('h3', class_='companyname')
    findCin = soup.find_all('div', class_='lighter')

    companyRegex = '>\s+([^<]+)<'
    cinRegex = 'CIN:\s+([^<]+)<'

    companyName = re.search(companyRegex, str(findCompanyName)).group(1)
    cin = re.search(cinRegex, str(findCin)).group(1)
    print("Company Name:", companyName, "CIN:", cin)

    resultCin = cin in actualCin
    print("The entered CIN number is", resultCin)

    sum = 0

    if resultCin:
        sum = 8

    resultCompanyName = companyName.strip() == actualCompanyName.strip()
    print("The entered Company Name is", resultCompanyName)

    if resultCompanyName:
        sum = sum+2

    return sum


def authentication(otp, mobileNo):
    '''
        This function sends an otp to the number for verification
        parameter: otp-randoly generated number to be verified by person
                   mobileNo - Mobile number given by the client
        response : Otp message is sent to mobile number
    '''
    sender = 'SEDEMO'
    apikey = '632s328863w07io97z6794u48cd1i031'
    message = 'Hi+the+otp+is'+otp
    baseurl = 'http://web.springedge.com/api/web/send/?apikey='+apikey

    url = baseurl+'&sender='+sender+'&to=' + \
        mobileNo+'&message='+message+'&format=json'
    response = requests.get(url)

    print('Response:', response, 'request.')


if __name__ == '__main__':
    pass
