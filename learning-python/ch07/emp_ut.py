from unittest import TestCase
from unittest.mock import patch, call
from ut.emp import EmployeeService


class EmployeeTest(TestCase):
    @patch("ut.emp.EmployeeDAO")
    def test_emp_service(self, employee_dao_mock):
        emp = EmployeeService(employee_dao_mock)
        emp.search_by_first_name("Scott")
        self.assertEqual([call.search_by_first_name("Scott")], employee_dao_mock.method_calls)