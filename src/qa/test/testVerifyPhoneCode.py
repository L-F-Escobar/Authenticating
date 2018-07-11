import sys, unittest, AuthenticateShell

'''
    Authenticate verify phone code end point.
    
    Purpose - This is used to complete the phone number verification process.
              The user receives an SMS with a code.
    
    Notes - only the fails can be automated.

    Method signature:
        def verify_phone_code(self, accessCode='', smsCode='', accessCodeExclude=False,
                              smsCodeExclude=False):
    
    Required:
        accessCode
        smsCode

    Test cases
        AccessCode missing from request call.
        Null AccessCode value. 
        Int AccessCode value.    
        Float AccessCode value.   
        String AccessCode value.
        Array AccessCode value.   

        SmsCode missing from request call.
        Null SmsCode value. 
        Int SmsCode value.    
        Float SmsCode value.   
        String SmsCode value.
        Array SmsCode value. 
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




    # *********************************************************************
    # *                         AccessCode tests                          *
    # *********************************************************************
    
    
        
    # Missing AccessCode information from request call.
    def test_missingAccessCode(self):
        responseBody = self.user.verify_phone_code(accessCode = self.user.GetAccessCode(),
                                                   smsCode = AuthenticateShell.data["smsCode"],
                                                   accessCodeExclude = True)

        self.assertEqual(responseBody['errorMessage'], "access has expired or does not exist",
                         msg='test_missingAccessCode assert#1 has failed.')
        
        
        
    # Test a null AccessCode.
    def test_nullAccessCode(self):
        responseBody = self.user.verify_phone_code(accessCode = '',
                                                   smsCode = AuthenticateShell.data["smsCode"])

        self.assertEqual(responseBody['errorMessage'], "access has expired or does not exist",
                          msg='test_nullAccessCode assert#1 has failed.')



    # Test a int AccessCode.
    def test_intAccessCode(self):
        responseBody = self.user.verify_phone_code(accessCode = 1,
                                                   smsCode = AuthenticateShell.data["smsCode"])

        self.assertEqual(responseBody['errorMessage'], "access has expired or does not exist",
                          msg='test_intAccessCode assert#1 has failed.')



    # Test a float AccessCode.
    def test_floatAccessCode(self):
        responseBody = self.user.verify_phone_code(accessCode = 123.369,
                                                   smsCode = AuthenticateShell.data["smsCode"])

        self.assertEqual(responseBody['errorMessage'], "access has expired or does not exist",
                          msg='test_floatAccessCode assert#1 has failed.')
        
        
        
    # Test a string AccessCode value call.
    def test_stringAccessCode(self):
        responseBody = self.user.verify_phone_code(accessCode = 'self.user.GetAccessCode()',
                                                   smsCode = AuthenticateShell.data["smsCode"])

        self.assertEqual(responseBody['errorMessage'], "access has expired or does not exist",
                          msg='test_stringAccessCode assert#1 has failed.')



    # Test an array AccessCode value call.
    def test_arrayAccessCode(self):
        responseBody = self.user.verify_phone_code(accessCode = [self.user.GetAccessCode()],
                                                   smsCode = AuthenticateShell.data["smsCode"])

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arrayAccessCode assert#1 has failed.')




    # *********************************************************************
    # *                           SmsCode tests                           *
    # *********************************************************************
    
    
        
    # Missing SmsCode information from request call.
    def test_missingSmsCode(self):
        responseBody = self.user.verify_phone_code(accessCode = self.user.GetAccessCode(),
                                                   smsCode = AuthenticateShell.data["smsCode"],
                                                   smsCodeExclude = True)

        self.assertEqual(responseBody['errorMessage'], "please submit code",
                         msg='test_missingSmsCode assert#1 has failed.')
        
        
        
    # Test a null SmsCode.
    def test_nullSmsCode(self):
        responseBody = self.user.verify_phone_code(accessCode = self.user.GetAccessCode(),
                                                   smsCode = '')

        self.assertEqual(responseBody['errorMessage'], "please submit code",
                          msg='test_nullSmsCode assert#1 has failed.')



    # Test a int SmsCode.
    def test_intSmsCode(self):
        responseBody = self.user.verify_phone_code(accessCode = self.user.GetAccessCode(),
                                                   smsCode = 123456789)

        self.assertEqual(responseBody['errorMessage'], "ERR: code does not match",
                          msg='test_intSmsCode assert#1 has failed.')



    # Test a float SmsCode.
    def test_floatSmsCode(self):
        responseBody = self.user.verify_phone_code(accessCode = self.user.GetAccessCode(),
                                                   smsCode = 12345.6789)

        self.assertEqual(responseBody['errorMessage'], "ERR: code does not match",
                          msg='test_floatSmsCode assert#1 has failed.')
        
        
        
    # Test a string SmsCode value call.
    def test_stringSmsCode(self):
        responseBody = self.user.verify_phone_code(accessCode = self.user.GetAccessCode(),
                                                   smsCode = 'AuthenticateShell.data["smsCode"]')

        self.assertEqual(responseBody['errorMessage'], "ERR: code does not match",
                          msg='test_stringSmsCode assert#1 has failed.')



    # Test an array SmsCode value call.
    def test_arraySmsCode(self):
        responseBody = self.user.verify_phone_code(accessCode = self.user.GetAccessCode(),
                                                   smsCode = [AuthenticateShell.data["smsCode"]])

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arraySmsCode assert#1 has failed.')




def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestVerifyPhone('test_missingAccessCode'))
    suite.addTest(TestVerifyPhone('test_nullAccessCode'))
    suite.addTest(TestVerifyPhone('test_intAccessCode'))
    suite.addTest(TestVerifyPhone('test_floatAccessCode'))
    suite.addTest(TestVerifyPhone('test_stringAccessCode'))
    suite.addTest(TestVerifyPhone('test_arrayAccessCode'))

    suite.addTest(TestVerifyPhone('test_missingSmsCode'))
    suite.addTest(TestVerifyPhone('test_nullSmsCode'))
    suite.addTest(TestVerifyPhone('test_intSmsCode'))
    suite.addTest(TestVerifyPhone('test_floatSmsCode'))
    suite.addTest(TestVerifyPhone('test_stringSmsCode'))
    suite.addTest(TestVerifyPhone('test_arraySmsCode'))
    
    return suite
    
    
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())