import unittest, xmlrunner, os
import sys

from test import testCreateUser
from test import testUpdateUser
from test import testGetUser
from test import testVerifyPhone
from test import testVerifyPhoneCode
from test import testVerifyEmail
from test import testVerifySocialNetworks
from test import testGetAvailableSocialNetworks
from test import testComparePhotos
from test import testUploadId
from test import testUploadIdEnhanced
from test import testCheckUploadId
from test import testUploadPassport
from test import testCheckUploadPassword
from test import testSetSocialNetworks
from test import testSetContractRequired
from test import testSetPhotoMatchPercent
from test import testSetDaysExpire
from test import testGetTestResults
from test import testGetQuiz
from test import testVerifyQuiz
from test import testGenCrimReport

# Initialize a test loader & test suite package.
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

## $ python runner.py
if len(sys.argv) == 1:
    # suite.addTests(loader.suiteClass(testCreateUser.suite()))
    # suite.addTests(loader.suiteClass(testUpdateUser.suite()))
    # suite.addTests(loader.suiteClass(testGetUser.suite()))
    # suite.addTests(loader.suiteClass(testVerifyPhone.suite()))
    # suite.addTests(loader.suiteClass(testVerifyPhoneCode.suite()))
    # suite.addTests(loader.suiteClass(testVerifyEmail.suite()))
    # suite.addTests(loader.suiteClass(testVerifySocialNetworks.suite()))
    # suite.addTests(loader.suiteClass(testGetAvailableSocialNetworks.suite()))
    # suite.addTests(loader.suiteClass(testComparePhotos.suite()))
    # suite.addTests(loader.suiteClass(testSetSocialNetworks.suite()))
    # suite.addTests(loader.suiteClass(testSetContractRequired.suite()))
    # suite.addTests(loader.suiteClass(testSetPhotoMatchPercent.suite()))
    suite.addTests(loader.suiteClass(testSetDaysExpire.suite()))
else:
    ## $ python runner.py -sandBox
    if sys.argv[1] == '-sandBox':
        # suite.addTests(loader.suiteClass(testUploadId.suite())) 
        # suite.addTests(loader.suiteClass(testUploadIdEnhanced.suite())) 
        # suite.addTests(loader.suiteClass(testCheckUploadId.suite())) 
        # suite.addTests(loader.suiteClass(testUploadPassport.suite()))
        # suite.addTests(loader.suiteClass(testCheckUploadPassword.suite()))
        # suite.addTests(loader.suiteClass(testGetTestResults.suite()))
        # suite.addTests(loader.suiteClass(testGetQuiz.suite()))
        # suite.addTests(loader.suiteClass(testVerifyQuiz.suite()))
        suite.addTests(loader.suiteClass(testGenCrimReport.suite()))

# Initialize an xml runner.
testRunner=xmlrunner.XMLTestRunner(output='data/testReports', verbosity=2)
 
# Run the suite & save the results.
results = testRunner.run(suite)
  
print(results)