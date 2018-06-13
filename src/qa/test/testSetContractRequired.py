import sys, unittest, AuthenticateShell

'''
    Authenticate set contract required end point.
    
    Purpose - Set whether or not phone and email verification are 
              both needed for the contact verified test.

    Method signature:
        def set_contract_required(self, companyAdminKey='', isPhoneRequired=True,
                              isEmailRequired=True, companyAdminKeyExclude=False, 
                              isPhoneRequiredExclude=False, isEmailRequiredExclude=False,
                              sandBox=False):

    Required:
        companyAdminKey
        isPhoneRequired
        isEmailRequired

    Test cases
        Successfully set social networks.

        CompanyAdminKey missing from request call.
        Null CompanyAdminKey value. 
        Int CompanyAdminKey value.    
        Float CompanyAdminKey value.   
        String CompanyAdminKey value.
        Array CompanyAdminKey value.   

        isPhoneRequired missing from request call.
        Null isPhoneRequired value. 
        Int isPhoneRequired value.    
        Float isPhoneRequired value.   
        String isPhoneRequired value.
        Array isPhoneRequired value. 

        IsEmailRequired missing from request call.
        Null IsEmailRequired value. 
        Int IsEmailRequired value.    
        Float IsEmailRequired value.   
        String IsEmailRequired value.
        Array IsEmailRequired value.
'''
class TestSetContractRequired(unittest.TestCase):

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
            cls.user.set_contract_required(AuthenticateShell.data['company_admin_key'], True, True)
        except:
            print("Unexpected error during tearDownClass:", sys.exc_info()[0])



    # Successfully set requirements. THIS HAS BEEN CONFIRMED THROUGH MANUAL DATABASE AUTHENTICATION.
    def test_success(self):
        responseBody = self.user.set_contract_required(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                        isPhoneRequired = False, 
                                                        isEmailRequired = False)

        self.assertEqual(responseBody['successful'], True,
                         msg='test_success assert#1 has failed.')



    # *********************************************************************
    # *                         CompanyAdminKey tests                     *
    # *********************************************************************
    
    
        
    # Missing CompanyAdminKey information from request call.
    def test_missingCompanyAdminKey(self):
        responseBody = self.user.set_contract_required(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                        isPhoneRequired = False, 
                                                        isEmailRequired = False,
                                                        companyAdminKeyExclude = True)

        self.assertEqual(responseBody['errorMessage'], "company admin key required",
                         msg='test_missingCompanyAdminKey assert#1 has failed.')
        
        
        
    # Test a null CompanyAdminKey.
    def test_nullCompanyAdminKey(self):
        responseBody = self.user.set_contract_required(companyAdminKey = '', 
                                                        isPhoneRequired = False, 
                                                        isEmailRequired = False)

        self.assertEqual(responseBody['errorMessage'], "company admin key required",
                          msg='test_nullCompanyAdminKey assert#1 has failed.')



    # Test a int CompanyAdminKey.
    def test_intCompanyAdminKey(self):
        responseBody = self.user.set_contract_required(companyAdminKey = 1, 
                                                        isPhoneRequired = False, 
                                                        isEmailRequired = False)

        self.assertEqual(responseBody['errorMessage'], "invalid company admin key",
                          msg='test_intCompanyAdminKey assert#1 has failed.')



    # Test a float CompanyAdminKey.
    def test_floatCompanyAdminKey(self):
        responseBody = self.user.set_contract_required(companyAdminKey = 1.1, 
                                                        isPhoneRequired = False, 
                                                        isEmailRequired = False)

        self.assertEqual(responseBody['errorMessage'], "invalid company admin key",
                          msg='test_floatCompanyAdminKey assert#1 has failed.')
        
        
        
    # Test a string CompanyAdminKey value call.
    def test_stringCompanyAdminKey(self):
        responseBody = self.user.set_contract_required("companyAdminKey = AuthenticateShell.data['company_admin_key']", 
                                                        isPhoneRequired = False, 
                                                        isEmailRequired = False)

        self.assertEqual(responseBody['errorMessage'], "invalid company admin key",
                          msg='test_stringCompanyAdminKey assert#1 has failed.')



    # Test an array CompanyAdminKey value call.
    def test_arrayCompanyAdminKey(self):
        responseBody = self.user.set_contract_required(companyAdminKey = [AuthenticateShell.data['company_admin_key']], 
                                                        isPhoneRequired = False, 
                                                        isEmailRequired = False)

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arrayCompanyAdminKey assert#1 has failed.')


    
    # *********************************************************************
    # *                          IsPhoneRequired tests                    *
    # *********************************************************************
    
    
        
    # Missing IsPhoneRequired information from request call.
    def test_missingIsPhoneRequired(self):
        responseBody = self.user.set_contract_required(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                        isPhoneRequired = False, 
                                                        isEmailRequired = False,
                                                        isPhoneRequiredExclude = True)

        self.assertEqual(responseBody['errorMessage'], 'isPhoneRequired field required',
                         msg='test_missingIsPhoneRequired assert#1 has failed.')
        
        
        
    # Test a null IsPhoneRequired.
    def test_nullIsPhoneRequired(self):
        responseBody = self.user.set_contract_required(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                        isPhoneRequired = '', 
                                                        isEmailRequired = False)

        self.assertEqual(responseBody['successful'], True,
                          msg='test_nullIsPhoneRequired assert#1 has failed.')



    # Test a int IsPhoneRequired.
    def test_intIsPhoneRequired(self):
        responseBody = self.user.set_contract_required(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                        isPhoneRequired = 123465, 
                                                        isEmailRequired = False)

        self.assertEqual(responseBody['successful'], True,
                          msg='test_intIsPhoneRequired assert#1 has failed.')



    # Test a float IsPhoneRequired.
    def test_floatIsPhoneRequired(self):
        responseBody = self.user.set_contract_required(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                        isPhoneRequired = 855.21651, 
                                                        isEmailRequired = False)

        self.assertEqual(responseBody['successful'], True,
                          msg='test_floatIsPhoneRequired assert#1 has failed.')
        
        
        
    # Test a string IsPhoneRequired value call.
    def test_stringIsPhoneRequired(self):
        responseBody = self.user.set_contract_required(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                        isPhoneRequired = 'False', 
                                                        isEmailRequired = False)

        self.assertEqual(responseBody['successful'], True,
                          msg='test_stringIsPhoneRequired assert#1 has failed.')



    # Test an array IsPhoneRequired value call.
    def test_arrayIsPhoneRequired(self):
        responseBody = self.user.set_contract_required(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                        isPhoneRequired = [False], 
                                                        isEmailRequired = False)

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arrayIsPhoneRequired assert#1 has failed.')




    # *********************************************************************
    # *                          IsEmailRequired tests                    *
    # *********************************************************************
    
    
        
    # Missing IsEmailRequired information from request call.
    def test_missingIsEmailRequired(self):
        responseBody = self.user.set_contract_required(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                        isPhoneRequired = False, 
                                                        isEmailRequired = False,
                                                        isEmailRequiredExclude = True)

        self.assertEqual(responseBody['errorMessage'], 'isEmailRequired field required',
                         msg='test_missingIsEmailRequired assert#1 has failed.')
        
        
        
    # Test a null IsEmailRequired.
    def test_nullIsEmailRequired(self):
        responseBody = self.user.set_contract_required(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                        isPhoneRequired = False, 
                                                        isEmailRequired = '')

        self.assertEqual(responseBody['successful'], True,
                          msg='test_nullIsEmailRequired assert#1 has failed.')



    # Test a int IsEmailRequired.
    def test_intIsEmailRequired(self):
        responseBody = self.user.set_contract_required(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                        isPhoneRequired = False, 
                                                        isEmailRequired = 123456)

        self.assertEqual(responseBody['successful'], True,
                          msg='test_intIsEmailRequired assert#1 has failed.')



    # Test a float IsEmailRequired.
    def test_floatIsEmailRequired(self):
        responseBody = self.user.set_contract_required(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                        isPhoneRequired = False, 
                                                        isEmailRequired = 855.258)

        self.assertEqual(responseBody['successful'], True,
                          msg='test_floatIsEmailRequired assert#1 has failed.')
        
        
        
    # Test a string IsEmailRequired value call.
    def test_stringIsEmailRequired(self):
        responseBody = self.user.set_contract_required(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                        isPhoneRequired = False, 
                                                        isEmailRequired = 'False')

        self.assertEqual(responseBody['successful'], True,
                          msg='test_stringIsEmailRequired assert#1 has failed.')



    # Test an array IsEmailRequired value call.
    def test_arrayIsEmailRequired(self):
        responseBody = self.user.set_contract_required(companyAdminKey = AuthenticateShell.data['company_admin_key'], 
                                                        isPhoneRequired = False, 
                                                        isEmailRequired = [False])

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arrayIsEmailRequired assert#1 has failed.')



