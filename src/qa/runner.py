import unittest, xmlrunner, os

from test import testCreateUser
from test import testUpdateUser
from test import testGetUser

# Initialize a test loader & test suite package.
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# suite.addTests(loader.suiteClass(testCreateUser.suite()))
# suite.addTests(loader.suiteClass(testUpdateUser.suite()))
suite.addTests(loader.suiteClass(testGetUser.suite()))

# Initialize an xml runner.
testRunner=xmlrunner.XMLTestRunner(output='data/testReports', verbosity=2)
 
# Run the suite & save the results.
results = testRunner.run(suite)
  
print(results)