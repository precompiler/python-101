class Employee:
    def __init__(self, first_name, last_name, email):
        self._first_name = first_name
        self._last_name = last_name
        self._email = email

    def __str__(self):
        return '{"first_name":"' + self._first_name + '",' \
               ' "last_name":"' + self._last_name + '",' \
               ' "email":"' + self._email + '"}'
    @property
    def get_first_name(self):
        return self._first_name

    @property
    def get_last_name(self):
        return self._last_name

    @property
    def get_email(self):
        return self._email


class EmployeeDAO:
    def search_by_first_name(self, first_name):
        pass


class EmployeeService:
    def __init__(self, employee_dao):
        self._employee_dao = employee_dao

    def search_by_first_name(self, first_name):
        self._employee_dao.search_by_first_name(first_name)
