import sys, unittest, AuthenticateShell

'''
    Authenticate set days to expire end point.
    
    Purpose - set the maximum number of days (24 hour periods) in 
              which a person can complete their test within. 
              
    Notes - THIS HAS BEEN CONFIRMED THROUGH MANUAL DATABASE AUTHENTICATION.

    Method signature:
        def set_days_expire(self, companyAdminKey='', days=10,
                        companyAdminKeyExclude=False, daysExclude=False, 
                        sandBox=False):

    Required:
        companyAdminKey
        days

    Test cases
        Successfully set days to expire.

        CompanyAdminKey missing from request call.
        Null CompanyAdminKey value. 
        Int CompanyAdminKey value.    
        Float CompanyAdminKey value.   
        String CompanyAdminKey value.
        Array CompanyAdminKey value.   

        Days missing from request call.
        Null Days value. 
        Int Days value.    
        Float Days value.   
        String Days value.
        Array Days value. 
'''
class TestSetDayExpire(unittest.TestCase):

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
            cls.user.set_days_expire(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                     days = 10)
        except:
            print("Unexpected error during tearDownClass:", sys.exc_info()[0])



    # Successfully set days to expire. THIS HAS BEEN CONFIRMED THROUGH MANUAL DATABASE AUTHENTICATION.
    def test_success(self):
        responseBody = self.user.set_days_expire(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                days = 16)

        self.assertEqual(responseBody['successful'], True,
                         msg='test_success assert#1 has failed.')



    # *********************************************************************
    # *                         CompanyAdminKey tests                     *
    # *********************************************************************
    
    
        
    # Missing CompanyAdminKey information from request call.
    def test_missingCompanyAdminKey(self):
        responseBody = self.user.set_days_expire(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                days = 1,
                                                companyAdminKeyExclude  =True)

        self.assertEqual(responseBody['errorMessage'], "company admin key required",
                         msg='test_missingCompanyAdminKey assert#1 has failed.')
        
        
        
    # Test a null CompanyAdminKey.
    def test_nullCompanyAdminKey(self):
        responseBody = self.user.set_days_expire(companyAdminKey = '', 
                                                days = 10)

        self.assertEqual(responseBody['errorMessage'], "company admin key required",
                          msg='test_nullCompanyAdminKey assert#1 has failed.')



    # Test a int CompanyAdminKey.
    def test_intCompanyAdminKey(self):
        responseBody = self.user.set_days_expire(companyAdminKey = 3425425, 
                                                days = 10)

        self.assertEqual(responseBody['errorMessage'], "invalid company admin key",
                          msg='test_intCompanyAdminKey assert#1 has failed.')



    # Test a float CompanyAdminKey.
    def test_floatCompanyAdminKey(self):
        responseBody = self.user.set_days_expire(companyAdminKey = 234.524, 
                                                days = 10)

        self.assertEqual(responseBody['errorMessage'], "invalid company admin key",
                          msg='test_floatCompanyAdminKey assert#1 has failed.')
        
        
        
    # Test a string CompanyAdminKey value call.
    def test_stringCompanyAdminKey(self):
        responseBody = self.user.set_days_expire(companyAdminKey = "AuthenticateShell.data['company_admin_key']", 
                                                days = 10)

        self.assertEqual(responseBody['errorMessage'], "invalid company admin key",
                          msg='test_stringCompanyAdminKey assert#1 has failed.')



    # Test an array CompanyAdminKey value call.
    def test_arrayCompanyAdminKey(self):
        responseBody = self.user.set_days_expire(companyAdminKey = [AuthenticateShell.data['company_admin_key']], 
                                                days = 10)

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arrayCompanyAdminKey assert#1 has failed.')


    
    # *********************************************************************
    # *                          Days tests                            *
    # *********************************************************************
    
    
        
    # Missing Days information from request call.
    def test_missingDays(self):
        responseBody = self.user.set_days_expire(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                            days = 10,
                                            daysExclude = True)

        self.assertEqual(responseBody['errorMessage'], 'submit days',
                         msg='test_missingDays assert#1 has failed.')
        
        
        
    # Test a null Days.
    def test_nullDays(self):
        responseBody = self.user.set_days_expire(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                            days = '')

        self.assertEqual(responseBody['errorMessage'], 'submit days',
                          msg='test_nullDays assert#1 has failed.')



    # Test a int Days.
    def test_intDays(self):
        responseBody = self.user.set_days_expire(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                            days = 10000000)

        self.assertEqual(responseBody['successful'], True,
                          msg='test_intDays assert#1 has failed.')



    # Test a float Days.
    def test_floatDays(self):
        responseBody = self.user.set_days_expire(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                            days = 1.10)

        self.assertEqual(responseBody['errorMessage'], 'submit days',
                          msg='test_floatDays assert#1 has failed.')
        
        
        
    # Test a string Days value call.
    def test_stringDays(self):
        responseBody = self.user.set_days_expire(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                            days = 'doggy')

        self.assertEqual(responseBody['errorMessage'], 'submit days',
                          msg='test_stringDays assert#1 has failed.')



    # Test an array Days value call.
    def test_arrayDays(self):
        responseBody = self.user.set_days_expire(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                            days = [10])

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arrayDays assert#1 has failed.')



def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestSetDayExpire('test_success'))

    suite.addTest(TestSetDayExpire('test_missingCompanyAdminKey'))
    suite.addTest(TestSetDayExpire('test_nullCompanyAdminKey'))
    suite.addTest(TestSetDayExpire('test_intCompanyAdminKey'))
    suite.addTest(TestSetDayExpire('test_floatCompanyAdminKey'))
    suite.addTest(TestSetDayExpire('test_stringCompanyAdminKey'))
    suite.addTest(TestSetDayExpire('test_arrayCompanyAdminKey'))

    suite.addTest(TestSetDayExpire('test_missingDays'))
    suite.addTest(TestSetDayExpire('test_nullDays'))
    suite.addTest(TestSetDayExpire('test_intDays'))
    suite.addTest(TestSetDayExpire('test_floatDays'))
    suite.addTest(TestSetDayExpire('test_stringDays'))
    suite.addTest(TestSetDayExpire('test_arrayDays'))

    return suite
    
    
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())