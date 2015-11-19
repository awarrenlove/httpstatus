import unittest

import httpstatus


class HTTPhttpstatusTest(unittest.TestCase):
    
    
    def test_lt(self):
        self.assertFalse(httpstatus.HTTP_200_OK < 199)
        self.assertFalse(httpstatus.HTTP_200_OK < 200)
        self.assertTrue(httpstatus.HTTP_200_OK < 201)
    
    def test_le(self):
        self.assertFalse(httpstatus.HTTP_200_OK <= 199)
        self.assertTrue(httpstatus.HTTP_200_OK <= 200)
        self.assertTrue(httpstatus.HTTP_200_OK <= 201)

    def test_eq(self):
        self.assertEqual(httpstatus.HTTP_200_OK, 200)
        self.assertEqual(200, httpstatus.HTTP_200_OK)

    def test_ne(self):
        self.assertNotEqual(httpstatus.HTTP_200_OK, 201)
        self.assertNotEqual(201, httpstatus.HTTP_200_OK)
    
    def test_gt(self):
        self.assertTrue(httpstatus.HTTP_200_OK > 199)
        self.assertFalse(httpstatus.HTTP_200_OK > 200)
        self.assertFalse(httpstatus.HTTP_200_OK > 201)
    
    def test_ge(self):
        self.assertTrue(httpstatus.HTTP_200_OK >= 199)
        self.assertTrue(httpstatus.HTTP_200_OK >= 200)
        self.assertFalse(httpstatus.HTTP_200_OK >= 201)
    
    def test_int(self):
        httpstatus_int = int(httpstatus.HTTP_200_OK)
        self.assertTrue(type(httpstatus_int) == int)
        self.assertTrue(httpstatus_int == 200)
    
    def test_str(self):
        httpstatus_str = str(httpstatus.HTTP_200_OK)
        self.assertTrue(type(httpstatus_str) == str)
        self.assertTrue(httpstatus_str == 'HTTP 200 - OK')
    
    def test_is_informational(self):
        self.assertTrue(httpstatus.is_informational(httpstatus.HTTP_100_CONTINUE))
        self.assertTrue(httpstatus.is_informational(100))
    
    def test_is_success(self):
        self.assertTrue(httpstatus.is_success(httpstatus.HTTP_200_OK))
        self.assertTrue(httpstatus.is_success(200))
    
    def test_is_redirect(self):
        self.assertTrue(httpstatus.is_redirect(httpstatus.HTTP_300_MULTIPLE_CHOICES))
        self.assertTrue(httpstatus.is_redirect(300))
    
    def test_is_client_error(self):
        self.assertTrue(httpstatus.is_client_error(httpstatus.HTTP_400_BAD_REQUEST))
        self.assertTrue(httpstatus.is_client_error(400))
    
    def test_is_server_error(self):
        self.assertTrue(httpstatus.is_server_error(httpstatus.HTTP_500_INTERNAL_SERVER_ERROR))
        self.assertTrue(httpstatus.is_server_error(500))


if __name__ == '__main__':
    unittest.main()
