import requests, os, json
import time, base64
from copy import deepcopy

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
        self.quizId = ''
        self.transactionId = ''
        self.responseUniqueId = ''
        self.questions = []
        self.answers = []



    ## @fn create_user : endpoint allows user to register.
    #
    def create_user(self, firstName='', lastName='', email='', phone='',
                    companyAdminKey='', country='', firstNameExclude=False,
                    lastNameExclude=False, emailExclude=False, phoneExclude=False,
                    companyAdminKeyExclude=False, countryExclude=False, sandBox=False):
        
        url = self.environment + data["createUser"]

        if sandBox == True:
            headers = {
                'Content-Type' : 'application/json',
                'authKey' : data["sandBoxAuthKey"]
            }
        else:
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
                    lastNameExclude=False, sandBox=False):
        
        url = self.environment + data["updateUser"]
        
        if sandBox == True:
            headers = {
                'Content-Type' : 'application/json',
                'authKey' : data["sandBoxAuthKey"]
            }
        else:
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
    def get_user(self, accessCode='', accessCodeExclude=False, sandBox=False):
        
        url = self.environment + data["getUser"]
        
        if sandBox == True:
            headers = {
                'Content-Type' : 'application/json',
                'authKey' : data["sandBoxAuthKey"]
            }
        else:
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
    def verify_phone(self, accessCode='', accessCodeExclude=False, sandBox=False):
        
        url = self.environment + data["verifyPhone"]
        
        if sandBox == True:
            headers = {
                'Content-Type' : 'application/json',
                'authKey' : data["sandBoxAuthKey"]
            }
        else:
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
                          smsCodeExclude=False, sandBox=False):
        
        url = self.environment + data["verifyPhoneCode"]
        
        if sandBox == True:
            headers = {
                'Content-Type' : 'application/json',
                'authKey' : data["sandBoxAuthKey"]
            }
        else:
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
    def verify_email(self, accessCode='', accessCodeExclude=False, sandBox=False):
        
        url = self.environment + data["verifyEmail"]
        
        if sandBox == True:
            headers = {
                'Content-Type' : 'application/json',
                'authKey' : data["sandBoxAuthKey"]
            }
        else:
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
                              socialMediaUserIdExclude=False, sandBox=False):
        
        url = self.environment + data["verifySocialNetworks"]
        
        if sandBox == True:
            headers = {
                'Content-Type' : 'application/json',
                'authKey' : data["sandBoxAuthKey"]
            }
        else:
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
    def get_available_social_networks(self, accessCode='', accessCodeExclude=False,
                                      sandBox=False):
        
        url = self.environment + data["getAvailableSocialNetworks"]
        
        if sandBox == True:
            headers = {
                'Content-Type' : 'application/json',
                'authKey' : data["sandBoxAuthKey"]
            }
        else:
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



    ## @fn compare_photo : This is used to complete the photo verification process.
    #                      Endpt takes 2 base64 imgs.
    #                      Does not return an indicator as to whether or not they 
    #                      actually passed the photo verification, this endpoint 
    #                      returns a success if the two images sent were successfully 
    #                      uploaded and saved to the database.
    #
    def compare_photo(self, accessCode='', img1='', img2='',
                      accessCodeExclude=False, img1Exclude=False,
                      img2Exclude=False, sandBox=False):
        
        url = self.environment + data["comparePhotos"]
        
        if sandBox == True:
            headers = {
                'Content-Type' : 'application/json',
                'authKey' : data["sandBoxAuthKey"]
            }
        else:
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




    ## @fn check_upload_id : used to determine if the uploadId process has finished.
    #
    def check_upload_id(self, accessCode='', accessCodeExclude=False, sandBox=False):
        
        url = self.environment + data["checkUploadId"]
        
        if sandBox == True:
            headers = {
                'Content-Type' : 'application/json',
                'authKey' : data["sandBoxAuthKey"]
            }
        else:
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



    ## @fn upload_id : 
    
    #
    def upload_id(self, accessCode='', idFront='', idBack='',
                      accessCodeExclude=False, idBackExclude=False,
                      idFrontExclude=False, sandBox=False):
        
        url = self.environment + data["uploadId"]
        
        if sandBox == True:
            headers = {
                'Content-Type' : 'application/json',
                'authKey' : data["sandBoxAuthKey"]
            }
        else:
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
        
        if idBackExclude == True:
            pass
        elif idBack != '':
            body['idBack'] = idBack
        else:
            body['idBack'] = ''

        if idFrontExclude == True:
            pass
        elif idFront != '':
            body['idFront'] = idFront
        else:
            body['idFront'] = ''

        response = requests.request('POST', url, json=body, headers=headers, verify=False)
    
        responseBody = response.json()

        # resultMessage == key
        if TestOutput == True:
            print('\nupload_id\n', responseBody)
            print('\nresponse.text\n', response.text)
            print('\nresponse.status_code: ', response.status_code)
        
        return responseBody



    ## @fn upload_id_enhanced : This is different from uploadId in that it is a 
    #                           more rigorous check and is harder to pass
    #
    def upload_id_enhanced(self, accessCode='', idFront='', idBack='',
                            accessCodeExclude=False, idBackExclude=False,
                            idFrontExclude=False, sandBox=False):
        
        url = self.environment + data["uploadEnhancedId"]
        
        if sandBox == True:
            headers = {
                'Content-Type' : 'application/json',
                'authKey' : data["sandBoxAuthKey"]
            }
        else:
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
        
        if idBackExclude == True:
            pass
        elif idBack != '':
            body['idBack'] = idBack
        else:
            body['idBack'] = ''

        if idFrontExclude == True:
            pass
        elif idFront != '':
            body['idFront'] = idFront
        else:
            body['idFront'] = ''

        response = requests.request('POST', url, json=body, headers=headers, verify=False)
    
        responseBody = response.json()

        # resultMessage == key
        if TestOutput == True:
            print('\nupload_id_enhanced\n', responseBody)
            print('\nresponse.text\n', response.text)
            print('\nresponse.status_code: ', response.status_code)
        
        return responseBody



    ## @fn upload_passport : This will upload a front of a passport to check the data
    #
    def upload_passport(self, accessCode='', idFront='',
                        accessCodeExclude=False, idFrontExclude=False, 
                        sandBox=False):
        
        url = self.environment + data["uploadPassport"]
        
        if sandBox == True:
            headers = {
                'Content-Type' : 'application/json',
                'authKey' : data["sandBoxAuthKey"]
            }
        else:
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

        if idFrontExclude == True:
            pass
        elif idFront != '':
            body['idFront'] = idFront
        else:
            body['idFront'] = ''

        response = requests.request('POST', url, json=body, headers=headers, verify=False)
    
        responseBody = response.json()

        # resultMessage == key
        if TestOutput == True:
            print('\nupload_passport\n', responseBody)
            print('\nresponse.text\n', response.text)
            print('\nresponse.status_code: ', response.status_code)
        
        return responseBody



    ## @fn check_upload_passport :  check if the uploadPassport call was successful.
    #
    def check_upload_passport(self, accessCode='', accessCodeExclude=False, sandBox=False):
        
        url = self.environment + data["checkUploadPassport"]
        
        if sandBox == True:
            headers = {
                'Content-Type' : 'application/json',
                'authKey' : data["sandBoxAuthKey"]
            }
        else:
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
            print('\ncheck_upload_passport\n', responseBody)
            print('\nresponse.status_code: ', response.status_code)
        
        return responseBody



    ## @fn set_social_networks : This is different from uploadId in that it is a 
    #                           more rigorous check and is harder to pass
    #
    def set_social_networks(self, companyAdminKey='', networks=[],
                            companyAdminKeyExclude=False, 
                            networksExclude=False, sandBox=False):
        
        url = self.environment + data["setSocialNetworks"]
        
        if sandBox == True:
            headers = {
                'Content-Type' : 'application/json',
                'authKey' : data["sandBoxAuthKey"]
            }
        else:
            headers = {
                'Content-Type' : 'application/json',
                'authKey' : data["authKey"]
            }
        
        body = {}
        
        if companyAdminKeyExclude == True:
            pass
        elif companyAdminKey != '':
            body['companyAdminKey'] = companyAdminKey
        else:
            body['companyAdminKey'] = ''
        
        if networksExclude == True:
            pass
        elif networks != '' and networks != []:
            body['networks'] = networks
        else:
            body['networks'] = []

        response = requests.request('POST', url, json=body, headers=headers, verify=False)
    
        responseBody = response.json()

        # resultMessage == key
        if TestOutput == True:
            print('\nset_social_networks\n', responseBody)
            print('\nresponse.status_code: ', response.status_code)
        
        return responseBody



    ## @fn set_contract_required : Set whether or not phone and email verification are 
    #                              both needed for the contact verified test.
    #
    def set_contract_required(self, companyAdminKey='', isPhoneRequired=True,
                              isEmailRequired=True, companyAdminKeyExclude=False, 
                              isPhoneRequiredExclude=False, isEmailRequiredExclude=False,
                              sandBox=False):
        
        url = self.environment + data["setContactRequired"]
        
        if sandBox == True:
            headers = {
                'Content-Type' : 'application/json',
                'authKey' : data["sandBoxAuthKey"]
            }
        else:
            headers = {
                'Content-Type' : 'application/json',
                'authKey' : data["authKey"]
            }
        
        body = {}
        
        if companyAdminKeyExclude == True:
            pass
        elif companyAdminKey != '':
            body['companyAdminKey'] = companyAdminKey
        else:
            body['companyAdminKey'] = ''
        
        if isPhoneRequiredExclude == True:
            pass
        elif isPhoneRequired != '':
            body['isPhoneRequired'] = isPhoneRequired
        else:
            body['isPhoneRequired'] = ''

        if isEmailRequiredExclude == True:
            pass
        elif isEmailRequired != '':
            body['isEmailRequired'] = isEmailRequired
        else:
            body['isEmailRequired'] = ''

        response = requests.request('POST', url, json=body, headers=headers, verify=False)
    
        responseBody = response.json()

        # resultMessage == key
        if TestOutput == True:
            print('\nset_contract_required\n', responseBody)
            print('\nresponse.status_code: ', response.status_code)
        
        return responseBody



    ## @fn set_photo_match_per : set the minimum photo match percent 
    #                            needed to pass the photo proof test check. 
    #
    def set_photo_match_per(self, companyAdminKey='', percent=40,
                            companyAdminKeyExclude=False, 
                            percentExclude=False, sandBox=False):
        
        url = self.environment + data["setPhotoMatchPercent"]
        
        if sandBox == True:
            headers = {
                'Content-Type' : 'application/json',
                'authKey' : data["sandBoxAuthKey"]
            }
        else:
            headers = {
                'Content-Type' : 'application/json',
                'authKey' : data["authKey"]
            }
        
        body = {}
        
        if companyAdminKeyExclude == True:
            pass
        elif companyAdminKey != '':
            body['companyAdminKey'] = companyAdminKey
        else:
            body['companyAdminKey'] = ''
        
        if percentExclude == True:
            pass
        elif percent != '':
            body['percent'] = percent
        else:
            body['percent'] = None

        response = requests.request('POST', url, json=body, headers=headers, verify=False)
    
        responseBody = response.json()

        # resultMessage == key
        if TestOutput == True:
            print('\nset_photo_match_per\n', responseBody)
            print('\nresponse.status_code: ', response.status_code)
        
        return responseBody



    ## @fn set_days_expire : set the maximum number of days (24 hour periods) in 
    #                        which a person can complete their test within. 
    #
    def set_days_expire(self, companyAdminKey='', days=10,
                        companyAdminKeyExclude=False, daysExclude=False, 
                        sandBox=False):
        
        url = self.environment + data["setDaysToExpire"]
        
        if sandBox == True:
            headers = {
                'Content-Type' : 'application/json',
                'authKey' : data["sandBoxAuthKey"]
            }
        else:
            headers = {
                'Content-Type' : 'application/json',
                'authKey' : data["authKey"]
            }
        
        body = {}
        
        if companyAdminKeyExclude == True:
            pass
        elif companyAdminKey != '':
            body['companyAdminKey'] = companyAdminKey
        else:
            body['companyAdminKey'] = ''
        
        if daysExclude == True:
            pass
        elif days != '':
            body['days'] = days
        else:
            body['days'] = None

        response = requests.request('POST', url, json=body, headers=headers, verify=False)
    
        responseBody = response.json()

        # resultMessage == key
        if TestOutput == True:
            print('\nset_days_expire\n', responseBody)
            print('\nresponse.status_code: ', response.status_code)
        
        return responseBody



    ## @fn get_test_result :  This endpoint allow a company to query the user's test results.
    #
    def get_test_result(self, accessCode='', companyAdminKey='', 
                        accessCodeExclude=False, companyAdminKeyExclude=False,
                        sandBox=False):
        
        url = self.environment + data["getTestResult"]
        
        if sandBox == True:
            headers = {
                'Content-Type' : 'application/json',
                'authKey' : data["sandBoxAuthKey"]
            }
        else:
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



    ## @fn get_test_results :  This endpoint allow a company to query the user's test results.
    #
    def get_test_results(self, accessCodes=[], companyAdminKey='', 
                        accessCodesExclude=False, companyAdminKeyExclude=False,
                        sandBox=False):
        
        url = self.environment + data["getTestResults"]
        
        if sandBox == True:
            headers = {
                'Content-Type' : 'application/json',
                'authKey' : data["sandBoxAuthKey"]
            }
        else:
            headers = {
                'Content-Type' : 'application/json',
                'authKey' : data["authKey"]
            }
        
        body = {}
        
        if accessCodesExclude == True:
            pass
        elif accessCodes != '' and accessCodes != []:
            body['accessCodes'] = accessCodes
        else:
            body['accessCodes'] = []

        if companyAdminKeyExclude == True:
            pass
        elif companyAdminKey != '':
            body['companyAdminKey'] = companyAdminKey
        else:
            body['companyAdminKey'] = ''

        response = requests.request('POST', url, json=body, headers=headers, verify=False)
    
        responseBody = response.json()
        
        if TestOutput == True:
            print('\nget_test_results\n', responseBody)
            print('\nresponse.status_code: ', response.status_code)
        
        return responseBody



    ## @fn get_quiz :  This will return a quiz object for a user if they have 
    #                  enough information to do so
    #
    def get_quiz(self, accessCodes=[], accessCodesExclude=False,
                 sandBox=False):

        choiceList = []
        questionId = ''

        url = self.environment + data["getQuiz"]
        
        if sandBox == True:
            headers = {
                'Content-Type' : 'application/json',
                'authKey' : data["sandBoxAuthKey"]
            }
        else:
            headers = {
                'Content-Type' : 'application/json',
                'authKey' : data["authKey"]
            }
        
        body = {}
        
        if accessCodesExclude == True:
            pass
        elif accessCodes != '':
            body['accessCodes'] = accessCodes
        else:
            body['accessCodes'] = ''

        response = requests.request('POST', url, json=body, headers=headers, verify=False)
    
        responseBody = response.json()

        # self.questions = []

        if TestOutput == True:
            print('\nget_quiz\n', responseBody)
            print('\nresponse.status_code: ', response.status_code)

        # Capture general quiz data.
        if response.status_code == 200:
            self.transactionId = responseBody['transactionID']
            self.responseUniqueId = responseBody['responseUniqueId']
            self.quizId = responseBody['quizId']

        # Capture specific quiz data in format below.
        # [{'nsquestionId':['nschoiceId', 'nschoiceId', 'nschoiceId', 'nschoiceId']},
        #  {'nsquestionId':['nschoiceId', 'nschoiceId', 'nschoiceId', 'nschoiceId']},
        #  {'nsquestionId':['nschoiceId', 'nschoiceId', 'nschoiceId', 'nschoiceId']},
        #  {'nsquestionId':['nschoiceId', 'nschoiceId', 'nschoiceId', 'nschoiceId']},
        # ]
        for i in range(len(responseBody['question'])):
            # Get the question Id. 
            questionId = responseBody['question'][i]['nsquestionId']

            # Then get all the answer id attached to said question id.
            for x in range(len(responseBody['question'][i]['choice'])):
                choiceList.append(responseBody['question'][i]['choice'][x]['nschoiceId'])
            
            # Now combine the two into a list of dictionary [question:{answers}]
            self.questions.append({questionId:deepcopy(choiceList)})
            choiceList.clear()

        return responseBody



    def GetUserId(self):
        return self.UserId
    
    def GetAccessCode(self):
        return self.AccessCode

    def GetQuizId(self):
        return self.quizId
    
    def GetTransactionId(self):
        return self.transactionId
    
    def GetResponseUniqueId(self):
        return self.responseUniqueId
    
    def GetQuestions(self):
        return self.questions


