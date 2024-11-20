# import localstack_lambda
# import unittest
# unittest.TestLoader.sortTestMethodsUsing=None

# class Test(unittest.TestCase):
#     def test_a_setup_class(self):
#         print('creating lambda function')
#         localstack_lambda.create_lambda('lambda')


#     def test_b_invoke_function_and_response(self):
#         print('invokin the function')
#         payload=localstack_lambda.invoke_function('lambda')
#         self.assertEqual(payload['message'], 'Hello User')


#     def test_c_teardown_class(self):
#         print('deleting the lambda function')
#         localstack_lambda.delete_lambda('lambda')
