import main_utils
import unittest
unittest.TestLoader.sortTestMethodsUsing = None
import time

class Test(unittest.TestCase):
    def test_a_setup_class(self):
        print('\r\nCreating the lambda functn...')
        args={
            'Environment': {
                'Variables':
                {
                    'LocalStack': 'True'
                }
            }
        }
        main_utils.create_lambda('lambda',**args)
        main_utils.create_bucket('hands-on-cloud-bucket')
        
  
    def test_b_invoke_function_and_response(self):
        print('\r\nInvoking the lambda function...')
        payload = main_utils.invoke_function('lambda')
        bucket_objects=main_utils.list_s3_bucket_objects('hands-on-cloud-bucket')
        # self.assertEqual(bucket_objects,['hands-on-cloud.txt'])
    def test_c_teardown_class(self):
        print('\r\nDeleting the lambda function...')
        main_utils.delete_lambda('lambda')