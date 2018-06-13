import sys, unittest, AuthenticateShell

'''
    Authenticate set social network end point.
    
    Purpose - 

    Method signature:
        def set_social_networks(self, companyAdminKey='', networks=[],
                                companyAdminKeyExclude=False, 
                                networksExclude=False, sandBox=False):

    Note: THIS END POINT IS BROKEN DUE TO SAND BOXING.

    Required:
        companyAdminKey
        networks

    Test cases
        Successfully set social networks.

        CompanyAdminKey missing from request call.
        Null CompanyAdminKey value. 
        Int CompanyAdminKey value.    
        Float CompanyAdminKey value.   
        String CompanyAdminKey value.
        Array CompanyAdminKey value.   

        Networks missing from request call.
        Null Networks value. 
        Int Networks value.    
        Float Networks value.   
        String Networks value.
        Array Networks value. 
'''
class TestSetSocialNetworks(unittest.TestCase):

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
            cls.user.set_social_networks(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                         networks = AuthenticateShell.data['defaultNetworks'])
        except:
            print("Unexpected error during tearDownClass:", sys.exc_info()[0])



    # Successfully set social networks.
    def test_success(self):
        responseBody = self.user.set_social_networks(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                     networks = AuthenticateShell.data['testNetworks'])

        self.assertEqual(responseBody['successful'], True,
                         msg='test_success assert#1 has failed.')

        responseBody = self.user.get_available_social_networks(self.user.GetAccessCode())

        self.assertEqual(responseBody['networks'], AuthenticateShell.data['testNetworks'],
                         msg='test_success assert#2 has failed.')



    # *********************************************************************
    # *                         CompanyAdminKey tests                     *
    # *********************************************************************
    
    
        
    # Missing CompanyAdminKey information from request call.
    def test_missingCompanyAdminKey(self):
        responseBody = self.user.set_social_networks(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                     networks = AuthenticateShell.data['testNetworks'],
                                                     companyAdminKeyExclude = True)

        self.assertEqual(responseBody['errorMessage'], "company admin key required",
                         msg='test_missingCompanyAdminKey assert#1 has failed.')
        
        
        
    # Test a null CompanyAdminKey.
    def test_nullCompanyAdminKey(self):
        responseBody = self.user.set_social_networks(companyAdminKey = '', 
                                                     networks = AuthenticateShell.data['testNetworks'])

        self.assertEqual(responseBody['errorMessage'], "company admin key required",
                          msg='test_nullCompanyAdminKey assert#1 has failed.')



    # Test a int CompanyAdminKey.
    def test_intCompanyAdminKey(self):
        responseBody = self.user.set_social_networks(companyAdminKey = 1111111111111, 
                                                     networks = AuthenticateShell.data['testNetworks'])

        self.assertEqual(responseBody['errorMessage'], "invalid company admin key",
                          msg='test_intCompanyAdminKey assert#1 has failed.')



    # Test a float CompanyAdminKey.
    def test_floatCompanyAdminKey(self):
        responseBody = self.user.set_social_networks(companyAdminKey = 11.11111111111, 
                                                     networks = AuthenticateShell.data['testNetworks'])

        self.assertEqual(responseBody['errorMessage'], "invalid company admin key",
                          msg='test_floatCompanyAdminKey assert#1 has failed.')
        
        
        
    # Test a string CompanyAdminKey value call.
    def test_stringCompanyAdminKey(self):
        responseBody = self.user.set_social_networks(companyAdminKey = "AuthenticateShell.data['company_admin_key']", 
                                                     networks = AuthenticateShell.data['testNetworks'])

        self.assertEqual(responseBody['errorMessage'], "invalid company admin key",
                          msg='test_stringCompanyAdminKey assert#1 has failed.')



    # Test an array CompanyAdminKey value call.
    def test_arrayCompanyAdminKey(self):
        responseBody = self.user.set_social_networks(companyAdminKey = [AuthenticateShell.data['company_admin_key']], 
                                                     networks = AuthenticateShell.data['testNetworks'])

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arrayCompanyAdminKey assert#1 has failed.')


    
    # *********************************************************************
    # *                          Networks tests                           *
    # *********************************************************************
    
    
        
    # Missing Networks information from request call.
    def test_missingNetworks(self):
        responseBody = self.user.set_social_networks(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                     networks = AuthenticateShell.data['testNetworks'],
                                                     networksExclude = True)

        self.assertEqual(responseBody['errorMessage'], 'please submit networks',
                         msg='test_missingNetworks assert#1 has failed.')
        
        
        
    # Test a null Networks.
    def test_nullNetworks(self):
        responseBody = self.user.set_social_networks(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                     networks = '')

        self.assertEqual(responseBody['successful'], True,
                          msg='test_nullNetworks assert#1 has failed.')

        responseBody = self.user.get_available_social_networks(self.user.GetAccessCode())

        self.assertEqual(responseBody['networks'], [],
                         msg='test_nullNetworks assert#2 has failed.')



    # Test a int Networks.
    def test_intNetworks(self):
        responseBody = self.user.set_social_networks(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                     networks = 123654789)

        self.assertEqual(responseBody['errorMessage'], "please submit networks",
                          msg='test_intNetworks assert#1 has failed.')



    # Test a float Networks.
    def test_floatNetworks(self):
        responseBody = self.user.set_social_networks(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                     networks = 123.654789)

        self.assertEqual(responseBody['errorMessage'], "please submit networks",
                          msg='test_floatNetworks assert#1 has failed.')
        
        
        
    # Test a string Networks value call.
    def test_stringNetworks(self):
        responseBody = self.user.set_social_networks(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                     networks = "AuthenticateShell.data['testNetworks']")

        self.assertEqual(responseBody['errorMessage'], "please submit networks",
                          msg='test_stringNetworks assert#1 has failed.')



    # Test an array Networks value call.
    def test_arrayNetworks(self):
        responseBody = self.user.set_social_networks(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                     networks = [AuthenticateShell.data['testNetworks']])

        self.assertEqual(responseBody['errorMessage'], "please submit networks",
                          msg='test_arrayNetworks assert#1 has failed.')



def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestSetSocialNetworks('test_success'))

    suite.addTest(TestSetSocialNetworks('test_missingCompanyAdminKey'))
    suite.addTest(TestSetSocialNetworks('test_nullCompanyAdminKey'))
    suite.addTest(TestSetSocialNetworks('test_intCompanyAdminKey'))
    suite.addTest(TestSetSocialNetworks('test_floatCompanyAdminKey'))
    suite.addTest(TestSetSocialNetworks('test_stringCompanyAdminKey'))
    suite.addTest(TestSetSocialNetworks('test_arrayCompanyAdminKey'))

    suite.addTest(TestSetSocialNetworks('test_missingNetworks'))
    suite.addTest(TestSetSocialNetworks('test_nullNetworks'))
    suite.addTest(TestSetSocialNetworks('test_intNetworks'))
    suite.addTest(TestSetSocialNetworks('test_floatNetworks'))
    suite.addTest(TestSetSocialNetworks('test_stringNetworks'))
    suite.addTest(TestSetSocialNetworks('test_arrayNetworks'))

    return suite
    
    
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())