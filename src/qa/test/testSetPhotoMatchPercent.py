import sys, unittest, AuthenticateShell

'''
    Authenticate set photo match percent end point.
    
    Purpose - set the minimum photo match percent 
              needed to pass the photo proof test check. 

    Method signature:
        def set_photo_match_per(self, companyAdminKey='', percent=40,
                            companyAdminKeyExclude=False, 
                            percentExclude=False, sandBox=False):

    Required:
        companyAdminKey
        percent

    Test cases
        Successfully set the photo match percentage.

        CompanyAdminKey missing from request call.
        Null CompanyAdminKey value. 
        Int CompanyAdminKey value.    
        Float CompanyAdminKey value.   
        String CompanyAdminKey value.
        Array CompanyAdminKey value.   

        percent missing from request call.
        Null percent value. 
        Int percent value.    
        Float percent value.   
        String percent value.
        Array percent value. 
'''
class TestPhotoMatch(unittest.TestCase):

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
            cls.user.set_photo_match_per(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                         percent = 40)
        except:
            print("Unexpected error during tearDownClass:", sys.exc_info()[0])



    # Successfully set photo match. THIS HAS BEEN CONFIRMED THROUGH MANUAL DATABASE AUTHENTICATION.
    def test_success(self):
        responseBody = self.user.set_photo_match_per(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                     percent = 100)

        self.assertEqual(responseBody['successful'], True,
                         msg='test_success assert#1 has failed.')



    # *********************************************************************
    # *                         CompanyAdminKey tests                     *
    # *********************************************************************
    
    
        
    # Missing CompanyAdminKey information from request call.
    def test_missingCompanyAdminKey(self):
        responseBody = self.user.set_photo_match_per(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                     percent = 100,
                                                     companyAdminKeyExclude = True)

        self.assertEqual(responseBody['errorMessage'], "company admin key required",
                         msg='test_missingCompanyAdminKey assert#1 has failed.')
        
        
        
    # Test a null CompanyAdminKey.
    def test_nullCompanyAdminKey(self):
        responseBody = self.user.set_photo_match_per(companyAdminKey = '', 
                                                     percent = 100)

        self.assertEqual(responseBody['errorMessage'], "company admin key required",
                          msg='test_nullCompanyAdminKey assert#1 has failed.')



    # Test a int CompanyAdminKey.
    def test_intCompanyAdminKey(self):
        responseBody = self.user.set_photo_match_per(companyAdminKey = 123654, 
                                                     percent = 100)

        self.assertEqual(responseBody['errorMessage'], "invalid company admin key",
                          msg='test_intCompanyAdminKey assert#1 has failed.')



    # Test a float CompanyAdminKey.
    def test_floatCompanyAdminKey(self):
        responseBody = self.user.set_photo_match_per(companyAdminKey = 123.2135, 
                                                     percent = 100)

        self.assertEqual(responseBody['errorMessage'], "invalid company admin key",
                          msg='test_floatCompanyAdminKey assert#1 has failed.')
        
        
        
    # Test a string CompanyAdminKey value call.
    def test_stringCompanyAdminKey(self):
        responseBody = self.user.set_photo_match_per(companyAdminKey = "AuthenticateShell.data['company_admin_key']", 
                                                     percent = 100)

        self.assertEqual(responseBody['errorMessage'], "invalid company admin key",
                          msg='test_stringCompanyAdminKey assert#1 has failed.')



    # Test an array CompanyAdminKey value call.
    def test_arrayCompanyAdminKey(self):
        responseBody = self.user.set_photo_match_per(companyAdminKey = [AuthenticateShell.data['company_admin_key']], 
                                                     percent = 100)

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arrayCompanyAdminKey assert#1 has failed.')


    
    # *********************************************************************
    # *                          Percent tests                            *
    # *********************************************************************
    
    
        
    # Missing Percent information from request call.
    def test_missingPercent(self):
        responseBody = self.user.set_photo_match_per(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                     percent = 100,
                                                     percentExclude = True)

        self.assertEqual(responseBody['errorMessage'], 'percent required',
                         msg='test_missingPercent assert#1 has failed.')
        
        
        
    # Test a null Percent.
    def test_nullPercent(self):
        responseBody = self.user.set_photo_match_per(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                     percent = '')

        self.assertEqual(responseBody['errorMessage'], 'percent required',
                          msg='test_nullPercent assert#1 has failed.')



    # Test a int Percent.
    def test_intPercent(self):
        responseBody = self.user.set_photo_match_per(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                     percent = 100000000000)

        self.assertEqual(responseBody['errorMessage'], 'percent required',
                          msg='test_intPercent assert#1 has failed.')



    # Test a float Percent.
    def test_floatPercent(self):
        responseBody = self.user.set_photo_match_per(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                     percent = 1.9999999999999999)

        self.assertEqual(responseBody['errorMessage'], 'percent required',
                          msg='test_floatPercent assert#1 has failed.')
        
        
        
    # Test a string Percent value call.
    def test_stringPercent(self):
        responseBody = self.user.set_photo_match_per(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                     percent = 'pie')

        self.assertEqual(responseBody['errorMessage'], 'percent required',
                          msg='test_stringPercent assert#1 has failed.')



    # Test an array Percent value call.
    def test_arrayPercent(self):
        responseBody = self.user.set_photo_match_per(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                     percent = [100])

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arrayPercent assert#1 has failed.')



def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestPhotoMatch('test_success'))

    suite.addTest(TestPhotoMatch('test_missingCompanyAdminKey'))
    suite.addTest(TestPhotoMatch('test_nullCompanyAdminKey'))
    suite.addTest(TestPhotoMatch('test_intCompanyAdminKey'))
    suite.addTest(TestPhotoMatch('test_floatCompanyAdminKey'))
    suite.addTest(TestPhotoMatch('test_stringCompanyAdminKey'))
    suite.addTest(TestPhotoMatch('test_arrayCompanyAdminKey'))

    suite.addTest(TestPhotoMatch('test_missingPercent'))
    suite.addTest(TestPhotoMatch('test_nullPercent'))
    suite.addTest(TestPhotoMatch('test_intPercent'))
    suite.addTest(TestPhotoMatch('test_floatPercent'))
    suite.addTest(TestPhotoMatch('test_stringPercent'))
    suite.addTest(TestPhotoMatch('test_arrayPercent'))

    return suite
    
    
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())