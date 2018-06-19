import sys, unittest, AuthenticateShell

'''
    Authenticate create user end point.
    
    Purpose - creates a user account
    
    Notes - 

    Method signature:
        create_user(self, firstName='', lastName='', email='', phone='',
                companyAdminKey='', country='', firstNameExclude=False,
                lastNameExclude=False, emailExclude=False, phoneExclude=False,
                companyAdminKeyExclude=False, countryExclude=False):
    
    Required:
        firstName
        lastName
        email
        phone
        companyAdminKey
        country

    Test cases
        Successfully create a user.

        FirstName missing from request call.
        Null FirstName value. 
        Int FirstName value.    
        Float FirstName value.   
        String FirstName value.
        Array FirstName value.  

        LastName missing from request call.
        Null LastName value. 
        Int LastName value.    
        Float LastName value.   
        String LastName value.
        Array LastName value.   

        Email missing from request call.
        Null Email value. 
        Int Email value.    
        Float Email value.   
        String Email value.
        Array Email value.  

        Phone missing from request call.
        Null Phone value. 
        Int Phone value.    
        Float Phone value.   
        String Phone value.
        Array Phone value. 

        CompanyAdminKey missing from request call.
        Null CompanyAdminKey value. 
        Int CompanyAdminKey value.    
        Float CompanyAdminKey value.   
        String CompanyAdminKey value.
        Array CompanyAdminKey value.  

        Country missing from request call.
        Null Country value. 
        Int Country value.    
        Float Country value.   
        String Country value.
        Array Country value.  
'''
class TestCreateUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        try:
            cls.user = AuthenticateShell.Authenticate()      
        except:
            print("Unexpected error during setUpClass:", sys.exc_info()[0])


    @classmethod
    def tearDownClass(cls):
        try:
            pass
        except:
            print("Unexpected error during tearDownClass:", sys.exc_info()[0])



    # Successfully crete a user.
    def test_success(self):
        responseBody = self.user.create_user(firstName = AuthenticateShell.data["firstName"], 
                                             lastName = AuthenticateShell.data["lastName"], 
                                             email = AuthenticateShell.data["email"], 
                                             phone = AuthenticateShell.data["phone"], 
                                             companyAdminKey = AuthenticateShell.data["company_admin_key"], 
                                             country = AuthenticateShell.data["country"])

        self.assertEqual(responseBody['successful'], True,
                         msg='test_success assert#1 has failed.')

        self.assertEqual(responseBody['firstName'], AuthenticateShell.data["firstName"],
                         msg='test_success assert#2 has failed.')

        self.assertEqual(responseBody['lastName'], AuthenticateShell.data["lastName"],
                         msg='test_success assert#3 has failed.')

        self.assertEqual(responseBody['companyId'], AuthenticateShell.data["company_admin_key"],
                         msg='test_success assert#4 has failed.')

        self.assertEqual(responseBody['userId'], self.user.GetUserId(),
                         msg='test_success assert#5 has failed.')

        self.assertEqual(responseBody['accessCode'], self.user.GetAccessCode(),
                         msg='test_success assert#6 has failed.')



    # *********************************************************************
    # *                         FirstName tests                           *
    # *********************************************************************
    
    
        
    # Missing FirstName information from request call.
    def test_missingFirstName(self):
        responseBody = self.user.create_user(firstName = AuthenticateShell.data["firstName"], 
                                             lastName = AuthenticateShell.data["lastName"], 
                                             email = AuthenticateShell.data["email"], 
                                             phone = AuthenticateShell.data["phone"], 
                                             companyAdminKey = AuthenticateShell.data["company_admin_key"], 
                                             country = AuthenticateShell.data["country"],
                                             firstNameExclude = True)

        self.assertEqual(responseBody['errorMessage'], "first name required",
                         msg='test_missingFirstName assert#1 has failed.')
        
        
        
    # Test a null FirstName.
    def test_nullFirstName(self):
        responseBody = self.user.create_user(firstName = '', 
                                             lastName = AuthenticateShell.data["lastName"], 
                                             email = AuthenticateShell.data["email"], 
                                             phone = AuthenticateShell.data["phone"], 
                                             companyAdminKey = AuthenticateShell.data["company_admin_key"], 
                                             country = AuthenticateShell.data["country"])

        self.assertEqual(responseBody['errorMessage'], "first name required",
                          msg='test_nullFirstName assert#1 has failed.')



    # Test a int FirstName.
    @unittest.skip("Validation bug - integer first name")
    def test_intFirstName(self):
        responseBody = self.user.create_user(firstName = 123456789, 
                                             lastName = AuthenticateShell.data["lastName"], 
                                             email = AuthenticateShell.data["email"], 
                                             phone = AuthenticateShell.data["phone"], 
                                             companyAdminKey = AuthenticateShell.data["company_admin_key"], 
                                             country = AuthenticateShell.data["country"])

        self.assertEqual(responseBody['errorMessage'], "first name required",
                          msg='test_intFirstName assert#1 has failed.')



    # Test a float FirstName.
    @unittest.skip("Validation bug - float first name")
    def test_floatFirstName(self):
        responseBody = self.user.create_user(firstName = 12.3456789, 
                                             lastName = AuthenticateShell.data["lastName"], 
                                             email = AuthenticateShell.data["email"], 
                                             phone = AuthenticateShell.data["phone"], 
                                             companyAdminKey = AuthenticateShell.data["company_admin_key"], 
                                             country = AuthenticateShell.data["country"])

        self.assertEqual(responseBody['errorMessage'], "first name required",
                          msg='test_floatFirstName assert#1 has failed.')
        
        
        
    # Test a string FirstName value call.
    def test_stringFirstName(self):
        responseBody = self.user.create_user(firstName = "Will always pass - no need to test", 
                                             lastName = AuthenticateShell.data["lastName"], 
                                             email = AuthenticateShell.data["email"], 
                                             phone = AuthenticateShell.data["phone"], 
                                             companyAdminKey = AuthenticateShell.data["company_admin_key"], 
                                             country = AuthenticateShell.data["country"])

        self.assertEqual(responseBody['successful'], True,
                          msg='test_stringFirstName assert#1 has failed.')



    # Test an array FirstName value call.
    def test_arrayFirstName(self):
        responseBody = self.user.create_user(firstName = ['will break'], 
                                             lastName = AuthenticateShell.data["lastName"], 
                                             email = AuthenticateShell.data["email"], 
                                             phone = AuthenticateShell.data["phone"], 
                                             companyAdminKey = AuthenticateShell.data["company_admin_key"], 
                                             country = AuthenticateShell.data["country"])

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arrayFirstName assert#1 has failed.')



    # *********************************************************************
    # *                         LastName tests                            *
    # *********************************************************************
    
    
        
    # Missing LastName information from request call.
    def test_missingLastName(self):
        responseBody = self.user.create_user(firstName = AuthenticateShell.data["firstName"], 
                                             lastName = AuthenticateShell.data["lastName"], 
                                             email = AuthenticateShell.data["email"], 
                                             phone = AuthenticateShell.data["phone"], 
                                             companyAdminKey = AuthenticateShell.data["company_admin_key"], 
                                             country = AuthenticateShell.data["country"],
                                             lastNameExclude = True)

        self.assertEqual(responseBody['errorMessage'], "last name required",
                         msg='test_missingLastName assert#1 has failed.')
        
        
        
    # Test a null LastName.
    def test_nullLastName(self):
        responseBody = self.user.create_user(firstName = AuthenticateShell.data["firstName"], 
                                             lastName = '', 
                                             email = AuthenticateShell.data["email"], 
                                             phone = AuthenticateShell.data["phone"], 
                                             companyAdminKey = AuthenticateShell.data["company_admin_key"], 
                                             country = AuthenticateShell.data["country"])

        self.assertEqual(responseBody['errorMessage'], "last name required",
                          msg='test_nullLastName assert#1 has failed.')



    # Test a int LastName.
    @unittest.skip("Validation bug - integer first name")
    def test_intLastName(self):
        responseBody = self.user.create_user(firstName = AuthenticateShell.data["firstName"], 
                                             lastName = 846513581351, 
                                             email = AuthenticateShell.data["email"], 
                                             phone = AuthenticateShell.data["phone"], 
                                             companyAdminKey = AuthenticateShell.data["company_admin_key"], 
                                             country = AuthenticateShell.data["country"])

        self.assertEqual(responseBody[''], "",
                          msg='test_intLastName assert#1 has failed.')



    # Test a float LastName.
    @unittest.skip("Validation bug - float first name")
    def test_floatLastName(self):
        responseBody = self.user.create_user(firstName = AuthenticateShell.data["firstName"], 
                                             lastName = 8465135.81351, 
                                             email = AuthenticateShell.data["email"], 
                                             phone = AuthenticateShell.data["phone"], 
                                             companyAdminKey = AuthenticateShell.data["company_admin_key"], 
                                             country = AuthenticateShell.data["country"])

        self.assertEqual(responseBody[''], "",
                          msg='test_floatLastName assert#1 has failed.')
        
        
        
    # Test a string LastName value call.
    def test_stringLastName(self):
        responseBody = self.user.create_user(firstName = AuthenticateShell.data["firstName"], 
                                             lastName = 'Should always pass - no need to test.', 
                                             email = AuthenticateShell.data["email"], 
                                             phone = AuthenticateShell.data["phone"], 
                                             companyAdminKey = AuthenticateShell.data["company_admin_key"], 
                                             country = AuthenticateShell.data["country"])

        self.assertEqual(responseBody['successful'], True,
                          msg='test_stringLastName assert#1 has failed.')



    # Test an array LastName value call.
    def test_arrayLastName(self):
        responseBody = self.user.create_user(firstName = AuthenticateShell.data["firstName"], 
                                             lastName = ['break it all'], 
                                             email = AuthenticateShell.data["email"], 
                                             phone = AuthenticateShell.data["phone"], 
                                             companyAdminKey = AuthenticateShell.data["company_admin_key"], 
                                             country = AuthenticateShell.data["country"])

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arrayLastName assert#1 has failed.')


    

    # *********************************************************************
    # *                            Email tests                            *
    # *********************************************************************
    
    
        
    # Missing Email information from request call.
    def test_missingEmail(self):
        responseBody = self.user.create_user(firstName = AuthenticateShell.data["firstName"], 
                                             lastName = AuthenticateShell.data["lastName"], 
                                             email = AuthenticateShell.data["email"], 
                                             phone = AuthenticateShell.data["phone"], 
                                             companyAdminKey = AuthenticateShell.data["company_admin_key"], 
                                             country = AuthenticateShell.data["country"],
                                             emailExclude = True)

        self.assertEqual(responseBody['errorMessage'], "email required",
                         msg='test_missingEmail assert#1 has failed.')
        
        
        
    # Test a null Email.
    def test_nullEmail(self):
        responseBody = self.user.create_user(firstName = AuthenticateShell.data["firstName"], 
                                             lastName = AuthenticateShell.data["lastName"], 
                                             email = '', 
                                             phone = AuthenticateShell.data["phone"], 
                                             companyAdminKey = AuthenticateShell.data["company_admin_key"], 
                                             country = AuthenticateShell.data["country"])

        self.assertEqual(responseBody['errorMessage'], "email required",
                          msg='test_nullEmail assert#1 has failed.')



    # Test a int Email.
    def test_intEmail(self):
        responseBody = self.user.create_user(firstName = AuthenticateShell.data["firstName"], 
                                             lastName = AuthenticateShell.data["lastName"], 
                                             email = 852465, 
                                             phone = AuthenticateShell.data["phone"], 
                                             companyAdminKey = AuthenticateShell.data["company_admin_key"], 
                                             country = AuthenticateShell.data["country"])

        self.assertEqual(responseBody['errorMessage'], "valid contact email required",
                          msg='test_intEmail assert#1 has failed.')



    # Test a float Email.
    def test_floatEmail(self):
        responseBody = self.user.create_user(firstName = AuthenticateShell.data["firstName"], 
                                             lastName = AuthenticateShell.data["lastName"], 
                                             email = 852.465, 
                                             phone = AuthenticateShell.data["phone"], 
                                             companyAdminKey = AuthenticateShell.data["company_admin_key"], 
                                             country = AuthenticateShell.data["country"])

        self.assertEqual(responseBody['errorMessage'], "valid contact email required",
                          msg='test_floatEmail assert#1 has failed.')
        
        
        
    # Test a string Email value call.
    def test_stringEmail(self):
        responseBody = self.user.create_user(firstName = AuthenticateShell.data["firstName"], 
                                             lastName = AuthenticateShell.data["lastName"], 
                                             email = 'Invalid email format', 
                                             phone = AuthenticateShell.data["phone"], 
                                             companyAdminKey = AuthenticateShell.data["company_admin_key"], 
                                             country = AuthenticateShell.data["country"])

        self.assertEqual(responseBody['errorMessage'], "valid contact email required",
                          msg='test_stringEmail assert#1 has failed.')



    # Test an array Email value call.
    def test_arrayEmail(self):
        responseBody = self.user.create_user(firstName = AuthenticateShell.data["firstName"], 
                                             lastName = AuthenticateShell.data["lastName"], 
                                             email = ['this is totally messed up please fail'], 
                                             phone = AuthenticateShell.data["phone"], 
                                             companyAdminKey = AuthenticateShell.data["company_admin_key"], 
                                             country = AuthenticateShell.data["country"])

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arrayEmail assert#1 has failed.')



   
    # *********************************************************************
    # *                         Phone tests                               *
    # *********************************************************************
    
    
        
    # Missing Phone information from request call.
    def test_missingPhone(self):
        responseBody = self.user.create_user(firstName = AuthenticateShell.data["firstName"], 
                                             lastName = AuthenticateShell.data["lastName"], 
                                             email = AuthenticateShell.data["email"], 
                                             phone = AuthenticateShell.data["phone"], 
                                             companyAdminKey = AuthenticateShell.data["company_admin_key"], 
                                             country = AuthenticateShell.data["country"],
                                             phoneExclude = True)

        self.assertEqual(responseBody['errorMessage'], "phone number required",
                         msg='test_missingPhone assert#1 has failed.')
        
        
        
    # Test a null Phone.
    def test_nullPhone(self):
        responseBody = self.user.create_user(firstName = AuthenticateShell.data["firstName"], 
                                             lastName = AuthenticateShell.data["lastName"], 
                                             email = AuthenticateShell.data["email"], 
                                             phone = '', 
                                             companyAdminKey = AuthenticateShell.data["company_admin_key"], 
                                             country = AuthenticateShell.data["country"])

        self.assertEqual(responseBody['errorMessage'], "phone number required",
                          msg='test_nullPhone assert#1 has failed.')



    # Test a int Phone.
    @unittest.skip("Validation bug - integer phone value")
    def test_intPhone(self):
        responseBody = self.user.create_user(firstName = AuthenticateShell.data["firstName"], 
                                             lastName = AuthenticateShell.data["lastName"], 
                                             email = AuthenticateShell.data["email"], 
                                             phone = 231321321321321321321321321321321, 
                                             companyAdminKey = AuthenticateShell.data["company_admin_key"], 
                                             country = AuthenticateShell.data["country"])

        self.assertEqual(responseBody[''], "",
                          msg='test_intPhone assert#1 has failed.')



    # Test a float Phone.
    @unittest.skip("Validation bug - float phone value")
    def test_floatPhone(self):
        responseBody = self.user.create_user(firstName = AuthenticateShell.data["firstName"], 
                                             lastName = AuthenticateShell.data["lastName"], 
                                             email = AuthenticateShell.data["email"], 
                                             phone = 2313213213213213.21321321321321321, 
                                             companyAdminKey = AuthenticateShell.data["company_admin_key"], 
                                             country = AuthenticateShell.data["country"])

        self.assertEqual(responseBody[''], "",
                          msg='test_floatPhone assert#1 has failed.')
        
        
        
    # Test a string Phone value call.
    @unittest.skip("Validation bug - string phone value")
    def test_stringPhone(self):
        responseBody = self.user.create_user(firstName = AuthenticateShell.data["firstName"], 
                                             lastName = AuthenticateShell.data["lastName"], 
                                             email = AuthenticateShell.data["email"], 
                                             phone = 'This is not a valid number', 
                                             companyAdminKey = AuthenticateShell.data["company_admin_key"], 
                                             country = AuthenticateShell.data["country"])

        self.assertEqual(responseBody[''], "",
                          msg='test_stringPhone assert#1 has failed.')



    # Test an array Phone value call.
    def test_arrayPhone(self):
        responseBody = self.user.create_user(firstName = AuthenticateShell.data["firstName"], 
                                             lastName = AuthenticateShell.data["lastName"], 
                                             email = AuthenticateShell.data["email"], 
                                             phone = ['this is not a valid number'], 
                                             companyAdminKey = AuthenticateShell.data["company_admin_key"], 
                                             country = AuthenticateShell.data["country"])

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arrayPhone assert#1 has failed.')





    # *********************************************************************
    # *                         CompanyAdminKey tests                     *
    # *********************************************************************
    
    
        
    # Missing CompanyAdminKey information from request call.
    def test_missingCompanyAdminKey(self):
        responseBody = self.user.create_user(firstName = AuthenticateShell.data["firstName"], 
                                             lastName = AuthenticateShell.data["lastName"], 
                                             email = AuthenticateShell.data["email"], 
                                             phone = AuthenticateShell.data["phone"], 
                                             companyAdminKey = AuthenticateShell.data["company_admin_key"], 
                                             country = AuthenticateShell.data["country"],
                                             companyAdminKeyExclude = True)

        self.assertEqual(responseBody['errorMessage'], "company admin key required",
                         msg='test_missingCompanyAdminKey assert#1 has failed.')
        
        
        
    # Test a null CompanyAdminKey.
    def test_nullCompanyAdminKey(self):
        responseBody = self.user.create_user(firstName = AuthenticateShell.data["firstName"], 
                                             lastName = AuthenticateShell.data["lastName"], 
                                             email = AuthenticateShell.data["email"], 
                                             phone = AuthenticateShell.data["phone"], 
                                             companyAdminKey = '', 
                                             country = AuthenticateShell.data["country"])

        self.assertEqual(responseBody['errorMessage'], "company admin key required",
                          msg='test_nullCompanyAdminKey assert#1 has failed.')



    # Test a int CompanyAdminKey.
    def test_intCompanyAdminKey(self):
        responseBody = self.user.create_user(firstName = AuthenticateShell.data["firstName"], 
                                             lastName = AuthenticateShell.data["lastName"], 
                                             email = AuthenticateShell.data["email"], 
                                             phone = AuthenticateShell.data["phone"], 
                                             companyAdminKey = 12345678, 
                                             country = AuthenticateShell.data["country"])

        self.assertEqual(responseBody['errorMessage'], "invalid company admin key",
                          msg='test_intCompanyAdminKey assert#1 has failed.')



    # Test a float CompanyAdminKey.
    def test_floatCompanyAdminKey(self):
        responseBody = self.user.create_user(firstName = AuthenticateShell.data["firstName"], 
                                             lastName = AuthenticateShell.data["lastName"], 
                                             email = AuthenticateShell.data["email"], 
                                             phone = AuthenticateShell.data["phone"], 
                                             companyAdminKey = 12345.678, 
                                             country = AuthenticateShell.data["country"])

        self.assertEqual(responseBody['errorMessage'], "invalid company admin key",
                          msg='test_floatCompanyAdminKey assert#1 has failed.')
        
        
        
    # Test a string CompanyAdminKey value call.
    def test_stringCompanyAdminKey(self):
        responseBody = self.user.create_user(firstName = AuthenticateShell.data["firstName"], 
                                             lastName = AuthenticateShell.data["lastName"], 
                                             email = AuthenticateShell.data["email"], 
                                             phone = AuthenticateShell.data["phone"], 
                                             companyAdminKey = 'Not a valid key', 
                                             country = AuthenticateShell.data["country"])

        self.assertEqual(responseBody['errorMessage'], "invalid company admin key",
                          msg='test_stringCompanyAdminKey assert#1 has failed.')



    # Test an array CompanyAdminKey value call.
    def test_arrayCompanyAdminKey(self):
        responseBody = self.user.create_user(firstName = AuthenticateShell.data["firstName"], 
                                             lastName = AuthenticateShell.data["lastName"], 
                                             email = AuthenticateShell.data["email"], 
                                             phone = AuthenticateShell.data["phone"], 
                                             companyAdminKey = ['this is not a valid key'], 
                                             country = AuthenticateShell.data["country"])

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arrayCompanyAdminKey assert#1 has failed.')




    # *********************************************************************
    # *                         Country tests                            *
    # *********************************************************************
    
    
        
    # Missing Country information from request call.
    def test_missingCountry(self):
        responseBody = self.user.create_user(firstName = AuthenticateShell.data["firstName"], 
                                             lastName = AuthenticateShell.data["lastName"], 
                                             email = AuthenticateShell.data["email"], 
                                             phone = AuthenticateShell.data["phone"], 
                                             companyAdminKey = AuthenticateShell.data["company_admin_key"], 
                                             country = AuthenticateShell.data["country"],
                                             countryExclude = True)

        self.assertEqual(responseBody['errorMessage'], "country required",
                         msg='test_missingCountry assert#1 has failed.')
        
        
        
    # Test a null Country.
    def test_nullCountry(self):
        responseBody = self.user.create_user(firstName = AuthenticateShell.data["firstName"], 
                                             lastName = AuthenticateShell.data["lastName"], 
                                             email = AuthenticateShell.data["email"], 
                                             phone = AuthenticateShell.data["phone"], 
                                             companyAdminKey = AuthenticateShell.data["company_admin_key"], 
                                             country = '')

        self.assertEqual(responseBody['errorMessage'], "country required",
                          msg='test_nullCountry assert#1 has failed.')



    # Test a int Country.
    def test_intCountry(self):
        responseBody = self.user.create_user(firstName = AuthenticateShell.data["firstName"], 
                                             lastName = AuthenticateShell.data["lastName"], 
                                             email = AuthenticateShell.data["email"], 
                                             phone = AuthenticateShell.data["phone"], 
                                             companyAdminKey = AuthenticateShell.data["company_admin_key"], 
                                             country = 666666666666)

        self.assertEqual(responseBody['errorMessage'], "Invalid country. Please use 'USA' for United States and 'CAN' for Canada",
                          msg='test_intCountry assert#1 has failed.')



    # Test a float Country.
    def test_floatCountry(self):
        responseBody = self.user.create_user(firstName = AuthenticateShell.data["firstName"], 
                                             lastName = AuthenticateShell.data["lastName"], 
                                             email = AuthenticateShell.data["email"], 
                                             phone = AuthenticateShell.data["phone"], 
                                             companyAdminKey = AuthenticateShell.data["company_admin_key"], 
                                             country = 66666.6666666)

        self.assertEqual(responseBody['errorMessage'], "Invalid country. Please use 'USA' for United States and 'CAN' for Canada",
                          msg='test_floatCountry assert#1 has failed.')
        
        
        
    # Test a string Country value call.
    def test_stringCountry(self):
        responseBody = self.user.create_user(firstName = AuthenticateShell.data["firstName"], 
                                             lastName = AuthenticateShell.data["lastName"], 
                                             email = AuthenticateShell.data["email"], 
                                             phone = AuthenticateShell.data["phone"], 
                                             companyAdminKey = AuthenticateShell.data["company_admin_key"], 
                                             country = 'This is not a valid county')

        self.assertEqual(responseBody['errorMessage'], "Invalid country. Please use 'USA' for United States and 'CAN' for Canada",
                          msg='test_stringCountry assert#1 has failed.')



    # Test an array Country value call.
    def test_arrayCountry(self):
        # Array Country value.
        responseBody = self.user.create_user(firstName = AuthenticateShell.data["firstName"], 
                                             lastName = AuthenticateShell.data["lastName"], 
                                             email = AuthenticateShell.data["email"], 
                                             phone = AuthenticateShell.data["phone"], 
                                             companyAdminKey = AuthenticateShell.data["company_admin_key"], 
                                             country = ['this is not a valid county'])

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arrayCountry assert#1 has failed.')




