import unittest
import requests
import hr2request
class TestMyProgram(unittest.TestCase):
    def test_url(self):
        headers = {
            'User-Agent': 'Mobile'
        }
        url2 = 'http://httpbin.org/headers'
        rh = requests.get(url2, headers=headers)
        self.assertEqual(rh.url,  url2)

if __name__ == '++main__':
    unittest.main()