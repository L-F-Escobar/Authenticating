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

# testClass()