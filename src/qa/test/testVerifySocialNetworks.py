import sys, unittest, AuthenticateShell

'''
    Authenticate verify social networks end point.
    
    Purpose - This is used to confirm valid social media credentials were entered.
    
    Notes - User is from Canada.

    Method signature:
        def verify_social_network(self, accessCode='', network='', socialMediaAccessToken='',
                              socialMediaUserId='', accessCodeExclude=False,
                              networkExclude=True, socialMediaAccessTokenExclude=True,
                              socialMediaUserIdExclude=True):
    
    Required:
        accessCode
        network
        socialMediaAccessToken
        socialMediaUserId

    Test cases
        Successfully verify the users social network.

        AccessCode missing from request call.
        Null AccessCode value. 
        Int AccessCode value.    
        Float AccessCode value.   
        String AccessCode value.
        Array AccessCode value.   

        Network missing from request call.
        Null Network value. 
        Int Network value.    
        Float Network value.   
        String Network value.
        Array Network value. 

        SocialMediaAccessToken missing from request call.
        Null SocialMediaAccessToken value. 
        Int SocialMediaAccessToken value.    
        Float SocialMediaAccessToken value.   
        String SocialMediaAccessToken value.
        Array SocialMediaAccessToken value. 

        SocialMediaUserId missing from request call.
        Null SocialMediaUserId value. 
        Int SocialMediaUserId value.    
        Float SocialMediaUserId value.   
        String SocialMediaUserId value.
        Array SocialMediaUserId value. 
'''
class TestVerifySocialNetworks(unittest.TestCase):

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



    # Successfully update a user.
    def test_success(self):
        responseBody = self.user.verify_social_network(accessCode = self.user.GetAccessCode(), 
                                                       network = AuthenticateShell.data['network'], 
                                                       socialMediaAccessToken = AuthenticateShell.data['socialMediaAccessToken'], 
                                                       socialMediaUserId = AuthenticateShell.data['socialMediaUserId'])

        self.assertEqual(responseBody['successful'], True,
                         msg='test_success assert#1 has failed.')



    # *********************************************************************
    # *                         AccessCode tests                          *
    # *********************************************************************
    
    
        
    # Missing AccessCode information from request call.
    def test_missingAccessCode(self):
        responseBody = self.user.verify_social_network(accessCode = self.user.GetAccessCode(), 
                                                       network = AuthenticateShell.data['network'], 
                                                       socialMediaAccessToken = AuthenticateShell.data['socialMediaAccessToken'], 
                                                       socialMediaUserId = AuthenticateShell.data['socialMediaUserId'],
                                                       accessCodeExclude = True)

        self.assertEqual(responseBody['errorMessage'], "accessCode required",
                         msg='test_missingAccessCode assert#1 has failed.')
        
        
        
    # Test a null AccessCode.
    def test_nullAccessCode(self):
        responseBody = self.user.verify_social_network(accessCode = '', 
                                                       network = AuthenticateShell.data['network'], 
                                                       socialMediaAccessToken = AuthenticateShell.data['socialMediaAccessToken'], 
                                                       socialMediaUserId = AuthenticateShell.data['socialMediaUserId'])

        self.assertEqual(responseBody['errorMessage'], "accessCode required",
                          msg='test_nullAccessCode assert#1 has failed.')



    # Test a int AccessCode.
    def test_intAccessCode(self):
        responseBody = self.user.verify_social_network(accessCode = 124321423423423, 
                                                       network = AuthenticateShell.data['network'], 
                                                       socialMediaAccessToken = AuthenticateShell.data['socialMediaAccessToken'], 
                                                       socialMediaUserId = AuthenticateShell.data['socialMediaUserId'])

        self.assertEqual(responseBody['errorMessage'], "access has expired or does not exist",
                          msg='test_intAccessCode assert#1 has failed.')



    # Test a float AccessCode.
    def test_floatAccessCode(self):
        responseBody = self.user.verify_social_network(accessCode = 23423.412341234, 
                                                       network = AuthenticateShell.data['network'], 
                                                       socialMediaAccessToken = AuthenticateShell.data['socialMediaAccessToken'], 
                                                       socialMediaUserId = AuthenticateShell.data['socialMediaUserId'])

        self.assertEqual(responseBody['errorMessage'], "access has expired or does not exist",
                          msg='test_floatAccessCode assert#1 has failed.')
        
        
        
    # Test a string AccessCode value call.
    def test_stringAccessCode(self):
        responseBody = self.user.verify_social_network(accessCode = 'self.user.GetAccessCode()', 
                                                       network = AuthenticateShell.data['network'], 
                                                       socialMediaAccessToken = AuthenticateShell.data['socialMediaAccessToken'], 
                                                       socialMediaUserId = AuthenticateShell.data['socialMediaUserId'])

        self.assertEqual(responseBody['errorMessage'], "access has expired or does not exist",
                          msg='test_stringAccessCode assert#1 has failed.')



    # Test an array AccessCode value call.
    def test_arrayAccessCode(self):
        responseBody = self.user.verify_social_network(accessCode = [self.user.GetAccessCode()], 
                                                       network = AuthenticateShell.data['network'], 
                                                       socialMediaAccessToken = AuthenticateShell.data['socialMediaAccessToken'], 
                                                       socialMediaUserId = AuthenticateShell.data['socialMediaUserId'])

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arrayAccessCode assert#1 has failed.')




    # *********************************************************************
    # *                         Network tests                             *
    # *********************************************************************
    
    
        
    # Missing Network information from request call.
    def test_missingNetwork(self):
        responseBody = self.user.verify_social_network(accessCode = self.user.GetAccessCode(), 
                                                       network = AuthenticateShell.data['network'], 
                                                       socialMediaAccessToken = AuthenticateShell.data['socialMediaAccessToken'], 
                                                       socialMediaUserId = AuthenticateShell.data['socialMediaUserId'],
                                                       networkExclude = True)

        self.assertEqual(responseBody['errorMessage'], "network required",
                         msg='test_missingNetwork assert#1 has failed.')
        
        
        
    # Test a null Network.
    def test_nullNetwork(self):
        responseBody = self.user.verify_social_network(accessCode = self.user.GetAccessCode(), 
                                                       network = '', 
                                                       socialMediaAccessToken = AuthenticateShell.data['socialMediaAccessToken'], 
                                                       socialMediaUserId = AuthenticateShell.data['socialMediaUserId'])

        self.assertEqual(responseBody['errorMessage'], "network required",
                          msg='test_nullNetwork assert#1 has failed.')



    # Test a int Network.
    #@unittest.skip("Network value can be any integer value (BUG)")
    def test_intNetwork(self):
        responseBody = self.user.verify_social_network(accessCode = self.user.GetAccessCode(), 
                                                       network = 11111111111111, 
                                                       socialMediaAccessToken = AuthenticateShell.data['socialMediaAccessToken'], 
                                                       socialMediaUserId = AuthenticateShell.data['socialMediaUserId'])

        self.assertEqual(responseBody['successful'], True,
                          msg='test_intNetwork assert#1 has failed.')



    # Test a float Network.
    #@unittest.skip("Network value can be any float value (BUG)")
    def test_floatNetwork(self):
        responseBody = self.user.verify_social_network(accessCode = self.user.GetAccessCode(), 
                                                       network = 1111.1111111111, 
                                                       socialMediaAccessToken = AuthenticateShell.data['socialMediaAccessToken'], 
                                                       socialMediaUserId = AuthenticateShell.data['socialMediaUserId'])

        self.assertEqual(responseBody['successful'], True,
                          msg='test_floatNetwork assert#1 has failed.')
        
        
        
    # Test a string Network value call.
    #@unittest.skip("Network value can be any string value (BUG)")
    def test_stringNetwork(self):
        responseBody = self.user.verify_social_network(accessCode = self.user.GetAccessCode(), 
                                                       network = "AuthenticateShell.data['network']", 
                                                       socialMediaAccessToken = AuthenticateShell.data['socialMediaAccessToken'], 
                                                       socialMediaUserId = AuthenticateShell.data['socialMediaUserId'])

        self.assertEqual(responseBody['successful'], True,
                          msg='test_stringNetwork assert#1 has failed.')



    # Test an array Network value call.
    def test_arrayNetwork(self):
        responseBody = self.user.verify_social_network(accessCode = self.user.GetAccessCode(), 
                                                       network = [AuthenticateShell.data['network']], 
                                                       socialMediaAccessToken = AuthenticateShell.data['socialMediaAccessToken'], 
                                                       socialMediaUserId = AuthenticateShell.data['socialMediaUserId'])

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arrayNetwork assert#1 has failed.')


    


    # *********************************************************************
    # *                    SocialMediaAccessToken tests                   *
    # *********************************************************************
    
    

    # Missing SocialMediaAccessToken information from request call.
    #@unittest.skip("socialMediaAccessToken can be entirely excluded")
    def test_missingSocialMediaAccessToken(self):
        responseBody = self.user.verify_social_network(accessCode = self.user.GetAccessCode(), 
                                                       network = AuthenticateShell.data['network'], 
                                                       socialMediaAccessToken = AuthenticateShell.data['socialMediaAccessToken'], 
                                                       socialMediaUserId = AuthenticateShell.data['socialMediaUserId'],
                                                       socialMediaAccessTokenExclude = True)

        self.assertEqual(responseBody['successful'], False,
                         msg='test_missingSocialMediaAccessToken assert#1 has failed.')
        
        
        
    # Test a null SocialMediaAccessToken.
    #@unittest.skip("socialMediaAccessToken can be entirely excluded")
    def test_nullSocialMediaAccessToken(self):
        responseBody = self.user.verify_social_network(accessCode = self.user.GetAccessCode(), 
                                                       network = AuthenticateShell.data['network'], 
                                                       socialMediaAccessToken = '', 
                                                       socialMediaUserId = AuthenticateShell.data['socialMediaUserId'])

        self.assertEqual(responseBody['successful'], False,
                          msg='test_nullSocialMediaAccessToken assert#1 has failed.')



    # Test a int SocialMediaAccessToken.
    #@unittest.skip("socialMediaAccessToken value can be any integer value (BUG)")
    def test_intSocialMediaAccessToken(self):
        responseBody = self.user.verify_social_network(accessCode = self.user.GetAccessCode(), 
                                                       network = AuthenticateShell.data['network'], 
                                                       socialMediaAccessToken = 123852, 
                                                       socialMediaUserId = AuthenticateShell.data['socialMediaUserId'])

        self.assertEqual(responseBody['successful'], True,
                          msg='test_intSocialMediaAccessToken assert#1 has failed.')



    # Test a float SocialMediaAccessToken.
    #@unittest.skip("socialMediaAccessToken value can be any float value (BUG)")
    def test_floatSocialMediaAccessToken(self):
        responseBody = self.user.verify_social_network(accessCode = self.user.GetAccessCode(), 
                                                       network = AuthenticateShell.data['network'], 
                                                       socialMediaAccessToken = 1.23852, 
                                                       socialMediaUserId = AuthenticateShell.data['socialMediaUserId'])

        self.assertEqual(responseBody['successful'], True,
                          msg='test_floatSocialMediaAccessToken assert#1 has failed.')
        
        
        
    # Test a string SocialMediaAccessToken value call.
    #@unittest.skip("socialMediaAccessToken value can be any string value (BUG)")
    def test_stringSocialMediaAccessToken(self):
        responseBody = self.user.verify_social_network(accessCode = self.user.GetAccessCode(), 
                                                       network = AuthenticateShell.data['network'], 
                                                       socialMediaAccessToken = "AuthenticateShell.data['socialMediaAccessToken']", 
                                                       socialMediaUserId = AuthenticateShell.data['socialMediaUserId'])

        self.assertEqual(responseBody['successful'], True,
                          msg='test_stringSocialMediaAccessToken assert#1 has failed.')



    # Test an array SocialMediaAccessToken value call.
    def test_arraySocialMediaAccessToken(self):
        responseBody = self.user.verify_social_network(accessCode = self.user.GetAccessCode(), 
                                                       network = AuthenticateShell.data['network'], 
                                                       socialMediaAccessToken = [AuthenticateShell.data['socialMediaAccessToken']], 
                                                       socialMediaUserId = AuthenticateShell.data['socialMediaUserId'])

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arraySocialMediaAccessToken assert#1 has failed.')





    
    # *********************************************************************
    # *                         SocialMediaUserId tests                   *
    # *********************************************************************
    
    
        
    # Missing SocialMediaUserId information from request call.
    def test_missingSocialMediaUserId(self):
        responseBody = self.user.verify_social_network(accessCode = self.user.GetAccessCode(), 
                                                       network = AuthenticateShell.data['network'], 
                                                       socialMediaAccessToken = AuthenticateShell.data['socialMediaAccessToken'], 
                                                       socialMediaUserId = AuthenticateShell.data['socialMediaUserId'],
                                                       socialMediaUserIdExclude = True)

        self.assertEqual(responseBody['successful'], False,
                         msg='test_missingSocialMediaUserId assert#1 has failed.')
        
        
        
    # Test a null SocialMediaUserId.
    def test_nullSocialMediaUserId(self):
        responseBody = self.user.verify_social_network(accessCode = self.user.GetAccessCode(), 
                                                       network = AuthenticateShell.data['network'], 
                                                       socialMediaAccessToken = AuthenticateShell.data['socialMediaAccessToken'], 
                                                       socialMediaUserId = '')

        self.assertEqual(responseBody['successful'], False,
                          msg='test_nullSocialMediaUserId assert#1 has failed.')



    # Test a int SocialMediaUserId.
    #@unittest.skip("SocialMediaUserId value can be any intger value (BUG)")
    def test_intSocialMediaUserId(self):
        responseBody = self.user.verify_social_network(accessCode = self.user.GetAccessCode(), 
                                                       network = AuthenticateShell.data['network'], 
                                                       socialMediaAccessToken = AuthenticateShell.data['socialMediaAccessToken'], 
                                                       socialMediaUserId = 656666666666666)

        self.assertEqual(responseBody['successful'], True,
                          msg='test_intSocialMediaUserId assert#1 has failed.')



    # Test a float SocialMediaUserId.
    #@unittest.skip("SocialMediaUserId value can be any float value (BUG)")
    def test_floatSocialMediaUserId(self):
        responseBody = self.user.verify_social_network(accessCode = self.user.GetAccessCode(), 
                                                       network = AuthenticateShell.data['network'], 
                                                       socialMediaAccessToken = AuthenticateShell.data['socialMediaAccessToken'], 
                                                       socialMediaUserId = 6.66666666666666)

        self.assertEqual(responseBody['successful'], True,
                          msg='test_floatSocialMediaUserId assert#1 has failed.')
        
        
        
    # Test a string SocialMediaUserId value call.
    #@unittest.skip("SocialMediaUserId value can be any string value (BUG)")
    def test_stringSocialMediaUserId(self):
        responseBody = self.user.verify_social_network(accessCode = self.user.GetAccessCode(), 
                                                       network = AuthenticateShell.data['network'], 
                                                       socialMediaAccessToken = AuthenticateShell.data['socialMediaAccessToken'], 
                                                       socialMediaUserId = "AuthenticateShell.data['socialMediaUserId']")

        self.assertEqual(responseBody['successful'], True,
                          msg='test_stringSocialMediaUserId assert#1 has failed.')



    # Test an array SocialMediaUserId value call.
    def test_arraySocialMediaUserId(self):
        responseBody = self.user.verify_social_network(accessCode = self.user.GetAccessCode(), 
                                                       network = AuthenticateShell.data['network'], 
                                                       socialMediaAccessToken = AuthenticateShell.data['socialMediaAccessToken'], 
                                                       socialMediaUserId = [AuthenticateShell.data['socialMediaUserId']])

        self.assertEqual(responseBody['errorMessage'], "An unknown error has occurred.",
                          msg='test_arraySocialMediaUserId assert#1 has failed.')



