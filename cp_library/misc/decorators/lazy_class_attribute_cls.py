import cp_library.misc.decorators.__header__

class lazy_class_attribute:
    def __init__(self, fn):
        self.fn = fn
        self.value = None
    
    def __get__(self, instance, owner):
        if self.value is None:
            # Call with owner (the class) as the first argument
            self.value = self.fn(owner)
        return self.value