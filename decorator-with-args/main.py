
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged = False


def auth_decorator(function):
    def wrapper(*args):
        if args[0].is_logged:
            function(args[0])

    return wrapper


@auth_decorator
def access(user):
    print(f"Username {user.name} can access")


xavi = User("xavi")
xavi.is_logged = True
access(xavi)
