import sys, unittest, AuthenticateShell

'''
    Authenticate verify email end point.
    
    Purpose - 
    
    Notes - 

    Method signature:
        def verify_email(self, accessCode='', accessCodeExclude=False): 
    
    Required:
        accessCode

    Test cases
        Successfully verify a user with their phone.

        AccessCode missing from request call.
        Null AccessCode value. 
        Int AccessCode value.    
        Float AccessCode value.   
        String AccessCode value.
        Array AccessCode value.   
'''
class TestVerifyEmail(unittest.TestCase):

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
        responseBody = self.user.verify_email(accessCode = self.user.GetAccessCode())

        self.assertEqual(responseBody['successful'], True,
                         msg='test_success assert#1 has failed.')



    # *********************************************************************
    # *                         AccessCode tests                          *
    # *********************************************************************
    
    
        
    # Missing AccessCode information from request call.
    def test_missingAccessCode(self):
        responseBody = self.user.verify_email(accessCode = self.user.GetAccessCode(),
                                          accessCodeExclude = True)

        self.assertEqual(responseBody['errorMessage'], "access has expired or does not exist",
                         msg='test_missingAccessCode assert#1 has failed.')
        
        
        
    # Test a null AccessCode.
    def test_nullAccessCode(self):
        responseBody = self.user.verify_email(accessCode = '')

        self.assertEqual(responseBody['errorMessage'], "access has expired or does not exist",
                          msg='test_nullAccessCode assert#1 has failed.')



    # Test a int AccessCode.
    def test_intAccessCode(self):
        responseBody = self.user.verify_email(accessCode = 1111111111111)

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_intAccessCode assert#1 has failed.')



    # Test a float AccessCode.
    def test_floatAccessCode(self):
        responseBody = self.user.verify_email(accessCode = 111111111111.1)

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_floatAccessCode assert#1 has failed.')
        
        
        
    # Test a string AccessCode value call.
    def test_stringAccessCode(self):
        responseBody = self.user.verify_email(accessCode = 'User not found')

        self.assertEqual(responseBody['errorMessage'], "access has expired or does not exist",
                          msg='test_stringAccessCode assert#1 has failed.')



    # Test an array AccessCode value call.
    def test_arrayAccessCode(self):
        responseBody = self.user.verify_email(accessCode = ['Invalid access code'])

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arrayAccessCode assert#1 has failed.')




def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestVerifyEmail('test_success'))

    suite.addTest(TestVerifyEmail('test_missingAccessCode'))
    suite.addTest(TestVerifyEmail('test_nullAccessCode'))
    suite.addTest(TestVerifyEmail('test_intAccessCode'))
    suite.addTest(TestVerifyEmail('test_floatAccessCode'))
    suite.addTest(TestVerifyEmail('test_stringAccessCode'))
    suite.addTest(TestVerifyEmail('test_arrayAccessCode'))
    
    return suite
    
    
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())