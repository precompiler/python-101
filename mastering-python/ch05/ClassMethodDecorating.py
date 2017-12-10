import functools


def Transactional(function):
    @functools.wraps(function)
    def _Transactional(self, *args, **kwargs):
        print("Start transaction...")
        function(self, *args, **kwargs)
        print("Commit transaction...")
    return _Transactional

class SqlUtils:
    @Transactional
    def executeSql(self, sql):
        print("Executing {}".format(sql))

sqlUtils = SqlUtils()
sqlUtils.executeSql("INSERT INTO emp SELECT * FROM emp")
