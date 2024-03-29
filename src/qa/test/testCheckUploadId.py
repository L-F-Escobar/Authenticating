import sys, unittest, AuthenticateShell

'''
    Authenticate check upload id end point.
    
    Purpose - Purpose of this endpoint is to check if the uploadId call was 
              successful. Note that this does not return whether or not the 
              user passed the verification check, it merely confirms that the 
              data was readable and clear.
    
    Notes - THIS END POINT IS BROKEN IN SANDBOX - ALWAYS SENDS BACK SAME DATA.

    Method signature:
        def check_upload_id(self, accessCode='', accessCodeExclude=False, sandBox=False):
    
    Required:
        accessCode

    Test cases
        Successfully check an uploaded image.

        AccessCode missing from request call.
        Null AccessCode value. 
        Int AccessCode value.    
        Float AccessCode value.   
        String AccessCode value.
        Array AccessCode value.   
'''
class TestCheckUploadId(unittest.TestCase):

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
                                sandBox=True)
            
            cls.frontId, cls.backId = AuthenticateShell.base64Encode()

            cls.user.upload_id(accessCode = cls.user.GetAccessCode(), 
                                idFront = cls.frontId, 
                                idBack = cls.backId,
                                sandBox=True)
        except:
            print("Unexpected error during setUpClass:", sys.exc_info()[0])


    @classmethod
    def tearDownClass(cls):
        try:
            pass
        except:
            print("Unexpected error during tearDownClass:", sys.exc_info()[0])



    # Successfully check the upload.
    def test_success(self):
        responseBody = self.user.check_upload_id(accessCode = self.user.GetAccessCode(),
                                                 sandBox=True)

        self.assertEqual(responseBody['successful'], False,
                         msg='test_success assert#1 has failed.')



    # *********************************************************************
    # *                         AccessCode tests                          *
    # *********************************************************************
    
    
        
    # Missing AccessCode information from request call.
    def test_missingAccessCode(self):
        responseBody = self.user.check_upload_id(accessCode = self.user.GetAccessCode(),
                                                 accessCodeExclude = True,
                                                 sandBox=True)

        self.assertEqual(responseBody['errorMessage'], "access code is required",
                         msg='test_missingAccessCode assert#1 has failed.')
        
        
        
    # Test a null AccessCode.
    def test_nullAccessCode(self):
        responseBody = self.user.check_upload_id(accessCode = '',
                                                  sandBox = True)

        self.assertEqual(responseBody['errorMessage'], "access code is required",
                          msg='test_nullAccessCode assert#1 has failed.')



    # Test a int AccessCode.
    def test_intAccessCode(self):
        responseBody = self.user.check_upload_id(accessCode = 1111111111111,
                                                  sandBox = True)

        self.assertEqual(responseBody['errorMessage'], "access has expired or does not exist",
                          msg='test_intAccessCode assert#1 has failed.')



    # Test a float AccessCode.
    def test_floatAccessCode(self):
        responseBody = self.user.check_upload_id(accessCode = 111111111111.1,
                                                  sandBox = True)

        self.assertEqual(responseBody['errorMessage'], "access has expired or does not exist",
                          msg='test_floatAccessCode assert#1 has failed.')
        
        
        
    # Test a string AccessCode value call.
    def test_stringAccessCode(self):
        responseBody = self.user.check_upload_id(accessCode = 'User not found',
                                                  sandBox = True)

        self.assertEqual(responseBody['errorMessage'], "access has expired or does not exist",
                          msg='test_stringAccessCode assert#1 has failed.')



    # Test an array AccessCode value call.
    def test_arrayAccessCode(self):
        responseBody = self.user.check_upload_id(accessCode = ['Invalid access code'],
                                                  sandBox = True)

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arrayAccessCode assert#1 has failed.')




def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestCheckUploadId('test_success'))

    suite.addTest(TestCheckUploadId('test_missingAccessCode'))
    suite.addTest(TestCheckUploadId('test_nullAccessCode'))
    suite.addTest(TestCheckUploadId('test_intAccessCode'))
    suite.addTest(TestCheckUploadId('test_floatAccessCode'))
    suite.addTest(TestCheckUploadId('test_stringAccessCode'))
    suite.addTest(TestCheckUploadId('test_arrayAccessCode'))
    
    return suite
    
    
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())