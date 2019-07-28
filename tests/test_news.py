import unittest
from app.models import News






class NewsTest (unittest.TestCase):

    def setUp(self):
        self.new_news= (1234,"Martin Young","Bitcoin Looks Bearish as Analysts Eye A Drop to Mid-$8,000","A big move was expected for bitcoin price and it came yesterday with a swift plunge back into four figures. The move resulted in a $15 billion dump from crypto market capitalization as altcoins blindly bled out in the shadow of their big brother. Bitcoin Does…", "https://bitcoinist.com/bitcoin-looks-bearish-as-analysts-eye-a-drop-to-mid-8000/",
 "https://bitcoinist.com/wp-content/uploads/2019/07/28-July-1-e1564304495292-1920x1200.jpg","2019-07-28T09:03:16Z", "A big move was expected for bitcoin price and it came yesterday with a swift plunge back into four figures. The move resulted in a $15 billion dump from crypto market capitalization as altcoins blindly bled out in the shadow of their big brother.\r\nBitcoin Doe… [+3116 chars]")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()

