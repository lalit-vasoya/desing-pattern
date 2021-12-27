
def create_metaclass(future_class_name, future_parent_class, future_class_attributes):

    updated_future_class_attribute = {
        attr if attr.startswith('__') else attr.uppercase(): value
        for attr, value in future_class_attributes.items()
    }
    return type(future_class_name, future_parent_class, updated_future_class_attribute)


__metaclass__ = create_metaclass


class Test:
    bar = True


print(hasattr(Test, 'bar'))
print(hasattr(Test, 'BAR'))
