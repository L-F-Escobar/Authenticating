import requests, os, json
import time

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



    ## @fn get_user : gets a users information
    #
    def get_user(self, accessCode='', accessCodeExclude=False):
        
        url = self.environment + data["getUser"]
        
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
            
        response = requests.request('POST', url, json=body, headers=headers, verify=False)
    
        responseBody = response.json()
        
        if TestOutput == True:
            print('\nget_user\n', responseBody)
            print('\nresponse.status_code: ', response.status_code)
        
        return responseBody



    ## @fn verify_phone : 
    #
    def verify_phone(self, accessCode='', accessCodeExclude=False):
        
        url = self.environment + data["verifyPhone"]
        
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
            
        response = requests.request('POST', url, json=body, headers=headers, verify=False)
    
        responseBody = response.json()
        
        if TestOutput == True:
            print('\nverify_phone\n', responseBody)
            print('\nresponse.status_code: ', response.status_code)
        
        return responseBody



    ## @fn verify_phone_code : 
    #
    def verify_phone_code(self, accessCode='', smsCode='', accessCodeExclude=False,
                          smsCodeExclude=False):
        
        url = self.environment + data["verifyPhoneCode"]
        
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
            
        if smsCodeExclude == True:
            pass
        elif smsCode != '':
            body['smsCode'] = smsCode
        else:
            body['smsCode'] = ''

        response = requests.request('POST', url, json=body, headers=headers, verify=False)
    
        responseBody = response.json()
        
        if TestOutput == True:
            print('\nverify_phone_code\n', responseBody)
            print('\nresponse.status_code: ', response.status_code)
        
        return responseBody



    ## @fn verify_email : 
    #
    def verify_email(self, accessCode='', accessCodeExclude=False):
        
        url = self.environment + data["verifyEmail"]
        
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
            
        response = requests.request('POST', url, json=body, headers=headers, verify=False)
    
        responseBody = response.json()
        
        if TestOutput == True:
            print('\nverify_email\n', responseBody)
            print('\nresponse.status_code: ', response.status_code)
        
        return responseBody



    ## @fn verify_social_network : 
    #
    def verify_social_network(self, accessCode='', network='', socialMediaAccessToken='',
                              socialMediaUserId='', accessCodeExclude=False,
                              networkExclude=False, socialMediaAccessTokenExclude=False,
                              socialMediaUserIdExclude=False):
        
        url = self.environment + data["verifySocialNetworks"]
        
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

        if networkExclude == True:
            pass
        elif network != '':
            body['network'] = network
        else:
            body['network'] = ''

        if socialMediaAccessTokenExclude == True:
            pass
        elif socialMediaAccessToken != '':
            body['socialMediaAccessToken'] = socialMediaAccessToken
        else:
            body['socialMediaAccessToken'] = ''

        if socialMediaUserIdExclude == True:
            pass
        elif socialMediaUserId != '':
            body['socialMediaUserId'] = socialMediaUserId
        else:
            body['socialMediaUserId'] = ''
            
        response = requests.request('POST', url, json=body, headers=headers, verify=False)
    
        responseBody = response.json()
        
        if TestOutput == True:
            print('\nverify_social_network\n', responseBody)
            print('\nresponse.status_code: ', response.status_code)
        
        return responseBody



    ## @fn get_available_social_networks : 
    #
    def get_available_social_networks(self, accessCode='', accessCodeExclude=False):
        
        url = self.environment + data["getAvailableSocialNetworks"]
        
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

        response = requests.request('POST', url, json=body, headers=headers, verify=False)
    
        responseBody = response.json()
        
        if TestOutput == True:
            print('\nget_available_social_networks\n', responseBody)
            print('\nresponse.status_code: ', response.status_code)
        
        return responseBody



    ## @fn compare_photo : 
    #
    def compare_photo(self, accessCode='', img1='', img2='',
                      accessCodeExclude=False, img1Exclude=False,
                      img2Exclude=False):
        
        url = self.environment + data["comparePhotos"]
        
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
        
        if img1Exclude == True:
            pass
        elif img1 != '':
            body['img1'] = img1
        else:
            body['img1'] = ''

        if img2Exclude == True:
            pass
        elif img2 != '':
            body['img2'] = img2
        else:
            body['img2'] = ''

        response = requests.request('POST', url, json=body, headers=headers, verify=False)
    
        responseBody = response.json()
        
        if TestOutput == True:
            print('\ncompare_photo\n', responseBody)
            print('\nresponse.status_code: ', response.status_code)
        
        return responseBody



    ## @fn get_test_result : 
    #
    def get_test_result(self, accessCode='', companyAdminKey='',
                        accessCodeExclude=False, companyAdminKeyExclude=False):
        
        url = self.environment + data["getTestResult"]
        
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
        
        if companyAdminKeyExclude == True:
            pass
        elif companyAdminKey != '':
            body['companyAdminKey'] = companyAdminKey
        else:
            body['companyAdminKey'] = ''

        response = requests.request('POST', url, json=body, headers=headers, verify=False)
    
        responseBody = response.json()
        
        if TestOutput == True:
            print('\nget_test_result\n', responseBody)
            print('\nresponse.status_code: ', response.status_code)
        
        return responseBody



    ## @fn check_upload_id : 
    #
    def check_upload_id(self, accessCode='', accessCodeExclude=False):
        
        url = self.environment + data["checkUploadId"]
        
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

        response = requests.request('POST', url, json=body, headers=headers, verify=False)
    
        responseBody = response.json()
        
        if TestOutput == True:
            print('\ncheck_upload_id\n', responseBody)
            print('\nresponse.status_code: ', response.status_code)
        
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


    # # Method signature. DONE
    # # def update_user(self, accessCode='', address='', city='', state='',
    # #                zipCode='', phone='', month=0, day=0, year=0,
    # #                firstName='', lastName='', accessCodeExclude=False,
    # #                addressExclude=False, cityExclude=False, stateExclude=False,
    # #                zipCodeExclude=False, phoneExclude=False, monthExclude=False,
    # #                dayExclude=False, yearExclude=False, firstNameExclude=False,
    # #                lastNameExclude=False):
    # user.update_user(user.GetAccessCode(), data["address"], data["city"],
    #                  data["state"], data["zipCode"], data["phone"],
    #                  data["month"], data["day"], data["year"],
    #                  data["updatedFirstName"], data["updatedLastName"])



    # # Method signature. DONE
    # # def get_user(self, accessCode='', accessCodeExclude=False):             
    # user.get_user(user.GetAccessCode())



    # # Method signature. DONE
    # # def verify_phone(self, accessCode='', accessCodeExclude=False):
    # user.verify_phone(user.GetAccessCode())


    # # Method signature. DONE
    # # def verify_phone_code(self, accessCode='', smsCode='', accessCodeExclude=False,
    # #                      smsCodeExclude=False):
    # user.verify_phone_code(user.GetAccessCode(), data["smsCode"])


    # # Method signature. DONE
    # # def verify_email(self, accessCode='', accessCodeExclude=False):
    # user.verify_email(user.GetAccessCode())



    # # Method signature. DONE
    # # def verify_social_network(self, accessCode='', network='', socialMediaAccessToken='',
    # #                           socialMediaUserId='', accessCodeExclude=False,
    # #                           networkExclude=True, socialMediaAccessTokenExclude=True,
    # #                           socialMediaUserIdExclude=True):
    # user.verify_social_network(user.GetAccessCode(), data['network'], 
    #                            data['socialMediaAccessToken'], data['socialMediaUserId'])


    # # Method signature. DONE
    # # def get_available_social_networks(self, accessCode='', accessCodeExclude=False):
    # user.get_available_social_networks(user.GetAccessCode())



    # Method signature. DONE
    # def compare_photo(self, accessCode='', img1='', img2='',
    #                   accessCodeExclude=False, img1Exclude=False,
    #                   img2Exclude=False):
    user.compare_photo(user.GetAccessCode(), data['my_selfie_1'], data['my_selfie_2'])

    time.sleep(60)

    # Method signature. DONE
    # def get_test_result(self, accessCode='', companyAdminKey='',
    #                     accessCodeExclude=False, companyAdminKeyExclude=False):
    user.get_test_result(user.GetAccessCode(), data['company_admin_key'])


    # Method signature. DONE
    # def check_upload_id(self, accessCode='', accessCodeExclude=False):
    user.check_upload_id(user.GetAccessCode())

testClass()