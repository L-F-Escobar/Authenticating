import sys, unittest, AuthenticateShell

'''
    Authenticate get test result(s) end point.
    
    Purpose - These endpoints allow a company to query the user's test results.
    
    Notes - 

    Method signature:
        def get_test_result(self, accessCode='', companyAdminKey='', 
                        accessCodeExclude=False, companyAdminKeyExclude=False,
                        sandBox=False):

        def get_test_results(self, accessCode=[], companyAdminKey='', 
                        accessCodeExclude=False, companyAdminKeyExclude=False,
                        sandBox=False):
    
    Required:
        accessCode
        companyAdminKey

    Test cases
        Successfully get test results.

        AccessCode missing from request call.
        Null AccessCode value. 
        Int AccessCode value.    
        Float AccessCode value.   
        String AccessCode value.
        Array AccessCode value.   

        CompanyAdminKey missing from request call.
        Null CompanyAdminKey value. 
        Int CompanyAdminKey value.    
        Float CompanyAdminKey value.   
        String CompanyAdminKey value.
        Array CompanyAdminKey value. 
        
'''
class TestGetTestResults(unittest.TestCase):

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

            cls.user.get_quiz(cls.user.GetAccessCode(), sandBox=True)

            cls.user.verify_quiz(cls.user.GetAccessCode(), cls.user.GetQuizId(), 
                                 cls.user.GetTransactionId(), cls.user.GetResponseUniqueId(), 
                                 cls.user.GetAnswers(), sandBox=True)
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
        responseBody = self.user.get_test_result(accessCode = self.user.GetAccessCode(), 
                                                 companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                 sandBox=True)

        self.assertEqual(responseBody['successful'], True,
                         msg='test_success assert#1 has failed.')

        testList = []
        testList.append(self.user.GetAccessCode())
        testList.append(self.user.GetAccessCode())

        responseBody = self.user.get_test_results(accessCodes = testList, 
                                                  companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                  sandBox=True)

        self.assertNotEqual(responseBody, [],
                         msg='test_success assert#2 has failed.')



    # *********************************************************************
    # *                         AccessCode tests                          *
    # *********************************************************************
    
    
        
    # Missing AccessCode information from request call.
    def test_missingAccessCode(self):
        responseBody = self.user.get_test_result(accessCode = self.user.GetAccessCode(), 
                                                 companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                 sandBox=True,
                                                 accessCodeExclude = True)

        self.assertEqual(responseBody['errorMessage'], "access code is required",
                         msg='test_missingAccessCode assert#1 has failed.')

        testList = []
        testList.append(self.user.GetAccessCode())
        testList.append(self.user.GetAccessCode())

        responseBody = self.user.get_test_results(accessCodes = testList, 
                                                  companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                  sandBox=True,
                                                  accessCodesExclude = True)

        self.assertNotEqual(responseBody['errorMessage'], 'access code is required',
                         msg='test_missingAccessCode assert#2 has failed.')
        
        
        
    # Test a null AccessCode.
    def test_nullAccessCode(self):
        responseBody = self.user.get_test_result(accessCode = '', 
                                                 companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                 sandBox=True)

        self.assertEqual(responseBody['errorMessage'], 'access code is required',
                         msg='test_nullAccessCode assert#1 has failed.')

        responseBody = self.user.get_test_results(accessCodes = '', 
                                                  companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                  sandBox=True)

        self.assertNotEqual(responseBody['errorMessage'], 'access code is required',
                         msg='test_nullAccessCode assert#2 has failed.')



    # Test a int AccessCode.
    def test_intAccessCode(self):
        responseBody = self.user.get_test_result(accessCode = 852582, 
                                                 companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                 sandBox=True)

        self.assertEqual(responseBody['errorMessage'], "Invalid Access Code",
                         msg='test_intAccessCode assert#1 has failed.')

        responseBody = self.user.get_test_results(accessCodes = 123456789, 
                                                  companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                  sandBox=True)

        self.assertNotEqual(responseBody['errorMessage'], 'Invalid Access Code',
                         msg='test_intAccessCode assert#2 has failed.')



    # Test a float AccessCode.
    def test_floatAccessCode(self):
        responseBody = self.user.get_test_result(accessCode = 1.1, 
                                                 companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                 sandBox=True)

        self.assertEqual(responseBody['errorMessage'], 'Invalid Access Code',
                         msg='test_floatAccessCode assert#1 has failed.')

        responseBody = self.user.get_test_results(accessCodes = 2.2, 
                                                  companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                  sandBox=True)

        self.assertNotEqual(responseBody['errorMessage'], 'Invalid Access Code',
                         msg='test_floatAccessCode assert#2 has failed.')
        
        
        
    # Test a string AccessCode value call.
    def test_stringAccessCode(self):
        responseBody = self.user.get_test_result(accessCode = 'self.user.GetAccessCode()', 
                                                 companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                 sandBox=True)

        self.assertEqual(responseBody['errorMessage'], 'Invalid Access Code',
                         msg='test_stringAccessCode assert#1 has failed.')

        responseBody = self.user.get_test_results(accessCodes = 'String', 
                                                  companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                  sandBox=True)

        self.assertNotEqual(responseBody['errorMessage'], 'Invalid Access Code',
                         msg='test_stringAccessCode assert#2 has failed.')



    # Test an array AccessCode value call.
    def test_arrayAccessCode(self):
        responseBody = self.user.get_test_result(accessCode = [self.user.GetAccessCode()], 
                                                 companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                 sandBox=True)

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                         msg='test_arrayAccessCode assert#1 has failed.')

        testList = []
        testList.append(self.user.GetAccessCode())
        testList.append(self.user.GetAccessCode())

        responseBody = self.user.get_test_results(accessCodes = [], 
                                                  companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                  sandBox=True)

        self.assertEqual(responseBody['errorMessage'], 'access codes are required',
                         msg='test_arrayAccessCode assert#2 has failed.')

    


    # *********************************************************************
    # *                         CompanyAdminKey tests                     *
    # *********************************************************************
    
    
        
    # Missing CompanyAdminKey information from request call.
    def test_missingCompanyAdminKey(self):
        responseBody = self.user.get_test_result(accessCode = self.user.GetAccessCode(), 
                                                 companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                 sandBox=True,
                                                 companyAdminKeyExclude = True)

        self.assertEqual(responseBody['errorMessage'], 'companyAdminKey is required',
                         msg='test_missingCompanyAdminKey assert#1 has failed.')

        testList = []
        testList.append(self.user.GetAccessCode())
        testList.append(self.user.GetAccessCode())

        responseBody = self.user.get_test_results(accessCodes = testList, 
                                                  companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                  sandBox=True,
                                                  companyAdminKeyExclude = True)

        self.assertEqual(responseBody['errorMessage'], 'companyAdminKey is required',
                         msg='test_missingCompanyAdminKey assert#2 has failed.')
        
        
        
    # Test a null CompanyAdminKey.
    def test_nullCompanyAdminKey(self):
        responseBody = self.user.get_test_result(accessCode = self.user.GetAccessCode(), 
                                                 companyAdminKey = '', 
                                                 sandBox=True)

        self.assertEqual(responseBody['errorMessage'], 'companyAdminKey is required',
                         msg='test_nullCompanyAdminKey assert#1 has failed.')

        testList = []
        testList.append(self.user.GetAccessCode())
        testList.append(self.user.GetAccessCode())

        responseBody = self.user.get_test_results(accessCodes = testList, 
                                                  companyAdminKey = '', 
                                                  sandBox=True)

        self.assertEqual(responseBody['errorMessage'], 'companyAdminKey is required',
                         msg='test_nullCompanyAdminKey assert#2 has failed.')



    # Test a int CompanyAdminKey.
    def test_intCompanyAdminKey(self):
        responseBody = self.user.get_test_result(accessCode = self.user.GetAccessCode(), 
                                                 companyAdminKey = 123654, 
                                                 sandBox=True)

        self.assertEqual(responseBody['errorMessage'], 'Unknown or Invalid Company Admin Key',
                         msg='test_intCompanyAdminKey assert#1 has failed.')

        testList = []
        testList.append(self.user.GetAccessCode())
        testList.append(self.user.GetAccessCode())

        responseBody = self.user.get_test_results(accessCodes = testList, 
                                                  companyAdminKey = 123654, 
                                                  sandBox=True)

        self.assertEqual(responseBody['errorMessage'], 'Unknown or Invalid Company Admin Key',
                         msg='test_intCompanyAdminKey assert#2 has failed.')



    # Test a float CompanyAdminKey.
    def test_floatCompanyAdminKey(self):
        responseBody = self.user.get_test_result(accessCode = self.user.GetAccessCode(), 
                                                 companyAdminKey = 11.1, 
                                                 sandBox=True)

        self.assertEqual(responseBody['errorMessage'], 'Unknown or Invalid Company Admin Key',
                         msg='test_floatCompanyAdminKey assert#1 has failed.')

        testList = []
        testList.append(self.user.GetAccessCode())
        testList.append(self.user.GetAccessCode())

        responseBody = self.user.get_test_results(accessCodes = testList, 
                                                  companyAdminKey = 6.66, 
                                                  sandBox=True)

        self.assertEqual(responseBody['errorMessage'], 'Unknown or Invalid Company Admin Key',
                         msg='test_floatCompanyAdminKey assert#2 has failed.')
        
        
        
    # Test a string CompanyAdminKey value call.
    def test_stringCompanyAdminKey(self):
        responseBody = self.user.get_test_result(accessCode = self.user.GetAccessCode(), 
                                                 companyAdminKey = "AuthenticateShell.data['company_admin_key']", 
                                                 sandBox=True)

        self.assertEqual(responseBody['errorMessage'], 'Unknown or Invalid Company Admin Key',
                         msg='test_stringCompanyAdminKey assert#1 has failed.')

        testList = []
        testList.append(self.user.GetAccessCode())
        testList.append(self.user.GetAccessCode())

        responseBody = self.user.get_test_results(accessCodes = testList, 
                                                  companyAdminKey = "AuthenticateShell.data['company_admin_key']", 
                                                  sandBox=True)

        self.assertEqual(responseBody['errorMessage'], 'Unknown or Invalid Company Admin Key',
                         msg='test_stringCompanyAdminKey assert#2 has failed.')



    # Test an array CompanyAdminKey value call.
    def test_arrayCompanyAdminKey(self):
        responseBody = self.user.get_test_result(accessCode = self.user.GetAccessCode(), 
                                                 companyAdminKey = [], 
                                                 sandBox=True)

        self.assertEqual(responseBody['errorMessage'], 'An unknown error has occurred.',
                         msg='test_arrayCompanyAdminKey assert#1 has failed.')

        testList = []
        testList.append(self.user.GetAccessCode())
        testList.append(self.user.GetAccessCode())

        responseBody = self.user.get_test_results(accessCodes = testList, 
                                                  companyAdminKey = [], 
                                                  sandBox=True)

        self.assertEqual(responseBody['errorMessage'], 'An unknown error has occurred.',
                         msg='test_arrayCompanyAdminKey assert#2 has failed.')




def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestGetTestResults('test_success'))

    suite.addTest(TestGetTestResults('test_missingAccessCode'))
    suite.addTest(TestGetTestResults('test_nullAccessCode'))
    suite.addTest(TestGetTestResults('test_intAccessCode'))
    suite.addTest(TestGetTestResults('test_floatAccessCode'))
    suite.addTest(TestGetTestResults('test_stringAccessCode'))
    suite.addTest(TestGetTestResults('test_arrayAccessCode'))

    suite.addTest(TestGetTestResults('test_missingCompanyAdminKey'))
    suite.addTest(TestGetTestResults('test_nullCompanyAdminKey'))
    suite.addTest(TestGetTestResults('test_intCompanyAdminKey'))
    suite.addTest(TestGetTestResults('test_floatCompanyAdminKey'))
    suite.addTest(TestGetTestResults('test_stringCompanyAdminKey'))
    suite.addTest(TestGetTestResults('test_arrayCompanyAdminKey'))
    
    return suite
    
    
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())