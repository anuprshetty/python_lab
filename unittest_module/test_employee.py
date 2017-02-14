import unittest
from unittest.mock import patch
from employee import Employee

# Important Points:
# - Unit tests are written to test the functionality of the code. i.e., whether our code is working as expected or not.
# - 'Unit' for Testing depends upon individual programmer.
# - 1...n functions, 1...n lines of code, 1...n objects, etc. (Capable of executing independently)
# - Unit tests are tests written for testing a unit of code.
# - One Unit Test runs independently of any other Unit Test, Code, etc.
# - External dependencies are managed with doubles (Mocks / Fakes / Stubs)
# - Each Unit Test should run within milliseconds.
# - Writing Unit Tests --> 3 Steps --> Arrange (Initializations) - Act (Call the function/code under test) - Assert (Verify the result - Whether it is expected or not) --> (AAA Model)

# Test Doubles:
# - Used in lieu of external dependencies like DB, Web, API, Library, Network, etc.
# - Easy to simulate various scenarios.
# - Some of the most widely used test doubles - Mocks, Fakes, Stubs.


class TestEmployee(unittest.TestCase):

    # For each test case, seperate instance of 'TestEmployee' class is created to run that perticular test case.

    # As 'setUpClass' and 'tearDownClass' methods not related to perticular test case, these methods are defined as 'classmethod'.
    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    # runs before each test cases
    def setUp(self):
        print("setUp")
        self.emp_1 = Employee("Ram", "Raj", 50000)
        self.emp_2 = Employee("Sham", "Lal", 45000)

    # runs after each test cases
    def tearDown(self):
        print("tearDown")

    # Test cases run parallelly (i.e., not run in order). So it's better to keep test cases isolated from one another.
    def test_email(self):
        print("test_email")
        self.assertEqual(self.emp_1.email, "Ram.Raj@gmail.com")
        self.assertEqual(self.emp_2.email, "Sham.Lal@gmail.com")

        self.emp_1.first_name = "Bob"
        self.emp_2.first_name = "Alice"

        self.assertEqual(self.emp_1.email, "Bob.Raj@gmail.com")
        self.assertEqual(self.emp_2.email, "Alice.Lal@gmail.com")

    def test_full_name(self):
        print("test_full_name")
        self.assertEqual(self.emp_1.full_name, "Ram Raj")
        self.assertEqual(self.emp_2.full_name, "Sham Lal")

        self.emp_1.first_name = "Bob"
        self.emp_2.first_name = "Alice"

        self.assertEqual(self.emp_1.full_name, "Bob Raj")
        self.assertEqual(self.emp_2.full_name, "Alice Lal")

    def test_hike_pay(self):
        print("test_hike_pay")
        self.emp_1.hike_pay()
        self.emp_2.hike_pay()

        self.assertEqual(self.emp_1.pay, 65000)
        self.assertEqual(self.emp_2.pay, 58500)

    # Mocking -> For accessing things that are out of your control.
    def test_monthly_schedule(self):
        print("test_monthly_schedule")
        with patch("employee.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.emp_1.monthly_schedule("May")
            mocked_get.assert_called_with("http://company.com/Ram_Raj/May/")
            self.assertEqual(schedule, "Success")

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule("July")
            mocked_get.assert_called_with("http://company.com/Sham_Lal/July/")
            self.assertEqual(schedule, "Bad Response!")


if __name__ == "__main__":
    unittest.main()
