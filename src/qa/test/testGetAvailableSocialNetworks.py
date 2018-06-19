import sys, unittest, AuthenticateShell

'''
    Authenticate get available social networks end point.
    
    Purpose - 
    
    Notes - 

    Method signature:
        def get_available_social_networks(self, accessCode='', accessCodeExclude=False):
    
    Required:
        accessCode

    Test cases
        Successfully get all available social networks.

        AccessCode missing from request call.
        Null AccessCode value. 
        Int AccessCode value.    
        Float AccessCode value.   
        String AccessCode value.
        Array AccessCode value.   
'''
class TestGetAvailableSocialNetworks(unittest.TestCase):

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



    # Successfully get available social networks.
    def test_success(self):
        responseBody = self.user.get_available_social_networks(accessCode = self.user.GetAccessCode())

        self.assertEqual(responseBody['networks'][0], 'facebook',
                         msg='test_success assert#1 has failed.')
        
        self.assertEqual(responseBody['networks'][1], 'instagram',
                         msg='test_success assert#2 has failed.')
        
        self.assertEqual(responseBody['networks'][2], 'twitter',
                         msg='test_success assert#3 has failed.')



    # *********************************************************************
    # *                         AccessCode tests                          *
    # *********************************************************************
    
    
        
    # Missing AccessCode information from request call.
    def test_missingAccessCode(self):
        responseBody = self.user.get_available_social_networks(accessCode = self.user.GetAccessCode(),
                                                               accessCodeExclude = True)

        self.assertEqual(responseBody['errorMessage'], "accessCode required",
                         msg='test_missingAccessCode assert#1 has failed.')
        
        
        
    # Test a null AccessCode.
    def test_nullAccessCode(self):
        responseBody = self.user.get_available_social_networks(accessCode = '')

        self.assertEqual(responseBody['errorMessage'], "accessCode required",
                          msg='test_nullAccessCode assert#1 has failed.')



    # Test a int AccessCode.
    def test_intAccessCode(self):
        responseBody = self.user.get_available_social_networks(accessCode = 123852123)

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_intAccessCode assert#1 has failed.')



    # Test a float AccessCode.
    def test_floatAccessCode(self):
        responseBody = self.user.get_available_social_networks(accessCode = 12385212.3)

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_floatAccessCode assert#1 has failed.')
        
        
        
    # Test a string AccessCode value call.
    def test_stringAccessCode(self):
        responseBody = self.user.get_available_social_networks(accessCode = 'self.user.GetAccessCode()')

        self.assertEqual(responseBody['errorMessage'], "access has expired or does not exist",
                          msg='test_stringAccessCode assert#1 has failed.')



    # Test an array AccessCode value call.
    def test_arrayAccessCode(self):
        responseBody = self.user.get_available_social_networks(accessCode = [self.user.GetAccessCode()])

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arrayAccessCode assert#1 has failed.')



def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestGetAvailableSocialNetworks('test_success'))

    suite.addTest(TestGetAvailableSocialNetworks('test_missingAccessCode'))
    suite.addTest(TestGetAvailableSocialNetworks('test_nullAccessCode'))
    suite.addTest(TestGetAvailableSocialNetworks('test_intAccessCode'))
    suite.addTest(TestGetAvailableSocialNetworks('test_floatAccessCode'))
    suite.addTest(TestGetAvailableSocialNetworks('test_stringAccessCode'))
    suite.addTest(TestGetAvailableSocialNetworks('test_arrayAccessCode'))

    return suite
    
    
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())