import sys, unittest, AuthenticateShell

'''
    Authenticate  end point.
    
    Purpose - This will upload a front of a passport to check the data

    Method signature:
        def upload_passport(self, accessCode='', idFront='',
                            accessCodeExclude=False, idFrontExclude=False, 
                            sandBox=False):

    Required:
        accessCode
        idFront

    Test cases
        Successfully upload a passport.

        AccessCode missing from request call.
        Null AccessCode value. 
        Int AccessCode value.    
        Float AccessCode value.   
        String AccessCode value.
        Array AccessCode value.   

        IdFront missing from request call.
        Null IdFront value. 
        Int IdFront value.    
        Float IdFront value.   
        String IdFront value.
        Array IdFront value. 
'''
class TestUploadPassport(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        try:
            cls.user = AuthenticateShell.Authenticate()      

            cls.user.create_user(firstName = AuthenticateShell.data["firstName"], 
                                 lastName = AuthenticateShell.data["lastName"], 
                                 email = AuthenticateShell.data["email"], 
                                 phone = AuthenticateShell.data["phone"], 
                                 companyAdminKey = AuthenticateShell.data["company_admin_key"], 
                                 country = AuthenticateShell.data["country"],
                                 sandBox = True)
        except:
            print("Unexpected error during setUpClass:", sys.exc_info()[0])


    @classmethod
    def tearDownClass(cls):
        try:
            pass
        except:
            print("Unexpected error during tearDownClass:", sys.exc_info()[0])



    # Successfully upload a passport.
    def test_success(self):
        responseBody = self.user.upload_passport(accessCode = self.user.GetAccessCode(), 
                                                idFront = AuthenticateShell.data['passport_good'], 
                                                sandBox=True)

        self.assertNotEqual(responseBody['success'], 'true',
                         msg='test_success assert#1 has failed.')



    # *********************************************************************
    # *                         AccessCode tests                          *
    # *********************************************************************
    
    
        
    # Missing AccessCode information from request call.
    def test_missingAccessCode(self):
        responseBody = self.user.upload_passport(accessCode = self.user.GetAccessCode(), 
                                                idFront = AuthenticateShell.data['passport_good'], 
                                                sandBox=True,
                                                accessCodeExclude = True)

        self.assertEqual(responseBody['errorMessage'], 'please submit access code',
                         msg='test_missingAccessCode assert#1 has failed.')
        
        
        
    # Test a null AccessCode.
    def test_nullAccessCode(self):
        responseBody = self.user.upload_passport(accessCode = '', 
                                                idFront = AuthenticateShell.data['passport_good'], 
                                                sandBox=True)

        self.assertEqual(responseBody['errorMessage'], 'please submit access code',
                          msg='test_nullAccessCode assert#1 has failed.')



    # Test a int AccessCode.
    def test_intAccessCode(self):
        responseBody = self.user.upload_passport(accessCode = 123821, 
                                                idFront = AuthenticateShell.data['passport_good'], 
                                                sandBox=True)

        self.assertEqual(responseBody['errorMessage'], 'An unknown error has occurred.',
                          msg='test_intAccessCode assert#1 has failed.')



    # Test a float AccessCode.
    def test_floatAccessCode(self):
        responseBody = self.user.upload_passport(accessCode = 1.1, 
                                                idFront = AuthenticateShell.data['passport_good'], 
                                                sandBox=True)

        self.assertEqual(responseBody['errorMessage'], 'An unknown error has occurred.',
                          msg='test_floatAccessCode assert#1 has failed.')
        
        
        
    # Test a string AccessCode value call.
    def test_stringAccessCode(self):
        responseBody = self.user.upload_passport(accessCode = 'self.user.GetAccessCode()', 
                                                idFront = AuthenticateShell.data['passport_good'], 
                                                sandBox=True)

        self.assertEqual(responseBody['errorMessage'], 'An unknown error has occurred.',
                          msg='test_stringAccessCode assert#1 has failed.')



    # Test an array AccessCode value call.
    def test_arrayAccessCode(self):
        responseBody = self.user.upload_passport(accessCode = [], 
                                                idFront = AuthenticateShell.data['passport_good'], 
                                                sandBox=True)

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arrayAccessCode assert#1 has failed.')


    
    # *********************************************************************
    # *                          idFront tests                            *
    # *********************************************************************
    
    
        
    # Missing idFront information from request call.
    def test_missingIdFront(self):
        responseBody = self.user.upload_passport(accessCode = self.user.GetAccessCode(), 
                                                idFront = AuthenticateShell.data['passport_good'], 
                                                sandBox=True,
                                                idFrontExclude = True)

        self.assertEqual(responseBody['errorMessage'], "please submit id Front",
                         msg='test_missingIdFront assert#1 has failed.')
        
        
        
    # Test a null IdFront.
    def test_nullIdFront(self):
        responseBody = self.user.upload_passport(accessCode = self.user.GetAccessCode(), 
                                                idFront = '', 
                                                sandBox=True)

        self.assertEqual(responseBody['errorMessage'], "please submit id Front",
                          msg='test_nullIdFront assert#1 has failed.')



    # Test a int IdFront.
    def test_intIdFront(self):
        responseBody = self.user.upload_passport(accessCode = self.user.GetAccessCode(), 
                                                idFront = 852, 
                                                sandBox=True)

        self.assertEqual(responseBody['errorMessage'], 'idFront is not a valid base-64 string.',
                          msg='test_intIdFront assert#1 has failed.')



    # Test a float IdFront.
    def test_floatIdFront(self):
        responseBody = self.user.upload_passport(accessCode = self.user.GetAccessCode(), 
                                                idFront = 5.5, 
                                                sandBox=True)

        self.assertEqual(responseBody['errorMessage'], 'idFront is not a valid base-64 string.',
                          msg='test_floatIdFront assert#1 has failed.')
        
        
        
    # Test a string IdFront value call.
    def test_stringIdFront(self):
        responseBody = self.user.upload_passport(accessCode = self.user.GetAccessCode(), 
                                                idFront = "invalid strnig", 
                                                sandBox=True)

        self.assertEqual(responseBody['errorMessage'], 'idFront is not a valid base-64 string.',
                          msg='test_stringIdFront assert#1 has failed.')



    # Test an array IdFront value call.
    def test_arrayIdFront(self):
        responseBody = self.user.upload_passport(accessCode = self.user.GetAccessCode(), 
                                                idFront = [], 
                                                sandBox=True)

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arrayIdFront assert#1 has failed.')



def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestUploadPassport('test_success'))

    suite.addTest(TestUploadPassport('test_missingAccessCode'))
    suite.addTest(TestUploadPassport('test_nullAccessCode'))
    suite.addTest(TestUploadPassport('test_intAccessCode'))
    suite.addTest(TestUploadPassport('test_floatAccessCode'))
    suite.addTest(TestUploadPassport('test_stringAccessCode'))
    suite.addTest(TestUploadPassport('test_arrayAccessCode'))

    suite.addTest(TestUploadPassport('test_missingIdFront'))
    suite.addTest(TestUploadPassport('test_nullIdFront'))
    suite.addTest(TestUploadPassport('test_intIdFront'))
    suite.addTest(TestUploadPassport('test_floatIdFront'))
    suite.addTest(TestUploadPassport('test_stringIdFront'))
    suite.addTest(TestUploadPassport('test_arrayIdFront'))

    return suite
    
    
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())