## Hard coded function to take real DL pictures. Hard coded for security & ease of testing.
def base64Encode():
    with open("C:\\Users\\lescobar-driver\\Documents\Authenticating\\Authenticating\\src\\qa\\assets\\dlfront.jpg", "rb") as dlFront:
        encoded_img_front = base64.b64encode(dlFront.read())
    
    with open("C:\\Users\\lescobar-driver\\Documents\Authenticating\\Authenticating\\src\\qa\\assets\\dlback.jpg", "rb") as dlBack:
        encoded_img_back = base64.b64encode(dlBack.read())

    return encoded_img_front.decode('UTF-8'), encoded_img_back.decode('UTF-8')





def testClass():
    # Declare class objects. Create class instance. DONE
    user = Authenticate()


    # Method signature. DONE
    # create_user(self, firstName='', lastName='', email='', phone='',
    #             companyAdminKey='', country='', firstNameExclude=False,
    #             lastNameExclude=False, emailExclude=False, phoneExclude=False,
    #             companyAdminKeyExclude=False, countryExclude=False):
    user.create_user(data["firstName"], data["lastName"], data["email"], 
                     data["phone"], data["company_admin_key"], data["country"],
                     sandBox=False)


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
    #                  data["updatedFirstName"], data["updatedLastName"], 
    #                  sandBox=False)


    # Day/Year is still broke - 'snow' works


    # # Method signature. DONE
    # # def get_user(self, accessCode='', accessCodeExclude=False):             
    # user.get_user(user.GetAccessCode(), sandBox=False)



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



    # # Method signature. DONE
    # # def compare_photo(self, accessCode='', img1='', img2='',
    # #                   accessCodeExclude=False, img1Exclude=False,
    # #                   img2Exclude=False):
    # user.compare_photo(user.GetAccessCode(), data['my_selfie_1'], data['my_selfie_2'])


    # front, back = base64Encode()


    # # Method signature. BROKEN
    # # def upload_id(self, accessCode='', idFront='', idBack='',
    # #                   accessCodeExclude=False, idBackExclude=False,
    # #                   idFrontExclude=False, sandBox=False):
    # user.upload_id(user.GetAccessCode(), front, back, sandBox=True)


    # # Method signature. BROKEN
    # # def upload_id_enhanced(self, accessCode='', idFront='', idBack='',
    # #                         accessCodeExclude=False, idBackExclude=False,
    # #                         idFrontExclude=False, sandBox=False):
    # user.upload_id_enhanced(user.GetAccessCode(), front, back, sandBox=True)


    # time.sleep(30)


    # # Method signature. BROKEN
    # # def check_upload_id(self, accessCode='', accessCodeExclude=False):
    # user.check_upload_id(user.GetAccessCode(), sandBox=True)


    # # Method signature. BROKEN
    # # def upload_passport(self, accessCode='', idFront='',
    # #                     accessCodeExclude=False, idFrontExclude=False, 
    # #                     sandBox=False):
    # user.upload_passport(user.GetAccessCode(), data['passport_good'], sandBox=True)


    # time.sleep(30)


    # # Method signature. DONE
    # # def check_upload_passport(self, accessCode='', accessCodeExclude=False, sandBox=False):
    # user.check_upload_passport(user.GetAccessCode(), sandBox=True)



    # # Method signature. DONE
    # # def set_social_networks(self, companyAdminKey='', networks=[],
    # #                         companyAdminKeyExclude=False, 
    # #                         networksExclude=False, sandBox=False):
    # user.set_social_networks(data['company_admin_key'], data['testNetworks'])



    # # Method signature. DONE
    # # def set_contract_required(self, companyAdminKey='', isPhoneRequired=True,
    # #                           isEmailRequired=True, companyAdminKeyExclude=False, 
    # #                           isPhoneRequiredExclude=False, isEmailRequiredExclude=False,
    # #                           sandBox=False):
    # user.set_contract_required(data['company_admin_key'], False, False)


    # # Method signature. DONE
    # # def set_photo_match_per(self, companyAdminKey='', percent=40,
    # #                         companyAdminKeyExclude=False, 
    # #                         percentExclude=False, sandBox=False):
    # user.set_photo_match_per(data['company_admin_key'], 40)



    # # Method signature. DONE
    # # def set_days_expire(self, companyAdminKey='', days=10,
    # #                     companyAdminKeyExclude=False, daysExclude=False, 
    # #                     sandBox=False):
    # user.set_days_expire(data['company_admin_key'], 10)






    # # Method signature. WORKING ON THIS STILL
    # # def get_test_result(self, accessCode='', companyAdminKey='', 
    # #                     accessCodeExclude=False, companyAdminKeyExclude=False,
    # #                     sandBox=False):
    # user.get_test_result(user.GetAccessCode(), data['company_admin_key'], sandBox=True)



    # # Method signature.WORKING ON THIS STILL 
    # # def get_test_results(self, accessCode=[], companyAdminKey='', 
    # #                     accessCodeExclude=False, companyAdminKeyExclude=False,
    # #                     sandBox=False):
    # user.get_test_results([user.GetAccessCode(), user.GetAccessCode()], data['company_admin_key'], sandBox=True)



    # Method signature. 
    # def get_quiz(self, accessCodes=[], accessCodesExclude=False,
    #              sandBox=False):
    response = user.get_quiz(user.GetAccessCode(), sandBox=True)
    response = user.GetQuestions()
    print(response)

    # for keys in response:
    #     if keys == 'question':
    #         print()
    #         print()
    #         for i in range(len(response[keys])):
    #             print()
    #             for inKeys in response[keys][i]:
    #                 print(inKeys, ":", response[keys][i][inKeys])
    #     else:
    #         print(keys, response[keys])



testClass()


# list1 = []
# dict1 = {'test':666}
# list1.append(dict1)
# list1.append({'random':6666})
# list1.append({'test':'new data'})

# print(list1)
# print(len(list1))


# list1[0]['test'] = 101010


# print(list1)
# print(len(list1))


# [{'nsquestionId':['nschoiceId', 'nschoiceId', 'nschoiceId', 'nschoiceId']},
#  {'nsquestionId':['nschoiceId', 'nschoiceId', 'nschoiceId', 'nschoiceId']},
#  {'nsquestionId':['nschoiceId', 'nschoiceId', 'nschoiceId', 'nschoiceId']},
#  {'nsquestionId':['nschoiceId', 'nschoiceId', 'nschoiceId', 'nschoiceId']},
# ]

