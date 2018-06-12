import sys, unittest, AuthenticateShell

'''
    Authenticate upload id end point.
    
    Purpose - This is used to capture data from an ID and, if determined 
              to be a valid ID, auto-fill forms.

    Method signature:
        def upload_id(self, accessCode='', idFront='', idBack='',
                      accessCodeExclude=False, idBackExclude=False,
                      idFrontExclude=False, sandBox=False):

    Note: THIS END POINT IS BROKEN DUE TO SAND BOXING.

    Required:
        accessCode
        idFront
        idBack

    Test cases
        Successfully upload a drivers license id.

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
                                 country = AuthenticateShell.data["country"])
            
            cls.frontId, cls.backId = AuthenticateShell.base64Encode()
        except:
            print("Unexpected error during setUpClass:", sys.exc_info()[0])


    @classmethod
    def tearDownClass(cls):
        try:
            pass
        except:
            print("Unexpected error during tearDownClass:", sys.exc_info()[0])



    # Successfully upload a drivers license id.
    def test_success(self):
        responseBody = self.user.upload_id(accessCode = self.user.GetAccessCode(), 
                                           idFront = self.frontId, 
                                           idBack = self.backId,
                                           sandBox=True)

        self.assertNotEqual(responseBody, '',
                         msg='test_success assert#1 has failed.')



    # # *********************************************************************
    # # *                         AccessCode tests                          *
    # # *********************************************************************
    
    
        
    # # Missing AccessCode information from request call.
    # def test_missingAccessCode(self):
    #     responseBody = self.user.

    #     self.assertEqual(responseBody['errorMessage'], "please submit access number",
    #                      msg='test_missingAccessCode assert#1 has failed.')
        
        
        
    # # Test a null AccessCode.
    # def test_nullAccessCode(self):
    #     responseBody = self.user.

    #     self.assertEqual(responseBody['errorMessage'], "please submit access number",
    #                       msg='test_nullAccessCode assert#1 has failed.')



    # # Test a int AccessCode.
    # def test_intAccessCode(self):
    #     responseBody = self.user.

    #     self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
    #                       msg='test_intAccessCode assert#1 has failed.')



    # # Test a float AccessCode.
    # def test_floatAccessCode(self):
    #     responseBody = self.user.

    #     self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
    #                       msg='test_floatAccessCode assert#1 has failed.')
        
        
        
    # # Test a string AccessCode value call.
    # def test_stringAccessCode(self):
    #     responseBody = self.user.

    #     self.assertEqual(responseBody['errorMessage'], "access has expired or does not exist",
    #                       msg='test_stringAccessCode assert#1 has failed.')



    # # Test an array AccessCode value call.
    # def test_arrayAccessCode(self):
    #     responseBody = self.user.

    #     self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
    #                       msg='test_arrayAccessCode assert#1 has failed.')


    
    # # *********************************************************************
    # # *                          idFront tests                               *
    # # *********************************************************************
    
    
        
    # # Missing idFront information from request call.
    # def test_missingImg1(self):
    #     responseBody = self.user.

    #     self.assertEqual(responseBody['errorMessage'], "please submit image 1",
    #                      msg='test_missingImg1 assert#1 has failed.')
        
        
        
    # # Test a null Img1.
    # def test_nullImg1(self):
    #     responseBody = self.user.

    #     self.assertEqual(responseBody['errorMessage'], "please submit image 1",
    #                       msg='test_nullImg1 assert#1 has failed.')



    # # Test a int Img1.
    # def test_intImg1(self):
    #     responseBody = self.user.

    #     self.assertEqual(responseBody['errorMessage'], "img1 is not a valid base-64 string.",
    #                       msg='test_intImg1 assert#1 has failed.')



    # # Test a float Img1.
    # def test_floatImg1(self):
    #     responseBody = self.user.

    #     self.assertEqual(responseBody['errorMessage'], "img1 is not a valid base-64 string.",
    #                       msg='test_floatImg1 assert#1 has failed.')
        
        
        
    # # Test a string Img1 value call.
    # def test_stringImg1(self):
    #     responseBody = self.user.

    #     self.assertEqual(responseBody['errorMessage'], "img1 is not a valid base-64 string.",
    #                       msg='test_stringImg1 assert#1 has failed.')



    # # Test an array Img1 value call.
    # def test_arrayImg1(self):
    #     responseBody = self.user.

    #     self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
    #                       msg='test_arrayImg1 assert#1 has failed.')




    # # *********************************************************************
    # # *                           Img2 tests                              *
    # # *********************************************************************
    
    
        
    # # Missing Img2 information from request call.
    # def test_missingImg2(self):
    #     responseBody = self.user.

    #     self.assertEqual(responseBody['errorMessage'], "please submit image 2",
    #                      msg='test_missingImg2 assert#1 has failed.')
        
        
        
    # # Test a null Img2.
    # def test_nullImg2(self):
    #     responseBody = self.user.

    #     self.assertEqual(responseBody['errorMessage'], "please submit image 2",
    #                       msg='test_nullImg2 assert#1 has failed.')



    # # Test a int Img2.
    # def test_intImg2(self):
    #     responseBody = self.user.

    #     self.assertEqual(responseBody['errorMessage'], "img2 is not a valid base-64 string.",
    #                       msg='test_intImg2 assert#1 has failed.')



    # # Test a float Img2.
    # def test_floatImg2(self):
    #     responseBody = self.user.

    #     self.assertEqual(responseBody['errorMessage'], "img2 is not a valid base-64 string.",
    #                       msg='test_floatImg2 assert#1 has failed.')
        
        
        
    # # Test a string Img2 value call.
    # def test_stringImg2(self):
    #     responseBody = self.user.

    #     self.assertEqual(responseBody['errorMessage'], "img2 is not a valid base-64 string.",
    #                       msg='test_stringImg2 assert#1 has failed.')



    # # Test an array Img2 value call.
    # def test_arrayImg2(self):
    #     responseBody = self.user.

    #     self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
    #                       msg='test_arrayImg2 assert#1 has failed.')



def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestComparePhotos('test_success'))

    # suite.addTest(TestComparePhotos('test_missingAccessCode'))
    # suite.addTest(TestComparePhotos('test_nullAccessCode'))
    # suite.addTest(TestComparePhotos('test_intAccessCode'))
    # suite.addTest(TestComparePhotos('test_floatAccessCode'))
    # suite.addTest(TestComparePhotos('test_stringAccessCode'))
    # suite.addTest(TestComparePhotos('test_arrayAccessCode'))

    # suite.addTest(TestComparePhotos('test_missingImg1'))
    # suite.addTest(TestComparePhotos('test_nullImg1'))
    # suite.addTest(TestComparePhotos('test_intImg1'))
    # suite.addTest(TestComparePhotos('test_floatImg1'))
    # suite.addTest(TestComparePhotos('test_stringImg1'))
    # suite.addTest(TestComparePhotos('test_arrayImg1'))

    # suite.addTest(TestComparePhotos('test_missingImg2'))
    # suite.addTest(TestComparePhotos('test_nullImg2'))
    # suite.addTest(TestComparePhotos('test_intImg2'))
    # suite.addTest(TestComparePhotos('test_floatImg2'))
    # suite.addTest(TestComparePhotos('test_stringImg2'))
    # suite.addTest(TestComparePhotos('test_arrayImg2'))

    return suite
    
    
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())