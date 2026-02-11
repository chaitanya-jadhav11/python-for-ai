import  unittest
import cap

class TestCap(unittest.TestCase):
    def test_cap_text(self):
        self.assertEqual(cap.cap_text('python'), 'Python')
        self.assertEqual(cap.cap_text('PYTHON'), 'Python')
        self.assertEqual(cap.cap_text('pYtHoN'), 'Python')
        self.assertEqual(cap.cap_text('my pYtHoN'), 'My Python')
if __name__ == '__main__':
    unittest.main()
