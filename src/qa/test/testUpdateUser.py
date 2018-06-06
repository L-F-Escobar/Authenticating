import sys, unittest, AuthenticateShell

'''
    Authenticate update user end point.
    
    Purpose - allows an active user to update their account information
    
    Notes - 

    Method signature:
        def update_user(self, accessCode='', address='', city='', state='',
                   zipCode='', phone='', month=0, day=0, year=0,
                   firstName='', lastName='', accessCodeExclude=False,
                   addressExclude=False, cityExclude=False, stateExclude=False,
                   zipCodeExclude=False, phoneExclude=False, monthExclude=False,
                   dayExclude=False, yearExclude=False, firstNameExclude=False,
                   lastNameExclude=False):
    
    Required:
        accessCode
        address
        city
        state
        zipCode
        phone
        month
        day
        year
        firstName
        lastName

    Test cases
        Successfully update a user.

        AccessCode missing from request call.
        Null AccessCode value. 
        Int AccessCode value.    
        Float AccessCode value.   
        String AccessCode value.
        Array AccessCode value. 

        Address missing from request call.
        Null Address value. 
        Int Address value.    
        Float Address value.   
        String Address value.
        Array Address value. 

        City missing from request call.
        Null City value. 
        Int City value.    
        Float City value.   
        String City value.
        Array City value. 

        State missing from request call.
        Null State value. 
        Int State value.    
        Float State value.   
        String State value.
        Array State value. 

        ZipCode missing from request call.
        Null ZipCode value. 
        Int ZipCode value.    
        Float ZipCode value.   
        String ZipCode value.
        Array ZipCode value. 

        Phone missing from request call.
        Null Phone value. 
        Int Phone value.    
        Float Phone value.   
        String Phone value.
        Array Phone value. 

        Month missing from request call.
        Null Month value. 
        Int Month value.    
        Float Month value.   
        String Month value.
        Array Month value. 

        Day missing from request call.
        Null Day value. 
        Int Day value.    
        Float Day value.   
        String Day value.
        Array Day value. 

        Year missing from request call.
        Null Year value. 
        Int Year value.    
        Float Year value.   
        String Year value.
        Array Year value. 

        FirstName missing from request call.
        Null FirstName value. 
        Int FirstName value.    
        Float FirstName value.   
        String FirstName value.
        Array FirstName value.  

        LastName missing from request call.
        Null LastName value. 
        Int LastName value.    
        Float LastName value.   
        String LastName value.
        Array LastName value. 
'''
class TestUpdateUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        try:
            cls.user = AuthenticateShell.Authenticate()      
            cls.user.create_user(firstName = AuthenticateShell.data["firstName"], 
                                lastName = AuthenticateShell.data["lastName"], 
                                email = AuthenticateShell.data["email"], 
                                phone = AuthenticateShell.data["phone"], 
                                companyAdminKey = AuthenticateShell.data["company_admin_key"], 
                                country = AuthenticateShell.data["country"])
        except:
            print("Unexpected error during setUpClass:", sys.exc_info()[0])


    @classmethod
    def tearDownClass(cls):
        try:
            pass
        except:
            print("Unexpected error during tearDownClass:", sys.exc_info()[0])



    # Successfully update a user.
    def test_success(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody['successful'], True,
                         msg='test_success assert#1 has failed.')

        self.assertEqual(responseBody['firstName'], AuthenticateShell.data["updatedFirstName"],
                         msg='test_success assert#2 has failed.')

        self.assertEqual(responseBody['lastName'], AuthenticateShell.data["updatedLastName"],
                         msg='test_success assert#3 has failed.')

        self.assertEqual(responseBody['companyId'], AuthenticateShell.data["company_admin_key"],
                         msg='test_success assert#4 has failed.')

        self.assertEqual(responseBody['userId'], self.user.GetUserId(),
                         msg='test_success assert#5 has failed.')

        self.assertEqual(responseBody['accessCode'], self.user.GetAccessCode(),
                         msg='test_success assert#6 has failed.')



    # *********************************************************************
    # *                         AccessCode tests                            *
    # *********************************************************************
    
    
        
    # Missing AccessCode information from request call.
    def test_missingAccessCode(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"],
                                             accessCodeExclude = True)

        self.assertEqual(responseBody['errorMessage'], "accessCode required",
                         msg='test_missingAccessCode assert#1 has failed.')
        
        
        
    # Test a null AccessCode.
    def test_nullAccessCode(self):
        responseBody = self.user.update_user(accessCode = '', 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody['errorMessage'], "ERR: access code has expired or does not exist",
                          msg='test_nullAccessCode assert#1 has failed.')



    # Test a int AccessCode.
    def test_intAccessCode(self):
        responseBody = self.user.update_user(accessCode = 123456789, 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody['errorMessage'], 
                          "An unknown error has occurred.",
                          msg='test_intAccessCode assert#1 has failed.')



    # Test a float AccessCode.
    def test_floatAccessCode(self):
        responseBody = self.user.update_user(accessCode = 123.321, 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody['errorMessage'], 
                          "An unknown error has occurred.",
                          msg='test_floatAccessCode assert#1 has failed.')
        
        
        
    # Test a string AccessCode value call.
    def test_stringAccessCode(self):
        responseBody = self.user.update_user(accessCode = 'invalid access code', 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody['errorMessage'], 
                          "ERR: access code has expired or does not exist",
                          msg='test_stringAccessCode assert#1 has failed.')



    # Test an array AccessCode value call.
    def test_arrayAccessCode(self):
        responseBody = self.user.update_user(accessCode = [self.user.GetAccessCode()], 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arrayAccessCode assert#1 has failed.')






    # *********************************************************************
    # *                         Address tests                            *
    # *********************************************************************
    
    
        
    # Missing Address information from request call.
    @unittest.skip("Exluding the address does not trigger an error")
    def test_missingAddress(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"],
                                             addressExclude = True)

        self.assertEqual(responseBody[''], "",
                         msg='test_missingAddress assert#1 has failed.')
        
        
        
    # Test a null Address.
    @unittest.skip("Exluding the address does not trigger an error")
    def test_nullAddress(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = '', 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody[''], "",
                          msg='test_nullAddress assert#1 has failed.')



    # Test a int Address.
    @unittest.skip("Address value can be an integer currently")
    def test_intAddress(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = 12345123649874516789, 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody[''], "",
                          msg='test_intAddress assert#1 has failed.')



    # Test a float Address.
    @unittest.skip("Address value can be an float currently")
    def test_floatAddress(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = 1111111111111.11111111111111111111, 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody[''], "",
                          msg='test_floatAddress assert#1 has failed.')
        
        
        
    # Test a string Address value call.
    @unittest.skip("Should always pass by design.")
    def test_stringAddress(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = 'Should pass street', 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody[''], '',
                          msg='test_stringAddress assert#1 has failed.')



    # Test an array Address value call.
    def test_arrayAddress(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = [AuthenticateShell.data["address"]], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arrayAddress assert#1 has failed.')

    


    # *********************************************************************
    # *                         City tests                                *
    # *********************************************************************
    
    
        
    # Missing City information from request call.
    @unittest.skip("Exluding the city does not trigger an error")
    def test_missingCity(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"],
                                             cityExclude = True)

        self.assertEqual(responseBody[''], "",
                         msg='test_missingCity assert#1 has failed.')
        
        
        
    # Test a null City.
    @unittest.skip("Exluding the city does not trigger an error")
    def test_nullCity(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = '',
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody[''], "",
                          msg='test_nullCity assert#1 has failed.')



    # Test a int City.
    @unittest.skip("City value can be an integer currently")
    def test_intCity(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = 3333333333333333333333333333333333,
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody[''], "",
                          msg='test_intCity assert#1 has failed.')



    # Test a float City.
    @unittest.skip("City value can be an float currently")
    def test_floatCity(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = 6666666666666666666666.66666666666,
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody[''], "",
                          msg='test_floatCity assert#1 has failed.')
        
        
        
    # Test a string City value call.
    @unittest.skip("Should always pass by design.")
    def test_stringCity(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = 'AuthenticateShell.data["city"]',
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody[''], '',
                          msg='test_stringCity assert#1 has failed.')



    # Test an array City value call.
    def test_arrayCity(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = [AuthenticateShell.data["city"]],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arrayCity assert#1 has failed.')




    # *********************************************************************
    # *                         State tests                               *
    # *********************************************************************
    
    
        
    # Missing State information from request call.
    @unittest.skip("Exluding the state does not trigger an error")
    def test_missingState(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"],
                                             stateExclude = True)

        self.assertEqual(responseBody[''], "",
                         msg='test_missingState assert#1 has failed.')
        
        
        
    # Test a null State.
    @unittest.skip("Exluding the city does not trigger an error")
    def test_nullState(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = '', 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody[''], "",
                          msg='test_nullState assert#1 has failed.')



    # Test a int State.
    @unittest.skip("State value can be any integer currently")
    def test_intState(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = 12345698798764651341681365168, 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody[''], "",
                          msg='test_intState assert#1 has failed.')



    # Test a float State.
    @unittest.skip("State value can be any float currently")
    def test_floatState(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = 1.2345698798764651341681365168, 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody[''], "",
                          msg='test_floatState assert#1 has failed.')
        
        
        
    # Test a string State value call.
    @unittest.skip("Should always pass by design.")
    def test_stringState(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = 'AuthenticateShell.data["state"]', 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody[''], '',
                          msg='test_stringState assert#1 has failed.')



    # Test an array State value call.
    def test_arrayState(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = [AuthenticateShell.data["state"]], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arrayState assert#1 has failed.')






    # *********************************************************************
    # *                         ZipCode tests                             *
    # *********************************************************************
    
    
        
    # Missing ZipCode information from request call.
    @unittest.skip("Exluding the zipCode does not trigger an error")
    def test_missingZipCode(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"],
                                             zipCodeExclude = True)

        self.assertEqual(responseBody[''], "",
                         msg='test_missingZipCode assert#1 has failed.')
        
        
        
    # Test a null ZipCode.
    @unittest.skip("Exluding the zipCode does not trigger an error")
    def test_nullZipCode(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = '', 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody[''], "",
                          msg='test_nullZipCode assert#1 has failed.')



    # Test a int ZipCode.
    @unittest.skip("ZipCode value can be any integer currently")
    def test_intZipCode(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = 11111111111111111111111111, 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody[''], "",
                          msg='test_intZipCode assert#1 has failed.')



    # Test a float ZipCode.
    @unittest.skip("ZipCode value can be any float currently")
    def test_floatZipCode(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = 1111111111111111111111111.1, 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody[''], "",
                          msg='test_floatZipCode assert#1 has failed.')
        
        
        
    # Test a string ZipCode value call.
    @unittest.skip("Should always pass by design.")
    def test_stringZipCode(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = 'AuthenticateShell.data["zipCode"]', 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody[''], '',
                          msg='test_stringZipCode assert#1 has failed.')



    # Test an array ZipCode value call.
    def test_arrayZipCode(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = [AuthenticateShell.data["zipCode"]], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arrayZipCode assert#1 has failed.')

    


    # *********************************************************************
    # *                         Phone tests                               *
    # *********************************************************************
    
    
        
    # Missing Phone information from request call.
    @unittest.skip("Exluding phone does not trigger an error")
    def test_missingPhone(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"],
                                             phoneExclude = True)

        self.assertEqual(responseBody[''], "",
                         msg='test_missingPhone assert#1 has failed.')
        
        
        
    # Test a null Phone.
    @unittest.skip("Exluding phone does not trigger an error")
    def test_nullPhone(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = '',
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody[''], "",
                          msg='test_nullPhone assert#1 has failed.')



    # Test a int Phone.
    @unittest.skip("Phone value can be any integer currently")
    def test_intPhone(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = 999999999999999999999999999999999999,
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody[''], "",
                          msg='test_intPhone assert#1 has failed.')



    # Test a float Phone.
    @unittest.skip("Phone value can be any float currently")
    def test_floatPhone(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = 999999999.999999999999999999999999999,
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody[''], "",
                          msg='test_floatPhone assert#1 has failed.')
        
        
        
    # Test a string Phone value call.
    @unittest.skip("Phone value can be any string currently")
    def test_stringPhone(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = 'AuthenticateShell.data["phone"]',
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody[''], '',
                          msg='test_stringPhone assert#1 has failed.')



    # Test an array Phone value call.
    def test_arrayPhone(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = [AuthenticateShell.data["phone"]],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arrayPhone assert#1 has failed.')




    # *********************************************************************
    # *                         Month tests                               *
    # *********************************************************************
    
    
        
    # Missing Month information from request call.
    @unittest.skip("Exluding month does not trigger an error")
    def test_missingMonth(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"],
                                             monthExclude = True)

        self.assertEqual(responseBody[''], "",
                         msg='test_missingMonth assert#1 has failed.')
        
        
        
    # Test a null Month.
    @unittest.skip("Exluding month does not trigger an error")
    def test_nullMonth(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = '', 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody[''], "",
                          msg='test_nullMonth assert#1 has failed.')



    # Test a int Month.
    @unittest.skip("Month value can be any integer currently")
    def test_intMonth(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = 666666666666666666666666666666, 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody[''], "",
                          msg='test_intMonth assert#1 has failed.')



    # Test a float Month.
    @unittest.skip("Month value can be any float currently")
    def test_floatMonth(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = 6666666666666.66666666666666666, 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody[''], "",
                          msg='test_floatMonth assert#1 has failed.')
        
        
        
    # Test a string Month value call.
    @unittest.skip("Month value can be any string currently")
    def test_stringMonth(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = 'AuthenticateShell.data["month"]', 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody[''], '',
                          msg='test_stringMonth assert#1 has failed.')



    # Test an array Month value call.
    def test_arrayMonth(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = [AuthenticateShell.data["month"]], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arrayMonth assert#1 has failed.')






    # *********************************************************************
    # *                           Day tests                               *
    # *********************************************************************
    
    
        
    # Missing Day information from request call.
    @unittest.skip("Exluding day does not trigger an error")
    def test_missingDay(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"],
                                             dayExclude = True)

        self.assertEqual(responseBody[''], "",
                         msg='test_missingDay assert#1 has failed.')
        
        
        
    # Test a null Day.
    @unittest.skip("Exluding day does not trigger an error")
    def test_nullDay(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = '', 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody[''], "",
                          msg='test_nullDay assert#1 has failed.')



    # Test a int Day.
    @unittest.skip("Day value can be any integer currently")
    def test_intDay(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = 666666666666666666666666666666, 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody[''], "",
                          msg='test_intDay assert#1 has failed.')



    # Test a float Day.
    @unittest.skip("Day value can be any float currently")
    def test_floatDay(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = 666666666666666666666.666666666, 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody[''], "",
                          msg='test_floatDay assert#1 has failed.')
        
        
        
    # Test a string Day value call.
    @unittest.skip("Day value can be any string currently")
    def test_stringDay(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = 'AuthenticateShell.data["day"]', 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody[''], '',
                          msg='test_stringDay assert#1 has failed.')



    # Test an array Day value call.
    def test_arrayDay(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = [AuthenticateShell.data["day"]], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arrayDay assert#1 has failed.')

    


    # *********************************************************************
    # *                         Year tests                                *
    # *********************************************************************
    
    
        
    # Missing Year information from request call.
    @unittest.skip("Exluding year does not trigger an error")
    def test_missingYear(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"],
                                             yearExclude = True)

        self.assertEqual(responseBody[''], "",
                         msg='test_missingYear assert#1 has failed.')
        
        
        
    # Test a null Year.
    @unittest.skip("Exluding year does not trigger an error")
    def test_nullYear(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = '',
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody[''], "",
                          msg='test_nullYear assert#1 has failed.')



    # Test a int Year.
    @unittest.skip("Year value can be any integer currently")
    def test_intYear(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = 1111111111111111111111111111,
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody[''], "",
                          msg='test_intYear assert#1 has failed.')



    # Test a float Year.
    @unittest.skip("Year value can be any float currently")
    def test_floatYear(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = 1.1111111111111111111111111111,
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody[''], "",
                          msg='test_floatYear assert#1 has failed.')
        
        
        
    # Test a string Year value call.
    @unittest.skip("Year value can be any string currently")
    def test_stringYear(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = 'AuthenticateShell.data["year"]',
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody[''], '',
                          msg='test_stringYear assert#1 has failed.')



    # Test an array Year value call.
    def test_arrayYear(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = [AuthenticateShell.data["year"]],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arrayYear assert#1 has failed.')




    # *********************************************************************
    # *                         FirstName tests                            *
    # *********************************************************************
    
    
        
    # Missing FirstName information from request call.
    @unittest.skip("Exluding firstName does not trigger an error")
    def test_missingFirstName(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"],
                                             firstNameExclude = True)

        self.assertEqual(responseBody[''], "",
                         msg='test_missingFirstName assert#1 has failed.')
        
        
        
    # Test a null FirstName.
    @unittest.skip("Exluding firstName does not trigger an error")
    def test_nullFirstName(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = '', 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody[''], "",
                          msg='test_nullFirstName assert#1 has failed.')



    # Test a int FirstName.
    @unittest.skip("FirstName value can be any integer currently")
    def test_intFirstName(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = 666666666666666666666666, 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody[''], "",
                          msg='test_intFirstName assert#1 has failed.')



    # Test a float FirstName.
    @unittest.skip("FirstName value can be any float currently")
    def test_floatFirstName(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = 6.6666666666666, 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody[''], "",
                          msg='test_floatFirstName assert#1 has failed.')
        
        
        
    # Test a string FirstName value call.
    @unittest.skip("Always pass by design")
    def test_stringFirstName(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = 'AuthenticateShell.data["updatedFirstName"]', 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody[''], '',
                          msg='test_stringFirstName assert#1 has failed.')



    # Test an array FirstName value call.
    def test_arrayFirstName(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = [AuthenticateShell.data["updatedFirstName"]], 
                                             lastName = AuthenticateShell.data["updatedLastName"])

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arrayFirstName assert#1 has failed.')



    # *********************************************************************
    # *                         LastName tests                            *
    # *********************************************************************
    
    
        
    # Missing LastName information from request call.
    @unittest.skip("Exluding firstName does not trigger an error")
    def test_missingLastName(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = AuthenticateShell.data["updatedLastName"],
                                             lastNameExclude = True)

        self.assertEqual(responseBody[''], "",
                         msg='test_missingLastName assert#1 has failed.')
        
        
        
    # Test a null LastName.
    @unittest.skip("Exluding firstName does not trigger an error")
    def test_nullLastName(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = '')

        self.assertEqual(responseBody[''], "",
                          msg='test_nullLastName assert#1 has failed.')



    # Test a int LastName.
    @unittest.skip("LastName value can be any integer currently")
    def test_intLastName(self):
        # Int LastName value.
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = 555555555555555555555)

        self.assertEqual(responseBody[''], "",
                          msg='test_intLastName assert#1 has failed.')



    # Test a float LastName.
    @unittest.skip("LastName value can be any float currently")
    def test_floatLastName(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = 55555555.5555555555)

        self.assertEqual(responseBody[''], "",
                          msg='test_floatLastName assert#1 has failed.')
        
        
        
    # Test a string LastName value call.
    @unittest.skip("Should always pass by design.")
    def test_stringLastName(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = 'AuthenticateShell.data["updatedLastName"]')

        self.assertEqual(responseBody[''], "",
                          msg='test_stringLastName assert#1 has failed.')



    # Test an array LastName value call.
    def test_arrayLastName(self):
        responseBody = self.user.update_user(accessCode = self.user.GetAccessCode(), 
                                             address = AuthenticateShell.data["address"], 
                                             city = AuthenticateShell.data["city"],
                                             state = AuthenticateShell.data["state"], 
                                             zipCode = AuthenticateShell.data["zipCode"], 
                                             phone = AuthenticateShell.data["phone"],
                                             month = AuthenticateShell.data["month"], 
                                             day = AuthenticateShell.data["day"], 
                                             year = AuthenticateShell.data["year"],
                                             firstName = AuthenticateShell.data["updatedFirstName"], 
                                             lastName = [AuthenticateShell.data["updatedLastName"]])

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arrayLastName assert#1 has failed.')



def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestUpdateUser('test_success'))

    suite.addTest(TestUpdateUser('test_missingAccessCode'))
    suite.addTest(TestUpdateUser('test_nullAccessCode'))
    suite.addTest(TestUpdateUser('test_intAccessCode'))
    suite.addTest(TestUpdateUser('test_floatAccessCode'))
    suite.addTest(TestUpdateUser('test_stringAccessCode'))
    suite.addTest(TestUpdateUser('test_arrayAccessCode'))

    suite.addTest(TestUpdateUser('test_missingAddress'))
    suite.addTest(TestUpdateUser('test_nullAddress'))
    suite.addTest(TestUpdateUser('test_intAddress'))
    suite.addTest(TestUpdateUser('test_floatAddress'))
    suite.addTest(TestUpdateUser('test_stringAddress'))
    suite.addTest(TestUpdateUser('test_arrayAddress'))

    suite.addTest(TestUpdateUser('test_missingCity'))
    suite.addTest(TestUpdateUser('test_nullCity'))
    suite.addTest(TestUpdateUser('test_intCity'))
    suite.addTest(TestUpdateUser('test_floatCity'))
    suite.addTest(TestUpdateUser('test_stringCity'))
    suite.addTest(TestUpdateUser('test_arrayCity'))

    suite.addTest(TestUpdateUser('test_missingState'))
    suite.addTest(TestUpdateUser('test_nullState'))
    suite.addTest(TestUpdateUser('test_intState'))
    suite.addTest(TestUpdateUser('test_floatState'))
    suite.addTest(TestUpdateUser('test_stringState'))
    suite.addTest(TestUpdateUser('test_arrayState'))

    suite.addTest(TestUpdateUser('test_missingZipCode'))
    suite.addTest(TestUpdateUser('test_nullZipCode'))
    suite.addTest(TestUpdateUser('test_intZipCode'))
    suite.addTest(TestUpdateUser('test_floatZipCode'))
    suite.addTest(TestUpdateUser('test_stringZipCode'))
    suite.addTest(TestUpdateUser('test_arrayZipCode'))

    suite.addTest(TestUpdateUser('test_missingPhone'))
    suite.addTest(TestUpdateUser('test_nullPhone'))
    suite.addTest(TestUpdateUser('test_intPhone'))
    suite.addTest(TestUpdateUser('test_floatPhone'))
    suite.addTest(TestUpdateUser('test_stringPhone'))
    suite.addTest(TestUpdateUser('test_arrayPhone'))

    suite.addTest(TestUpdateUser('test_missingMonth'))
    suite.addTest(TestUpdateUser('test_nullMonth'))
    suite.addTest(TestUpdateUser('test_intMonth'))
    suite.addTest(TestUpdateUser('test_floatMonth'))
    suite.addTest(TestUpdateUser('test_stringMonth'))
    suite.addTest(TestUpdateUser('test_arrayMonth'))

    suite.addTest(TestUpdateUser('test_missingDay'))
    suite.addTest(TestUpdateUser('test_nullDay'))
    suite.addTest(TestUpdateUser('test_intDay'))
    suite.addTest(TestUpdateUser('test_floatDay'))
    suite.addTest(TestUpdateUser('test_stringDay'))
    suite.addTest(TestUpdateUser('test_arrayDay'))

    suite.addTest(TestUpdateUser('test_missingYear'))
    suite.addTest(TestUpdateUser('test_nullYear'))
    suite.addTest(TestUpdateUser('test_intYear'))
    suite.addTest(TestUpdateUser('test_floatYear'))
    suite.addTest(TestUpdateUser('test_stringYear'))
    suite.addTest(TestUpdateUser('test_arrayYear'))

    suite.addTest(TestUpdateUser('test_missingFirstName'))
    suite.addTest(TestUpdateUser('test_nullFirstName'))
    suite.addTest(TestUpdateUser('test_intFirstName'))
    suite.addTest(TestUpdateUser('test_floatFirstName'))
    suite.addTest(TestUpdateUser('test_stringFirstName'))
    suite.addTest(TestUpdateUser('test_arrayFirstName'))

    suite.addTest(TestUpdateUser('test_missingLastName'))
    suite.addTest(TestUpdateUser('test_nullLastName'))
    suite.addTest(TestUpdateUser('test_intLastName'))
    suite.addTest(TestUpdateUser('test_floatLastName'))
    suite.addTest(TestUpdateUser('test_stringLastName'))
    suite.addTest(TestUpdateUser('test_arrayLastName'))
    
    return suite
    
    
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())