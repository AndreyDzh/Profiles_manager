import unittest
from src.models.profiles import Profile

class TestProfilesFunctions(unittest.TestCase):

    def setUp(self):
        self.profile = Profile("TestName", "IP:PORT", "Homepage.com")

    def test_to_dict(self):
        result = self.profile.to_dict()
        self.assertEqual(result, {
            "name": "TestName", 
            "proxy": "IP:PORT",
            "homepage": "Homepage.com"
        })
    
    def test_from_dict(self):
        result = Profile.from_dict({
            "name": "TestName", 
            "proxy": "IP:PORT",
            "homepage": "Homepage.com"
        })
        self.assertEqual(result, self.profile)
    
    def test_change_proxy(self):
        self.profile.change_proxy("New proxy")
        result = self.profile.proxy
        self.assertEqual(result, "New proxy")
