

class MemberTable(dict):
    """ Override the behaviour of dictionary object """

    def __init__(self):
        """" add member name dictionary """
        print('MemberTable call the __init__ method')
        self.member_names = []

    def __setitem__(self, key, value):
        """" Assign the key in member_names """
        print('MemberTable call the __setattr__ method', key)
        if key not in self:
            self.member_names.append(key)

        dict.__setitem__(self, key, value)


# metaclass
class OrderClass(type):
    """" Define the metaclass """

    @classmethod
    def __prepare__(metacls, name, bases):
        print('MetaClass call __prepare__')
        return MemberTable()

    def __new__(cls, name, base, classdict):
        print('MetaClass call __new__')
        result = type.__new__(cls, name, base, dict(classdict))
        # result.member_names = classdict.member_names
        return result


class MyClass(metaclass=OrderClass):

    def __new__(cls, *args, **kwargs):
        print('MyClass call __new__')
        return super(MyClass, cls).__new__(cls, *args, **kwargs)

    def __init__(self):
        print('MyClass call __init__')

    # method1 goes in array element 0
    def method1(self):
        pass

    # method2 goes in array element 1
    def method2(self):
        pass


if __name__ == '__main__':
    obj = MyClass()


# Output
# MetaClass call __prepare__
# MemberTable call the __init__ method
# MemberTable call the __setattr__ method __module__
# MemberTable call the __setattr__ method __qualname__
# MemberTable call the __setattr__ method __new__
# MemberTable call the __setattr__ method __init__
# MemberTable call the __setattr__ method method1
# MemberTable call the __setattr__ method method2
# MemberTable call the __setattr__ method __classcell__
# MetaClass call __new__
# MyClass call __new__
# MyClass call __init__
