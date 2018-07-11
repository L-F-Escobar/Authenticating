import sys, unittest, AuthenticateShell

'''
    Authenticate compare photos end point.
    
    Purpose - This is used to complete the photo verification process.
              Endpt takes 2 base64 imgs.
              Does not return an indicator as to whether or not they 
              actually passed the photo verification, this endpoint 
              returns a success if the two images sent were successfully 
              uploaded and saved to the database.

    Notes - User is from Canada.

    Method signature:
        def compare_photo(self, accessCode='', img1='', img2='',
                        accessCodeExclude=False, img1Exclude=False,
                        img2Exclude=False):
    
    Required:
        accessCode
        img1
        img2

    Test cases
        Successfully send 2 photos to the data base.

        AccessCode missing from request call.
        Null AccessCode value. 
        Int AccessCode value.    
        Float AccessCode value.   
        String AccessCode value.
        Array AccessCode value.   

        Img1 missing from request call.
        Null Img1 value. 
        Int Img1 value.    
        Float Img1 value.   
        String Img1 value.
        Array Img1 value. 

        Img2 missing from request call.
        Null Img2 value. 
        Int Img2 value.    
        Float Img2 value.   
        String Img2 value.
        Array Img2 value. 
'''
class TestComparePhotos(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        try:
            cls.user = AuthenticateShell.Authenticate()      

            cls.user.create_user(firstName = AuthenticateShell.data["firstName"], 
                                 lastName = AuthenticateShell.data["lastName"], 
                                 email = AuthenticateShell.data["email"], 
                                 phone = AuthenticateShell.data["phone"], 
                                 companyAdminKey = AuthenticateShell.data["company_admin_key"], 
                                 country = AuthenticateShell.data["countryCAN"])
        except:
            print("Unexpected error during setUpClass:", sys.exc_info()[0])


    @classmethod
    def tearDownClass(cls):
        try:
            pass
        except:
            print("Unexpected error during tearDownClass:", sys.exc_info()[0])



    # Successfully send 2 photos to the database.
    def test_success(self):
        responseBody = self.user.compare_photo(accessCode = self.user.GetAccessCode(), 
                                               img1 = AuthenticateShell.data['my_selfie_1'], 
                                               img2 = AuthenticateShell.data['my_selfie_2'])

        self.assertEqual(responseBody['successful'], True,
                         msg='test_success assert#1 has failed.')



    # *********************************************************************
    # *                         AccessCode tests                          *
    # *********************************************************************
    
    
        
    # Missing AccessCode information from request call.
    def test_missingAccessCode(self):
        responseBody = self.user.compare_photo(accessCode = self.user.GetAccessCode(), 
                                               img1 = AuthenticateShell.data['my_selfie_1'], 
                                               img2 = AuthenticateShell.data['my_selfie_2'],
                                               accessCodeExclude = True)

        self.assertEqual(responseBody['errorMessage'], "please submit access number",
                         msg='test_missingAccessCode assert#1 has failed.')
        
        
        
    # Test a null AccessCode.
    def test_nullAccessCode(self):
        responseBody = self.user.compare_photo(accessCode = '', 
                                               img1 = AuthenticateShell.data['my_selfie_1'], 
                                               img2 = AuthenticateShell.data['my_selfie_2'])

        self.assertEqual(responseBody['errorMessage'], "please submit access number",
                          msg='test_nullAccessCode assert#1 has failed.')



    # Test a int AccessCode.
    def test_intAccessCode(self):
        responseBody = self.user.compare_photo(accessCode = 111111111111111, 
                                               img1 = AuthenticateShell.data['my_selfie_1'], 
                                               img2 = AuthenticateShell.data['my_selfie_2'])

        self.assertEqual(responseBody['errorMessage'], "access has expired or does not exist",
                          msg='test_intAccessCode assert#1 has failed.')



    # Test a float AccessCode.
    def test_floatAccessCode(self):
        responseBody = self.user.compare_photo(accessCode = 111.111111111111, 
                                               img1 = AuthenticateShell.data['my_selfie_1'], 
                                               img2 = AuthenticateShell.data['my_selfie_2'])

        self.assertEqual(responseBody['errorMessage'], "access has expired or does not exist",
                          msg='test_floatAccessCode assert#1 has failed.')
        
        
        
    # Test a string AccessCode value call.
    def test_stringAccessCode(self):
        responseBody = self.user.compare_photo(accessCode = "self.user.GetAccessCode()", 
                                               img1 = AuthenticateShell.data['my_selfie_1'], 
                                               img2 = AuthenticateShell.data['my_selfie_2'])

        self.assertEqual(responseBody['errorMessage'], "access has expired or does not exist",
                          msg='test_stringAccessCode assert#1 has failed.')



    # Test an array AccessCode value call.
    def test_arrayAccessCode(self):
        responseBody = self.user.compare_photo(accessCode = [self.user.GetAccessCode()], 
                                               img1 = AuthenticateShell.data['my_selfie_1'], 
                                               img2 = AuthenticateShell.data['my_selfie_2'])

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arrayAccessCode assert#1 has failed.')


    
    # *********************************************************************
    # *                          Img1 tests                               *
    # *********************************************************************
    
    
        
    # Missing Img1 information from request call.
    def test_missingImg1(self):
        responseBody = self.user.compare_photo(accessCode = self.user.GetAccessCode(), 
                                               img1 = AuthenticateShell.data['my_selfie_1'], 
                                               img2 = AuthenticateShell.data['my_selfie_2'],
                                               img1Exclude = True)

        self.assertEqual(responseBody['errorMessage'], "please submit image 1",
                         msg='test_missingImg1 assert#1 has failed.')
        
        
        
    # Test a null Img1.
    def test_nullImg1(self):
        responseBody = self.user.compare_photo(accessCode = self.user.GetAccessCode(), 
                                               img1 = '', 
                                               img2 = AuthenticateShell.data['my_selfie_2'])

        self.assertEqual(responseBody['errorMessage'], "please submit image 1",
                          msg='test_nullImg1 assert#1 has failed.')



    # Test a int Img1.
    def test_intImg1(self):
        responseBody = self.user.compare_photo(accessCode = self.user.GetAccessCode(), 
                                               img1 = 1234684, 
                                               img2 = AuthenticateShell.data['my_selfie_2'])

        self.assertEqual(responseBody['errorMessage'], "img1 is not a valid base-64 string.",
                          msg='test_intImg1 assert#1 has failed.')



    # Test a float Img1.
    def test_floatImg1(self):
        responseBody = self.user.compare_photo(accessCode = self.user.GetAccessCode(), 
                                               img1 = 12346.84, 
                                               img2 = AuthenticateShell.data['my_selfie_2'])

        self.assertEqual(responseBody['errorMessage'], "img1 is not a valid base-64 string.",
                          msg='test_floatImg1 assert#1 has failed.')
        
        
        
    # Test a string Img1 value call.
    def test_stringImg1(self):
        responseBody = self.user.compare_photo(accessCode = self.user.GetAccessCode(), 
                                               img1 = "AuthenticateShell.data['my_selfie_1']", 
                                               img2 = AuthenticateShell.data['my_selfie_2'])

        self.assertEqual(responseBody['errorMessage'], "img1 is not a valid base-64 string.",
                          msg='test_stringImg1 assert#1 has failed.')



    # Test an array Img1 value call.
    def test_arrayImg1(self):
        responseBody = self.user.compare_photo(accessCode = self.user.GetAccessCode(), 
                                               img1 = [AuthenticateShell.data['my_selfie_1']], 
                                               img2 = AuthenticateShell.data['my_selfie_2'])

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arrayImg1 assert#1 has failed.')




    # *********************************************************************
    # *                           Img2 tests                              *
    # *********************************************************************
    
    
        
    # Missing Img2 information from request call.
    def test_missingImg2(self):
        responseBody = self.user.compare_photo(accessCode = self.user.GetAccessCode(), 
                                               img1 = AuthenticateShell.data['my_selfie_1'], 
                                               img2 = AuthenticateShell.data['my_selfie_2'],
                                               img2Exclude = True)

        self.assertEqual(responseBody['errorMessage'], "please submit image 2",
                         msg='test_missingImg2 assert#1 has failed.')
        
        
        
    # Test a null Img2.
    def test_nullImg2(self):
        responseBody = self.user.compare_photo(accessCode = self.user.GetAccessCode(), 
                                               img1 = AuthenticateShell.data['my_selfie_1'], 
                                               img2 = '')

        self.assertEqual(responseBody['errorMessage'], "please submit image 2",
                          msg='test_nullImg2 assert#1 has failed.')



    # Test a int Img2.
    def test_intImg2(self):
        responseBody = self.user.compare_photo(accessCode = self.user.GetAccessCode(), 
                                               img1 = AuthenticateShell.data['my_selfie_1'], 
                                               img2 = 123654)

        self.assertEqual(responseBody['errorMessage'], "img2 is not a valid base-64 string.",
                          msg='test_intImg2 assert#1 has failed.')



    # Test a float Img2.
    def test_floatImg2(self):
        responseBody = self.user.compare_photo(accessCode = self.user.GetAccessCode(), 
                                               img1 = AuthenticateShell.data['my_selfie_1'], 
                                               img2 = 12315.201650)

        self.assertEqual(responseBody['errorMessage'], "img2 is not a valid base-64 string.",
                          msg='test_floatImg2 assert#1 has failed.')
        
        
        
    # Test a string Img2 value call.
    def test_stringImg2(self):
        responseBody = self.user.compare_photo(accessCode = self.user.GetAccessCode(), 
                                               img1 = AuthenticateShell.data['my_selfie_1'], 
                                               img2 = "AuthenticateShell.data['my_selfie_2']")

        self.assertEqual(responseBody['errorMessage'], "img2 is not a valid base-64 string.",
                          msg='test_stringImg2 assert#1 has failed.')



    # Test an array Img2 value call.
    def test_arrayImg2(self):
        responseBody = self.user.compare_photo(accessCode = self.user.GetAccessCode(), 
                                               img1 = AuthenticateShell.data['my_selfie_1'], 
                                               img2 = [AuthenticateShell.data['my_selfie_2']])

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arrayImg2 assert#1 has failed.')



def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestComparePhotos('test_success'))

    suite.addTest(TestComparePhotos('test_missingAccessCode'))
    suite.addTest(TestComparePhotos('test_nullAccessCode'))
    suite.addTest(TestComparePhotos('test_intAccessCode'))
    suite.addTest(TestComparePhotos('test_floatAccessCode'))
    suite.addTest(TestComparePhotos('test_stringAccessCode'))
    suite.addTest(TestComparePhotos('test_arrayAccessCode'))

    suite.addTest(TestComparePhotos('test_missingImg1'))
    suite.addTest(TestComparePhotos('test_nullImg1'))
    suite.addTest(TestComparePhotos('test_intImg1'))
    suite.addTest(TestComparePhotos('test_floatImg1'))
    suite.addTest(TestComparePhotos('test_stringImg1'))
    suite.addTest(TestComparePhotos('test_arrayImg1'))

    suite.addTest(TestComparePhotos('test_missingImg2'))
    suite.addTest(TestComparePhotos('test_nullImg2'))
    suite.addTest(TestComparePhotos('test_intImg2'))
    suite.addTest(TestComparePhotos('test_floatImg2'))
    suite.addTest(TestComparePhotos('test_stringImg2'))
    suite.addTest(TestComparePhotos('test_arrayImg2'))

    return suite
    
    
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())