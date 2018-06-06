import sys, unittest, AuthenticateShell

'''
    Authenticate verify phone end point.
    
    Purpose - gets all the user information
    
    Notes - 

    Method signature:
        def verify_phone(self, accessCode='', accessCodeExclude=False): 
    
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
class TestVerifyPhone(unittest.TestCase):

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
        responseBody = self.user.verify_phone(accessCode = self.user.GetAccessCode())

        self.assertEqual(responseBody['successful'], True,
                         msg='test_success assert#1 has failed.')



    # *********************************************************************
    # *                         AccessCode tests                          *
    # *********************************************************************
    
    
        
    # Missing AccessCode information from request call.
    def test_missingAccessCode(self):
        responseBody = self.user.verify_phone(accessCode = self.user.GetAccessCode(),
                                          accessCodeExclude = True)

        self.assertEqual(responseBody['errorMessage'], "access has expired or does not exist",
                         msg='test_missingAccessCode assert#1 has failed.')
        
        
        
    # Test a null AccessCode.
    def test_nullAccessCode(self):
        responseBody = self.user.verify_phone(accessCode = '')

        self.assertEqual(responseBody['errorMessage'], "access has expired or does not exist",
                          msg='test_nullAccessCode assert#1 has failed.')



    # Test a int AccessCode.
    def test_intAccessCode(self):
        responseBody = self.user.verify_phone(accessCode = 1111111111111)

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_intAccessCode assert#1 has failed.')



    # Test a float AccessCode.
    def test_floatAccessCode(self):
        responseBody = self.user.verify_phone(accessCode = 111111111111.1)

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_floatAccessCode assert#1 has failed.')
        
        
        
    # Test a string AccessCode value call.
    def test_stringAccessCode(self):
        responseBody = self.user.verify_phone(accessCode = 'User not found')

        self.assertEqual(responseBody['errorMessage'], "access has expired or does not exist",
                          msg='test_stringAccessCode assert#1 has failed.')



    # Test an array AccessCode value call.
    def test_arrayAccessCode(self):
        responseBody = self.user.verify_phone(accessCode = ['Invalid access code'])

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arrayAccessCode assert#1 has failed.')




def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestVerifyPhone('test_success'))

    suite.addTest(TestVerifyPhone('test_missingAccessCode'))
    suite.addTest(TestVerifyPhone('test_nullAccessCode'))
    suite.addTest(TestVerifyPhone('test_intAccessCode'))
    suite.addTest(TestVerifyPhone('test_floatAccessCode'))
    suite.addTest(TestVerifyPhone('test_stringAccessCode'))
    suite.addTest(TestVerifyPhone('test_arrayAccessCode'))
    
    return suite
    
    
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())