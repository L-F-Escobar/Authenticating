import sys, unittest, AuthenticateShell

'''
    Authenticate upload id end point.
    
    Purpose - This is used to capture data from an ID and, if determined 
              to be a valid ID, auto-fill forms.
              This is different from uploadId in that it is a more rigorous 
              check and is harder to pass.

    Method signature:
        def upload_id_enhanced(self, accessCode='', idFront='', idBack='',
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

        IdFront missing from request call.
        Null IdFront value. 
        Int IdFront value.    
        Float IdFront value.   
        String IdFront value.
        Array IdFront value. 

        IdBack missing from request call.
        Null IdBack value. 
        Int IdBack value.    
        Float IdBack value.   
        String IdBack value.
        Array IdBack value. 
'''
class TestUploadIdEnchanced(unittest.TestCase):

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
        responseBody = self.user.upload_id_enhanced(accessCode = self.user.GetAccessCode(), 
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
    # def test_missingIdFront(self):
    #     responseBody = self.user.

    #     self.assertEqual(responseBody['errorMessage'], "please submit image 1",
    #                      msg='test_missingIdFront assert#1 has failed.')
        
        
        
    # # Test a null IdFront.
    # def test_nullIdFront(self):
    #     responseBody = self.user.

    #     self.assertEqual(responseBody['errorMessage'], "please submit image 1",
    #                       msg='test_nullIdFront assert#1 has failed.')



    # # Test a int IdFront.
    # def test_intIdFront(self):
    #     responseBody = self.user.

    #     self.assertEqual(responseBody['errorMessage'], "IdFront is not a valid base-64 string.",
    #                       msg='test_intIdFront assert#1 has failed.')



    # # Test a float IdFront.
    # def test_floatIdFront(self):
    #     responseBody = self.user.

    #     self.assertEqual(responseBody['errorMessage'], "IdFront is not a valid base-64 string.",
    #                       msg='test_floatIdFront assert#1 has failed.')
        
        
        
    # # Test a string IdFront value call.
    # def test_stringIdFront(self):
    #     responseBody = self.user.

    #     self.assertEqual(responseBody['errorMessage'], "IdFront is not a valid base-64 string.",
    #                       msg='test_stringIdFront assert#1 has failed.')



    # # Test an array IdFront value call.
    # def test_arrayIdFront(self):
    #     responseBody = self.user.

    #     self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
    #                       msg='test_arrayIdFront assert#1 has failed.')




    # # *********************************************************************
    # # *                           IdBack tests                              *
    # # *********************************************************************
    
    
        
    # # Missing IdBack information from request call.
    # def test_missingIdBack(self):
    #     responseBody = self.user.

    #     self.assertEqual(responseBody['errorMessage'], "please submit image 2",
    #                      msg='test_missingIdBack assert#1 has failed.')
        
        
        
    # # Test a null IdBack.
    # def test_nullIdBack(self):
    #     responseBody = self.user.

    #     self.assertEqual(responseBody['errorMessage'], "please submit image 2",
    #                       msg='test_nullIdBack assert#1 has failed.')



    # # Test a int IdBack.
    # def test_intIdBack(self):
    #     responseBody = self.user.

    #     self.assertEqual(responseBody['errorMessage'], "IdBack is not a valid base-64 string.",
    #                       msg='test_intIdBack assert#1 has failed.')



    # # Test a float IdBack.
    # def test_floatIdBack(self):
    #     responseBody = self.user.

    #     self.assertEqual(responseBody['errorMessage'], "IdBack is not a valid base-64 string.",
    #                       msg='test_floatIdBack assert#1 has failed.')
        
        
        
    # # Test a string IdBack value call.
    # def test_stringIdBack(self):
    #     responseBody = self.user.

    #     self.assertEqual(responseBody['errorMessage'], "IdBack is not a valid base-64 string.",
    #                       msg='test_stringIdBack assert#1 has failed.')



    # # Test an array IdBack value call.
    # def test_arrayIdBack(self):
    #     responseBody = self.user.

    #     self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
    #                       msg='test_arrayIdBack assert#1 has failed.')



def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestUploadIdEnchanced('test_success'))

    # suite.addTest(TestUploadIdEnchanced('test_missingAccessCode'))
    # suite.addTest(TestUploadIdEnchanced('test_nullAccessCode'))
    # suite.addTest(TestUploadIdEnchanced('test_intAccessCode'))
    # suite.addTest(TestUploadIdEnchanced('test_floatAccessCode'))
    # suite.addTest(TestUploadIdEnchanced('test_stringAccessCode'))
    # suite.addTest(TestUploadIdEnchanced('test_arrayAccessCode'))

    # suite.addTest(TestUploadIdEnchanced('test_missingIdFront'))
    # suite.addTest(TestUploadIdEnchanced('test_nullIdFront'))
    # suite.addTest(TestUploadIdEnchanced('test_intIdFront'))
    # suite.addTest(TestUploadIdEnchanced('test_floatIdFront'))
    # suite.addTest(TestUploadIdEnchanced('test_stringIdFront'))
    # suite.addTest(TestUploadIdEnchanced('test_arrayIdFront'))

    # suite.addTest(TestUploadIdEnchanced('test_missingIdBack'))
    # suite.addTest(TestUploadIdEnchanced('test_nullIdBack'))
    # suite.addTest(TestUploadIdEnchanced('test_intIdBack'))
    # suite.addTest(TestUploadIdEnchanced('test_floatIdBack'))
    # suite.addTest(TestUploadIdEnchanced('test_stringIdBack'))
    # suite.addTest(TestUploadIdEnchanced('test_arrayIdBack'))

    return suite
    
    
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())