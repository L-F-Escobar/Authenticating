import requests, os, json

requests.packages.urllib3.disable_warnings()

# Set test output flag.
# True  - Test print statements will output to console.
# False - No console output.
if 'TESTOUTPUT' not in os.environ.keys():
    TestOutput = False
else:
    TestOutput = bool(os.environ['TESTOUTPUT'])

# FOR TESTING 
TestOutput = True
    
# Get all necessary data.
with open('data.json') as data_file:    
    data = json.load(data_file)


# for testing we will default set an environment
setEnv = data['authenticating_base_url_staging']


'''
    Authenticating Test Automation Shell 
    
    Shell provides a platform to run unittest scripts against. 
    
    Each class method corresponds to an end point. 
    
    Each method contains header/body dictionaries. Dict pairs can be
    entirely excluded or assigned any values, including null.
    
    def example(email='', emailExclude=False):
    
    If emailExclude flag is set to True during the method call, the keypair 
    will not be included in the request.
'''
class Authenticate:
    ## @var Save a BaseURL without API Version.
    BaseURL = setEnv
        
    ## @fn __init__ : Class initializations.
    def __init__(self, env=setEnv):
        self.UserId = ''
        self.AccessCode = ''
        self.environment = env
        



    ## @fn create_user : endpoint allows user to register.
    #
    def create_user(self, firstName='', lastName='', email='', phone='',
                    companyAdminKey='', country='', firstNameExclude=False,
                    lastNameExclude=False, emailExclude=False, phoneExclude=False,
                    companyAdminKeyExclude=False, countryExclude=False):
        
        url = self.environment + data["createUser"]
        
        headers = {
            'Content-Type' : 'application/json',
            'authKey' : data["authKey"]
        }
        
        body = {}
        
        if firstNameExclude == True:
            pass
        elif firstName != '':
            body['firstName'] = firstName
        else:
            body['firstName'] = ''
            
        if lastNameExclude == True:
            pass
        elif lastName != '':
            body['lastName'] = lastName
        else:
            body['lastName'] = ''
        
        if emailExclude == True:
            pass
        elif email != '':
            body['email'] = email
        else:
            body['email'] = ''

        if phoneExclude == True:
            pass
        elif phone != '':
            body['phone'] = phone
        else:
            body['phone'] = ''
        
        if companyAdminKeyExclude == True:
            pass
        elif companyAdminKey != '':
            body['companyAdminKey'] = companyAdminKey
        else:
            body['companyAdminKey'] = ''
        
        if countryExclude == True:
            pass
        elif country != '':
            body['country'] = country
        else:
            body['country'] = ''
            
        response = requests.request('POST', url, json=body, headers=headers, verify=False)
    
        responseBody = response.json()
        
        if TestOutput == True:
            print('\ncreate_user\n', responseBody)
            print('\nresponse.status_code: ', response.status_code)
        
        # Grab the request Id of a successful call.
        if 'successful' in responseBody.keys():
            if responseBody['successful'] == True:
                self.AccessCode = responseBody['accessCode']
                self.UserId = responseBody['userId']
        
        return responseBody



    ## @fn update_user : allows a user profile to be updated.
    #
    def update_user(self, accessCode='', address='', city='', state='',
                    zipCode='', phone='', month=0, day=0, year=0,
                    firstName='', lastName='', accessCodeExclude=False,
                    addressExclude=False, cityExclude=False, stateExclude=False,
                    zipCodeExclude=False, phoneExclude=False, monthExclude=False,
                    dayExclude=False, yearExclude=False, firstNameExclude=False,
                    lastNameExclude=False):
        
        url = self.environment + data["updateUser"]
        
        headers = {
            'Content-Type' : 'application/json',
            'authKey' : data["authKey"]
        }
        
        body = {}
        
        if accessCodeExclude == True:
            pass
        elif accessCode != '':
            body['accessCode'] = accessCode
        else:
            body['accessCode'] = ''

        if addressExclude == True:
            pass
        elif address != '':
            body['address'] = address
        else:
            body['address'] = ''
        
        if cityExclude == True:
            pass
        elif city != '':
            body['city'] = city
        else:
            body['city'] = ''
        
        if stateExclude == True:
            pass
        elif state != '':
            body['state'] = state
        else:
            body['state'] = ''

        if zipCodeExclude == True:
            pass
        elif zipCode != '':
            body['zipCode'] = zipCode
        else:
            body['zipCode'] = ''

        if phoneExclude == True:
            pass
        elif phone != '':
            body['phone'] = phone
        else:
            body['phone'] = ''
        
        if monthExclude == True:
            pass
        elif month != '':
            body['month'] = month
        else:
            body['month'] = ''
        
        if dayExclude == True:
            pass
        elif day != '':
            body['day'] = day
        else:
            body['day'] = ''

        if yearExclude == True:
            pass
        elif year != '':
            body['year'] = year
        else:
            body['year'] = ''

        if firstNameExclude == True:
            pass
        elif firstName != '':
            body['firstName'] = firstName
        else:
            body['firstName'] = ''
            
        if lastNameExclude == True:
            pass
        elif lastName != '':
            body['lastName'] = lastName
        else:
            body['lastName'] = ''
            
        response = requests.request('POST', url, json=body, headers=headers, verify=False)
    
        responseBody = response.json()
        
        if TestOutput == True:
            print('\nupdate_user\n', responseBody)
            print('\nresponse.status_code: ', response.status_code)
        
        # Grab the request Id of a successful call.
        if 'successful' in responseBody.keys():
            if responseBody['successful'] == True:
                self.AccessCode = responseBody['accessCode']
                self.UserId = responseBody['userId']
        
        return responseBody



    def GetUserId(self):
        return self.UserId
    
    def GetAccessCode(self):
        return self.AccessCode


def testClass():
    # Declare class objects. Create class instance. DONE
    user = Authenticate()


    # Method signature. DONE
    # create_user(self, firstName='', lastName='', email='', phone='',
    #             companyAdminKey='', country='', firstNameExclude=False,
    #             lastNameExclude=False, emailExclude=False, phoneExclude=False,
    #             companyAdminKeyExclude=False, countryExclude=False):
    user.create_user(data["firstName"], data["lastName"], data["email"], 
                     data["phone"], data["company_admin_key"], data["country"])


    # Method signature. DONE
    # def update_user(self, accessCode='', address='', city='', state='',
    #                zipCode='', phone='', month=0, day=0, year=0,
    #                firstName='', lastName='', accessCodeExclude=False,
    #                addressExclude=False, cityExclude=False, stateExclude=False,
    #                zipCodeExclude=False, phoneExclude=False, monthExclude=False,
    #                dayExclude=False, yearExclude=False, firstNameExclude=False,
    #                lastNameExclude=False):
    user.update_user(user.GetAccessCode(), data["address"], data["city"],
                     data["state"], data["zipCode"], data["phone"],
                     data["month"], data["day"], data["year"],
                     data["updatedFirstName"], data["updatedLastName"])

# testClass()