def suite():
    suite = unittest.TestSuite()

    # suite.addTest(TestSetContractRequired('test_success'))

    # suite.addTest(TestSetContractRequired('test_missingCompanyAdminKey'))
    # suite.addTest(TestSetContractRequired('test_nullCompanyAdminKey'))
    # suite.addTest(TestSetContractRequired('test_intCompanyAdminKey'))
    # suite.addTest(TestSetContractRequired('test_floatCompanyAdminKey'))
    # suite.addTest(TestSetContractRequired('test_stringCompanyAdminKey'))
    # suite.addTest(TestSetContractRequired('test_arrayCompanyAdminKey'))

    # suite.addTest(TestSetContractRequired('test_missingIsPhoneRequired'))
    # suite.addTest(TestSetContractRequired('test_nullIsPhoneRequired'))
    # suite.addTest(TestSetContractRequired('test_intIsPhoneRequired'))
    # suite.addTest(TestSetContractRequired('test_floatIsPhoneRequired'))
    # suite.addTest(TestSetContractRequired('test_stringIsPhoneRequired'))
    # suite.addTest(TestSetContractRequired('test_arrayIsPhoneRequired'))

    suite.addTest(TestSetContractRequired('test_missingIsEmailRequired'))
    suite.addTest(TestSetContractRequired('test_nullIsEmailRequired'))
    suite.addTest(TestSetContractRequired('test_intIsEmailRequired'))
    suite.addTest(TestSetContractRequired('test_floatIsEmailRequired'))
    suite.addTest(TestSetContractRequired('test_stringIsEmailRequired'))
    suite.addTest(TestSetContractRequired('test_arrayIsEmailRequired'))

    return suite
    
    
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())