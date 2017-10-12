import json
def div(a, b):
    try:
        print("calculating {}/{}: ".format(a, b))
        result = a / b
    except ZeroDivisionError as ex:
        print(ex)
    else:
        print("result is: {}".format(result))
    finally:
        print("Finally")


div(10, 5)

div(20, 0)


def parse_emp_json(json_data):
    try:
        return json.loads(json_data)
    except (ValueError, TypeError) as ex:
        print(type(ex), ex)

json_str = '{"id": 1, "first_name":"Scott"}'
emp1 = parse_emp_json(json_str)
emp2 = parse_emp_json("{{")
emp3 = parse_emp_json(2)

class CustomeException(Exception):
    pass

raise CustomeException