def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestVerifySocialNetworks('test_success'))

    suite.addTest(TestVerifySocialNetworks('test_missingAccessCode'))
    suite.addTest(TestVerifySocialNetworks('test_nullAccessCode'))
    suite.addTest(TestVerifySocialNetworks('test_intAccessCode'))
    suite.addTest(TestVerifySocialNetworks('test_floatAccessCode'))
    suite.addTest(TestVerifySocialNetworks('test_stringAccessCode'))
    suite.addTest(TestVerifySocialNetworks('test_arrayAccessCode'))
    
    suite.addTest(TestVerifySocialNetworks('test_missingNetwork'))
    suite.addTest(TestVerifySocialNetworks('test_nullNetwork'))
    suite.addTest(TestVerifySocialNetworks('test_intNetwork'))
    suite.addTest(TestVerifySocialNetworks('test_floatNetwork'))
    suite.addTest(TestVerifySocialNetworks('test_stringNetwork'))
    suite.addTest(TestVerifySocialNetworks('test_arrayNetwork'))

    suite.addTest(TestVerifySocialNetworks('test_missingSocialMediaAccessToken'))
    suite.addTest(TestVerifySocialNetworks('test_nullSocialMediaAccessToken'))
    suite.addTest(TestVerifySocialNetworks('test_intSocialMediaAccessToken'))
    suite.addTest(TestVerifySocialNetworks('test_floatSocialMediaAccessToken'))
    suite.addTest(TestVerifySocialNetworks('test_stringSocialMediaAccessToken'))
    suite.addTest(TestVerifySocialNetworks('test_arraySocialMediaAccessToken'))

    suite.addTest(TestVerifySocialNetworks('test_missingSocialMediaUserId'))
    suite.addTest(TestVerifySocialNetworks('test_nullSocialMediaUserId'))
    suite.addTest(TestVerifySocialNetworks('test_intSocialMediaUserId'))
    suite.addTest(TestVerifySocialNetworks('test_floatSocialMediaUserId'))
    suite.addTest(TestVerifySocialNetworks('test_stringSocialMediaUserId'))
    suite.addTest(TestVerifySocialNetworks('test_arraySocialMediaUserId'))

    return suite
    
    
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())