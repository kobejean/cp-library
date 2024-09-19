import cp_library.io.__init__

class Parsable:
    @classmethod
    def parse(cls, parse_spec):
        return parse_spec(lambda s: cls(s))