import sys, unittest, AuthenticateShell

'''
    Authenticate get user end point.
    
    Purpose - gets all the user information
    
    Notes - 

    Method signature:
        def get_user(self, accessCode='', accessCodeExclude=False): 
    
    Required:
        accessCode

    Test cases
        Successfully update a user.

        AccessCode missing from request call.
        Null AccessCode value. 
        Int AccessCode value.    
        Float AccessCode value.   
        String AccessCode value.
        Array AccessCode value.   
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

            cls.user.update_user(accessCode = cls.user.GetAccessCode(), 
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
        responseBody = self.user.get_user(accessCode = self.user.GetAccessCode())

        self.assertEqual(responseBody['successful'], True,
                         msg='test_success assert#1 has failed.')

        self.assertEqual(responseBody['firstName'], AuthenticateShell.data["updatedFirstName"],
                         msg='test_success assert#2 has failed.')

        self.assertEqual(responseBody['lastName'], AuthenticateShell.data["updatedLastName"],
                         msg='test_success assert#3 has failed.')

        self.assertEqual(responseBody['userId'], self.user.GetUserId(),
                         msg='test_success assert#5 has failed.')

        self.assertEqual(responseBody['accessCode'], self.user.GetAccessCode(),
                         msg='test_success assert#6 has failed.')
        
        self.assertEqual(responseBody['email'], AuthenticateShell.data["email"],
                         msg='test_success assert#7 has failed.')
        
        self.assertEqual(responseBody['phone'], AuthenticateShell.data["phone"],
                         msg='test_success assert#8 has failed.')



    # *********************************************************************
    # *                         AccessCode tests                          *
    # *********************************************************************
    
    
        
    # Missing AccessCode information from request call.
    def test_missingAccessCode(self):
        responseBody = self.user.get_user(accessCode = self.user.GetAccessCode(),
                                          accessCodeExclude = True)

        self.assertEqual(responseBody['errorMessage'], "accessCode required",
                         msg='test_missingAccessCode assert#1 has failed.')
        
        
        
    # Test a null AccessCode.
    def test_nullAccessCode(self):
        responseBody = self.user.get_user(accessCode = '')

        self.assertEqual(responseBody['errorMessage'], "accessCode required",
                          msg='test_nullAccessCode assert#1 has failed.')



    # Test a int AccessCode.
    def test_intAccessCode(self):
        responseBody = self.user.get_user(accessCode = 1111111111111)

        self.assertEqual(responseBody['errorMessage'], "User not found",
                          msg='test_intAccessCode assert#1 has failed.')



    # Test a float AccessCode.
    def test_floatAccessCode(self):
        responseBody = self.user.get_user(accessCode = 111111111111.1)

        self.assertEqual(responseBody['errorMessage'], "User not found",
                          msg='test_floatAccessCode assert#1 has failed.')
        
        
        
    # Test a string AccessCode value call.
    def test_stringAccessCode(self):
        responseBody = self.user.get_user(accessCode = 'User not found')

        self.assertEqual(responseBody['errorMessage'], "User not found",
                          msg='test_stringAccessCode assert#1 has failed.')



    # Test an array AccessCode value call.
    def test_arrayAccessCode(self):
        responseBody = self.user.get_user(accessCode = ['Invalid access code'])

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arrayAccessCode assert#1 has failed.')




def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestUpdateUser('test_success'))

    suite.addTest(TestUpdateUser('test_missingAccessCode'))
    suite.addTest(TestUpdateUser('test_nullAccessCode'))
    suite.addTest(TestUpdateUser('test_intAccessCode'))
    suite.addTest(TestUpdateUser('test_floatAccessCode'))
    suite.addTest(TestUpdateUser('test_stringAccessCode'))
    suite.addTest(TestUpdateUser('test_arrayAccessCode'))
    
    return suite
    
    
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())