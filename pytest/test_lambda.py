import main_utils
import unittest
unittest.TestLoader.sortTestMethodsUsing = None
import time

class Test(unittest.TestCase):
    def test_a_setup_class(self):
        print('\r\nCreating the lambda functn...')
        main_utils.create_lambda('lambda')
        time.sleep(100)
        print('coming out of sleep of create lambda')
    def test_b_invoke_function_and_response(self):
        print('\r\nInvoking the lambda function...')
        payload = main_utils.invoke_function('lambda')
        self.assertEqual(payload['message'], 'Hello User!')
    def test_c_teardown_class(self):
        print('\r\nDeleting the lambda function...')
        main_utils.delete_lambda('lambda')