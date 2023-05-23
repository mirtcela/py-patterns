# todo: call factory() and return true or false
# depending on whether the factory makes a
# singleton or not
def is_singleton(factory):
    first = factory()
    second = factory()
    return first is second