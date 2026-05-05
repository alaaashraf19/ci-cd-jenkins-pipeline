import unittest
import xmlrunner

loader = unittest.TestLoader()
suite = loader.discover('.', pattern='TestCalculator.py')

with open('test-results.xml', 'wb') as output:
    xmlrunner.XMLTestRunner(output=output).run(suite)