import sys, unittest, AuthenticateShell

'''
    Authenticate get quiz end point.
    
    Purpose - This will return a quiz object for a user if they have 
               enough information to do so
    
    Notes - Difficult end point to properly test....

    Method signature:
        def get_quiz(self, accessCode='', accessCodeExclude=False,
                 sandBox=False):
    
    Required:
        accessCode

    Test cases
        Successfully get test results.

        AccessCode missing from request call.
        Null AccessCode value. 
        Int AccessCode value.    
        Float AccessCode value.   
        String AccessCode value.
        Array AccessCode value.   
        
'''
class TestGetQuiz(unittest.TestCase):

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



    # Successfully check test results.
    def test_success(self):
        responseBody = self.user.get_quiz(accessCode = self.user.GetAccessCode(), 
                                          sandBox=True)

        self.assertNotEqual(responseBody, [],
                         msg='test_success assert#1 has failed.')



    # *********************************************************************
    # *                         AccessCode tests                          *
    # *********************************************************************
    
    
        
    # Missing AccessCode information from request call.
    def test_missingAccessCode(self):
        responseBody = self.user.get_quiz(accessCode = self.user.GetAccessCode(), 
                                          sandBox=True,
                                          accessCodeExclude = True)

        self.assertEqual(responseBody['successful'], 'accessCode required',
                         msg='test_missingAccessCode assert#1 has failed.')
        
        
        
    # Test a null AccessCode.
    def test_nullAccessCode(self):
        responseBody = self.user.get_quiz(accessCode = '', 
                                          sandBox=True)

        self.assertEqual(responseBody['successful'], 'accessCode required',
                         msg='test_nullAccessCode assert#1 has failed.')



    # Test a int AccessCode.
    def test_intAccessCode(self):
        responseBody = self.user.get_quiz(accessCode = 78, 
                                          sandBox=True)

        self.assertEqual(responseBody['successful'], 'access has expired or does not exist',
                         msg='test_intAccessCode assert#1 has failed.')



    # Test a float AccessCode.
    def test_floatAccessCode(self):
        responseBody = self.user.get_quiz(accessCode = 6.6, 
                                          sandBox=True)

        self.assertEqual(responseBody['successful'], 'access has expired or does not exist',
                         msg='test_floatAccessCode assert#1 has failed.')
        
        
        
    # Test a string AccessCode value call.
    def test_stringAccessCode(self):
        responseBody = self.user.get_quiz(accessCode = "self.user.GetAccessCode()", 
                                          sandBox=True)

        self.assertEqual(responseBody['successful'], 'access has expired or does not exist',
                         msg='test_stringAccessCode assert#1 has failed.')



    # Test an array AccessCode value call.
    def test_arrayAccessCode(self):
        responseBody = self.user.get_quiz(accessCode = [], 
                                          sandBox=True)

        self.assertEqual(responseBody['successful'], 'An unknown error has occurred.',
                         msg='test_arrayAccessCode assert#1 has failed.')



def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestGetQuiz('test_success'))

    suite.addTest(TestGetQuiz('test_missingAccessCode'))
    # suite.addTest(TestGetQuiz('test_nullAccessCode'))
    # suite.addTest(TestGetQuiz('test_intAccessCode'))
    # suite.addTest(TestGetQuiz('test_floatAccessCode'))
    # suite.addTest(TestGetQuiz('test_stringAccessCode'))
    # suite.addTest(TestGetQuiz('test_arrayAccessCode'))
    
    return suite
    
    
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())