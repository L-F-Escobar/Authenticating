import sys, unittest, AuthenticateShell

'''
    Authenticate verify quiz end point.
    
    Purpose - This is used to complete the Identity Proof Quiz. The users will give 
              their answers to the multiple choice questions and this will score 
              their results.
    
    Notes - 

    Method signature:
        def verify_quiz(self, accessCode='', quizId='', transactionID='', responseUniqueId='',
                        answers=[], accessCodeExclude=False, quizIdExclude=False,
                        transactionIDExclude=False, responseUniqueIdExclude=False,
                        answersExclude=False, sandBox=False):

    Required:
        accessCode
        quizId
        transactionID
        responseUniqueId
        answers

    Test cases
        Successfully get test results.

        AccessCode missing from request call.
        Null AccessCode value. 
        Int AccessCode value.    
        Float AccessCode value.   
        String AccessCode value.
        Array AccessCode value.   

        QuizId missing from request call.
        Null QuizId value. 
        Int QuizId value.    
        Float QuizId value.   
        String QuizId value.
        Array QuizId value. 

        TransactionId missing from request call.
        Null TransactionId value. 
        Int TransactionId value.    
        Float TransactionId value.   
        String TransactionId value.
        Array TransactionId value. 

        ResponseId missing from request call.
        Null ResponseId value. 
        Int ResponseId value.    
        Float ResponseId value.   
        String ResponseId value.
        Array ResponseId value. 

        Answers missing from request call.
        Null Answers value. 
        Int Answers value.    
        Float Answers value.   
        String Answers value.
        Array Answers value. 
        
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

        except:
            print("Unexpected error during setUpClass:", sys.exc_info()[0])


    @classmethod
    def tearDownClass(cls):
        try:
            pass
        except:
            print("Unexpected error during tearDownClass:", sys.exc_info()[0])



    # Successfully verify a quiz.
    def test_success(self):
        responseBody = self.user.verify_quiz(self.user.GetAccessCode(), self.user.GetQuizId(), 
                                             self.user.GetTransactionId(), self.user.GetResponseUniqueId(), 
                                             self.user.GetAnswers(), sandBox=True)

        self.assertEqual(responseBody['result'], 'PASS',
                         msg='test_success assert#1 has failed.')



    # # *********************************************************************
    # # *                         AccessCode tests                          *
    # # *********************************************************************
    
    
        
    # # Missing AccessCode information from request call.
    # def test_missingAccessCode(self):
    #     responseBody = self.user.verify_quiz(accessCode = self.user.GetAccessCode(), 
    #                                          quizId = self.user.GetQuizId(), 
    #                                          transactionID = self.user.GetTransactionId(), 
    #                                          responseUniqueId = self.user.GetResponseUniqueId(), 
    #                                          answers = self.user.GetAnswers(), 
    #                                          sandBox=True,
    #                                          accessCodeExclude = True)

    #     self.assertEqual(responseBody['errorMessage'], "access code is required",
    #                      msg='test_missingAccessCode assert#1 has failed.')
        
        
        
    # # Test a null AccessCode.
    # def test_nullAccessCode(self):
    #     responseBody = self.user.verify_quiz(accessCode = '', 
    #                                          quizId = self.user.GetQuizId(), 
    #                                          transactionID = self.user.GetTransactionId(), 
    #                                          responseUniqueId = self.user.GetResponseUniqueId(), 
    #                                          answers = self.user.GetAnswers(), 
    #                                          sandBox=True)

    #     self.assertEqual(responseBody['errorMessage'], 'access code is required',
    #                      msg='test_nullAccessCode assert#1 has failed.')



    # # Test a int AccessCode.
    # def test_intAccessCode(self):
    #     responseBody = self.user.verify_quiz(accessCode = 1, 
    #                                          quizId = self.user.GetQuizId(), 
    #                                          transactionID = self.user.GetTransactionId(), 
    #                                          responseUniqueId = self.user.GetResponseUniqueId(), 
    #                                          answers = self.user.GetAnswers(), 
    #                                          sandBox=True)

    #     self.assertEqual(responseBody['errorMessage'], "Invalid Access Code",
    #                      msg='test_intAccessCode assert#1 has failed.')



    # # Test a float AccessCode.
    # def test_floatAccessCode(self):
    #     responseBody = self.user.verify_quiz(accessCode = 1.1, 
    #                                          quizId = self.user.GetQuizId(), 
    #                                          transactionID = self.user.GetTransactionId(), 
    #                                          responseUniqueId = self.user.GetResponseUniqueId(), 
    #                                          answers = self.user.GetAnswers(), 
    #                                          sandBox=True)

    #     self.assertEqual(responseBody['errorMessage'], 'Invalid Access Code',
    #                      msg='test_floatAccessCode assert#1 has failed.')
        
        
        
    # # Test a string AccessCode value call.
    # def test_stringAccessCode(self):
    #     responseBody = self.user.verify_quiz(accessCode = 'self.user.GetAccessCode()', 
    #                                          quizId = self.user.GetQuizId(), 
    #                                          transactionID = self.user.GetTransactionId(), 
    #                                          responseUniqueId = self.user.GetResponseUniqueId(), 
    #                                          answers = self.user.GetAnswers(), 
    #                                          sandBox=True)

    #     self.assertEqual(responseBody['errorMessage'], 'Invalid Access Code',
    #                      msg='test_stringAccessCode assert#1 has failed.')



    # # Test an array AccessCode value call.
    # def test_arrayAccessCode(self):
    #     responseBody = self.user.verify_quiz(accessCode = [self.user.GetAccessCode()], 
    #                                          quizId = self.user.GetQuizId(), 
    #                                          transactionID = self.user.GetTransactionId(), 
    #                                          responseUniqueId = self.user.GetResponseUniqueId(), 
    #                                          answers = self.user.GetAnswers(), 
    #                                          sandBox=True)

    #     self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
    #                      msg='test_arrayAccessCode assert#1 has failed.')








                    
    # # *********************************************************************
    # # *                         QuizId tests                          *
    # # *********************************************************************
    
    
        
    # # Missing QuizId information from request call.
    # def test_missingQuizId(self):
    #     responseBody = self.user.verify_quiz(accessCode = self.user.GetAccessCode(), 
    #                                          quizId = self.user.GetQuizId(), 
    #                                          transactionID = self.user.GetTransactionId(), 
    #                                          responseUniqueId = self.user.GetResponseUniqueId(), 
    #                                          answers = self.user.GetAnswers(), 
    #                                          sandBox=True)

    #     self.assertEqual(responseBody['errorMessage'], "access code is required",
    #                      msg='test_missingAccessCode assert#1 has failed.')
        
        
        
    # # Test a null AccessCode.
    # def test_nullAccessCode(self):
    #     responseBody = self.user.verify_quiz(accessCode = self.user.GetAccessCode(), 
    #                                          quizId = self.user.GetQuizId(), 
    #                                          transactionID = self.user.GetTransactionId(), 
    #                                          responseUniqueId = self.user.GetResponseUniqueId(), 
    #                                          answers = self.user.GetAnswers(), 
    #                                          sandBox=True)

    #     self.assertEqual(responseBody['errorMessage'], 'access code is required',
    #                      msg='test_nullAccessCode assert#1 has failed.')



    # # Test a int AccessCode.
    # def test_intAccessCode(self):
    #     responseBody = self.user.verify_quiz(accessCode = self.user.GetAccessCode(), 
    #                                          quizId = self.user.GetQuizId(), 
    #                                          transactionID = self.user.GetTransactionId(), 
    #                                          responseUniqueId = self.user.GetResponseUniqueId(), 
    #                                          answers = self.user.GetAnswers(), 
    #                                          sandBox=True)

    #     self.assertEqual(responseBody['errorMessage'], "Invalid Access Code",
    #                      msg='test_intAccessCode assert#1 has failed.')



    # # Test a float AccessCode.
    # def test_floatAccessCode(self):
    #     responseBody = self.user.verify_quiz(accessCode = self.user.GetAccessCode(), 
    #                                          quizId = self.user.GetQuizId(), 
    #                                          transactionID = self.user.GetTransactionId(), 
    #                                          responseUniqueId = self.user.GetResponseUniqueId(), 
    #                                          answers = self.user.GetAnswers(), 
    #                                          sandBox=True)

    #     self.assertEqual(responseBody['errorMessage'], 'Invalid Access Code',
    #                      msg='test_floatAccessCode assert#1 has failed.')
        
        
        
    # # Test a string AccessCode value call.
    # def test_stringAccessCode(self):
    #     responseBody = self.user.verify_quiz(accessCode = self.user.GetAccessCode(), 
    #                                          quizId = self.user.GetQuizId(), 
    #                                          transactionID = self.user.GetTransactionId(), 
    #                                          responseUniqueId = self.user.GetResponseUniqueId(), 
    #                                          answers = self.user.GetAnswers(), 
    #                                          sandBox=True)

    #     self.assertEqual(responseBody['errorMessage'], 'Invalid Access Code',
    #                      msg='test_stringAccessCode assert#1 has failed.')



    # # Test an array AccessCode value call.
    # def test_arrayAccessCode(self):
    #     responseBody = self.user.verify_quiz(accessCode = self.user.GetAccessCode(), 
    #                                          quizId = self.user.GetQuizId(), 
    #                                          transactionID = self.user.GetTransactionId(), 
    #                                          responseUniqueId = self.user.GetResponseUniqueId(), 
    #                                          answers = self.user.GetAnswers(), 
    #                                          sandBox=True)

    #     self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
    #                      msg='test_arrayAccessCode assert#1 has failed.')


















    # # *********************************************************************
    # # *                         TransactionId tests                          *
    # # *********************************************************************
    
    
        
    # # Missing TransactionId information from request call.
    # def test_missingTransactionId(self):
    #     responseBody = self.user.verify_quiz(accessCode = self.user.GetAccessCode(), 
    #                                          quizId = self.user.GetQuizId(), 
    #                                          transactionID = self.user.GetTransactionId(), 
    #                                          responseUniqueId = self.user.GetResponseUniqueId(), 
    #                                          answers = self.user.GetAnswers(), 
    #                                          sandBox=True)

    #     self.assertEqual(responseBody['errorMessage'], "access code is required",
    #                      msg='test_missingAccessCode assert#1 has failed.')
        
        
        
    # # Test a null AccessCode.
    # def test_nullAccessCode(self):
    #     responseBody = self.user.verify_quiz(accessCode = self.user.GetAccessCode(), 
    #                                          quizId = self.user.GetQuizId(), 
    #                                          transactionID = self.user.GetTransactionId(), 
    #                                          responseUniqueId = self.user.GetResponseUniqueId(), 
    #                                          answers = self.user.GetAnswers(), 
    #                                          sandBox=True)

    #     self.assertEqual(responseBody['errorMessage'], 'access code is required',
    #                      msg='test_nullAccessCode assert#1 has failed.')



    # # Test a int AccessCode.
    # def test_intAccessCode(self):
    #     responseBody = self.user.verify_quiz(accessCode = self.user.GetAccessCode(), 
    #                                          quizId = self.user.GetQuizId(), 
    #                                          transactionID = self.user.GetTransactionId(), 
    #                                          responseUniqueId = self.user.GetResponseUniqueId(), 
    #                                          answers = self.user.GetAnswers(), 
    #                                          sandBox=True)

    #     self.assertEqual(responseBody['errorMessage'], "Invalid Access Code",
    #                      msg='test_intAccessCode assert#1 has failed.')



    # # Test a float AccessCode.
    # def test_floatAccessCode(self):
    #     responseBody = self.user.verify_quiz(accessCode = self.user.GetAccessCode(), 
    #                                          quizId = self.user.GetQuizId(), 
    #                                          transactionID = self.user.GetTransactionId(), 
    #                                          responseUniqueId = self.user.GetResponseUniqueId(), 
    #                                          answers = self.user.GetAnswers(), 
    #                                          sandBox=True)

    #     self.assertEqual(responseBody['errorMessage'], 'Invalid Access Code',
    #                      msg='test_floatAccessCode assert#1 has failed.')
        
        
        
    # # Test a string AccessCode value call.
    # def test_stringAccessCode(self):
    #     responseBody = self.user.verify_quiz(accessCode = self.user.GetAccessCode(), 
    #                                          quizId = self.user.GetQuizId(), 
    #                                          transactionID = self.user.GetTransactionId(), 
    #                                          responseUniqueId = self.user.GetResponseUniqueId(), 
    #                                          answers = self.user.GetAnswers(), 
    #                                          sandBox=True)

    #     self.assertEqual(responseBody['errorMessage'], 'Invalid Access Code',
    #                      msg='test_stringAccessCode assert#1 has failed.')



    # # Test an array AccessCode value call.
    # def test_arrayAccessCode(self):
    #     responseBody = self.user.verify_quiz(accessCode = self.user.GetAccessCode(), 
    #                                          quizId = self.user.GetQuizId(), 
    #                                          transactionID = self.user.GetTransactionId(), 
    #                                          responseUniqueId = self.user.GetResponseUniqueId(), 
    #                                          answers = self.user.GetAnswers(), 
    #                                          sandBox=True)

    #     self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
    #                      msg='test_arrayAccessCode assert#1 has failed.')





















    # # *********************************************************************
    # # *                         ResponseId tests                          *
    # # *********************************************************************
    
    
        
    # # Missing ResponseId information from request call.
    # def test_missingResponseId(self):
    #     responseBody = self.user.verify_quiz(accessCode = self.user.GetAccessCode(), 
    #                                          quizId = self.user.GetQuizId(), 
    #                                          transactionID = self.user.GetTransactionId(), 
    #                                          responseUniqueId = self.user.GetResponseUniqueId(), 
    #                                          answers = self.user.GetAnswers(), 
    #                                          sandBox=True)

    #     self.assertEqual(responseBody['errorMessage'], "access code is required",
    #                      msg='test_missingAccessCode assert#1 has failed.')
        
        
        
    # # Test a null AccessCode.
    # def test_nullAccessCode(self):
    #     responseBody = self.user.verify_quiz(accessCode = self.user.GetAccessCode(), 
    #                                          quizId = self.user.GetQuizId(), 
    #                                          transactionID = self.user.GetTransactionId(), 
    #                                          responseUniqueId = self.user.GetResponseUniqueId(), 
    #                                          answers = self.user.GetAnswers(), 
    #                                          sandBox=True)

    #     self.assertEqual(responseBody['errorMessage'], 'access code is required',
    #                      msg='test_nullAccessCode assert#1 has failed.')



    # # Test a int AccessCode.
    # def test_intAccessCode(self):
    #     responseBody = self.user.verify_quiz(accessCode = self.user.GetAccessCode(), 
    #                                          quizId = self.user.GetQuizId(), 
    #                                          transactionID = self.user.GetTransactionId(), 
    #                                          responseUniqueId = self.user.GetResponseUniqueId(), 
    #                                          answers = self.user.GetAnswers(), 
    #                                          sandBox=True)

    #     self.assertEqual(responseBody['errorMessage'], "Invalid Access Code",
    #                      msg='test_intAccessCode assert#1 has failed.')



    # # Test a float AccessCode.
    # def test_floatAccessCode(self):
    #     responseBody = self.user.verify_quiz(accessCode = self.user.GetAccessCode(), 
    #                                          quizId = self.user.GetQuizId(), 
    #                                          transactionID = self.user.GetTransactionId(), 
    #                                          responseUniqueId = self.user.GetResponseUniqueId(), 
    #                                          answers = self.user.GetAnswers(), 
    #                                          sandBox=True)

    #     self.assertEqual(responseBody['errorMessage'], 'Invalid Access Code',
    #                      msg='test_floatAccessCode assert#1 has failed.')
        
        
        
    # # Test a string AccessCode value call.
    # def test_stringAccessCode(self):
    #     responseBody = self.user.verify_quiz(accessCode = self.user.GetAccessCode(), 
    #                                          quizId = self.user.GetQuizId(), 
    #                                          transactionID = self.user.GetTransactionId(), 
    #                                          responseUniqueId = self.user.GetResponseUniqueId(), 
    #                                          answers = self.user.GetAnswers(), 
    #                                          sandBox=True)

    #     self.assertEqual(responseBody['errorMessage'], 'Invalid Access Code',
    #                      msg='test_stringAccessCode assert#1 has failed.')



    # # Test an array AccessCode value call.
    # def test_arrayAccessCode(self):
    #     responseBody = self.user.verify_quiz(accessCode = self.user.GetAccessCode(), 
    #                                          quizId = self.user.GetQuizId(), 
    #                                          transactionID = self.user.GetTransactionId(), 
    #                                          responseUniqueId = self.user.GetResponseUniqueId(), 
    #                                          answers = self.user.GetAnswers(), 
    #                                          sandBox=True)

    #     self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
    #                      msg='test_arrayAccessCode assert#1 has failed.')











    # # *********************************************************************
    # # *                         Answers tests                          *
    # # *********************************************************************
    
    
        
    # # Missing Answers information from request call.
    # def test_missingAnswers(self):
    #     responseBody = self.user.verify_quiz(accessCode = self.user.GetAccessCode(), 
    #                                          quizId = self.user.GetQuizId(), 
    #                                          transactionID = self.user.GetTransactionId(), 
    #                                          responseUniqueId = self.user.GetResponseUniqueId(), 
    #                                          answers = self.user.GetAnswers(), 
    #                                          sandBox=True)

    #     self.assertEqual(responseBody['errorMessage'], "access code is required",
    #                      msg='test_missingAccessCode assert#1 has failed.')
        
        
        
    # # Test a null AccessCode.
    # def test_nullAccessCode(self):
    #     responseBody = self.user.verify_quiz(accessCode = self.user.GetAccessCode(), 
    #                                          quizId = self.user.GetQuizId(), 
    #                                          transactionID = self.user.GetTransactionId(), 
    #                                          responseUniqueId = self.user.GetResponseUniqueId(), 
    #                                          answers = self.user.GetAnswers(), 
    #                                          sandBox=True)

    #     self.assertEqual(responseBody['errorMessage'], 'access code is required',
    #                      msg='test_nullAccessCode assert#1 has failed.')



    # # Test a int AccessCode.
    # def test_intAccessCode(self):
    #     responseBody = self.user.verify_quiz(accessCode = self.user.GetAccessCode(), 
    #                                          quizId = self.user.GetQuizId(), 
    #                                          transactionID = self.user.GetTransactionId(), 
    #                                          responseUniqueId = self.user.GetResponseUniqueId(), 
    #                                          answers = self.user.GetAnswers(), 
    #                                          sandBox=True)

    #     self.assertEqual(responseBody['errorMessage'], "Invalid Access Code",
    #                      msg='test_intAccessCode assert#1 has failed.')



    # # Test a float AccessCode.
    # def test_floatAccessCode(self):
    #     responseBody = self.user.verify_quiz(accessCode = self.user.GetAccessCode(), 
    #                                          quizId = self.user.GetQuizId(), 
    #                                          transactionID = self.user.GetTransactionId(), 
    #                                          responseUniqueId = self.user.GetResponseUniqueId(), 
    #                                          answers = self.user.GetAnswers(), 
    #                                          sandBox=True)

    #     self.assertEqual(responseBody['errorMessage'], 'Invalid Access Code',
    #                      msg='test_floatAccessCode assert#1 has failed.')
        
        
        
    # # Test a string AccessCode value call.
    # def test_stringAccessCode(self):
    #     responseBody = self.user.verify_quiz(accessCode = self.user.GetAccessCode(), 
    #                                          quizId = self.user.GetQuizId(), 
    #                                          transactionID = self.user.GetTransactionId(), 
    #                                          responseUniqueId = self.user.GetResponseUniqueId(), 
    #                                          answers = self.user.GetAnswers(), 
    #                                          sandBox=True)

    #     self.assertEqual(responseBody['errorMessage'], 'Invalid Access Code',
    #                      msg='test_stringAccessCode assert#1 has failed.')



    # # Test an array AccessCode value call.
    # def test_arrayAccessCode(self):
    #     responseBody = self.user.verify_quiz(accessCode = self.user.GetAccessCode(), 
    #                                          quizId = self.user.GetQuizId(), 
    #                                          transactionID = self.user.GetTransactionId(), 
    #                                          responseUniqueId = self.user.GetResponseUniqueId(), 
    #                                          answers = self.user.GetAnswers(), 
    #                                          sandBox=True)

    #     self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
    #                      msg='test_arrayAccessCode assert#1 has failed.')

    






def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestGetTestResults('test_success'))

    # suite.addTest(TestGetTestResults('test_missingAccessCode'))
    # suite.addTest(TestGetTestResults('test_nullAccessCode'))
    # suite.addTest(TestGetTestResults('test_intAccessCode'))
    # suite.addTest(TestGetTestResults('test_floatAccessCode'))
    # suite.addTest(TestGetTestResults('test_stringAccessCode'))
    # suite.addTest(TestGetTestResults('test_arrayAccessCode'))

    # suite.addTest(TestGetTestResults('test_missingQuizId'))
    # suite.addTest(TestGetTestResults('test_nullQuizId'))
    # suite.addTest(TestGetTestResults('test_intQuizId'))
    # suite.addTest(TestGetTestResults('test_floatQuizId'))
    # suite.addTest(TestGetTestResults('test_stringQuizId'))
    # suite.addTest(TestGetTestResults('test_arrayQuizId'))

    # suite.addTest(TestGetTestResults('test_missingTransactionId'))
    # suite.addTest(TestGetTestResults('test_nullTransactionId'))
    # suite.addTest(TestGetTestResults('test_intTransactionId'))
    # suite.addTest(TestGetTestResults('test_floatTransactionId'))
    # suite.addTest(TestGetTestResults('test_stringTransactionId'))
    # suite.addTest(TestGetTestResults('test_arrayTransactionId'))

    # suite.addTest(TestGetTestResults('test_missingResponseId'))
    # suite.addTest(TestGetTestResults('test_nullResponseId'))
    # suite.addTest(TestGetTestResults('test_intResponseId'))
    # suite.addTest(TestGetTestResults('test_floatResponseId'))
    # suite.addTest(TestGetTestResults('test_stringResponseId'))
    # suite.addTest(TestGetTestResults('test_arrayResponseId'))

    # suite.addTest(TestGetTestResults('test_missingAnswers'))
    # suite.addTest(TestGetTestResults('test_nullAnswers'))
    # suite.addTest(TestGetTestResults('test_intAnswers'))
    # suite.addTest(TestGetTestResults('test_floatAnswers'))
    # suite.addTest(TestGetTestResults('test_stringAnswers'))
    # suite.addTest(TestGetTestResults('test_arrayAnswers'))
    
    return suite
    
    
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())