def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestCreateUser('test_success'))

    suite.addTest(TestCreateUser('test_missingFirstName'))
    suite.addTest(TestCreateUser('test_nullFirstName'))
    suite.addTest(TestCreateUser('test_intFirstName'))
    suite.addTest(TestCreateUser('test_floatFirstName'))
    suite.addTest(TestCreateUser('test_stringFirstName'))
    suite.addTest(TestCreateUser('test_arrayFirstName'))

    suite.addTest(TestCreateUser('test_missingLastName'))
    suite.addTest(TestCreateUser('test_nullLastName'))
    suite.addTest(TestCreateUser('test_intLastName'))
    suite.addTest(TestCreateUser('test_floatLastName'))
    suite.addTest(TestCreateUser('test_stringLastName'))
    suite.addTest(TestCreateUser('test_arrayLastName'))

    suite.addTest(TestCreateUser('test_missingEmail'))
    suite.addTest(TestCreateUser('test_nullEmail'))
    suite.addTest(TestCreateUser('test_intEmail'))
    suite.addTest(TestCreateUser('test_floatEmail'))
    suite.addTest(TestCreateUser('test_stringEmail'))
    suite.addTest(TestCreateUser('test_arrayEmail'))

    suite.addTest(TestCreateUser('test_missingPhone'))
    suite.addTest(TestCreateUser('test_nullPhone'))
    suite.addTest(TestCreateUser('test_intPhone'))
    suite.addTest(TestCreateUser('test_floatPhone'))
    suite.addTest(TestCreateUser('test_stringPhone'))
    suite.addTest(TestCreateUser('test_arrayPhone'))

    suite.addTest(TestCreateUser('test_missingCompanyAdminKey'))
    suite.addTest(TestCreateUser('test_nullCompanyAdminKey'))
    suite.addTest(TestCreateUser('test_intCompanyAdminKey'))
    suite.addTest(TestCreateUser('test_floatCompanyAdminKey'))
    suite.addTest(TestCreateUser('test_stringCompanyAdminKey'))
    suite.addTest(TestCreateUser('test_arrayCompanyAdminKey'))

    suite.addTest(TestCreateUser('test_missingCountry'))
    suite.addTest(TestCreateUser('test_nullCountry'))
    suite.addTest(TestCreateUser('test_intCountry'))
    suite.addTest(TestCreateUser('test_floatCountry'))
    suite.addTest(TestCreateUser('test_stringCountry'))
    suite.addTest(TestCreateUser('test_arrayCountry'))
    
    return suite
    
    
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())