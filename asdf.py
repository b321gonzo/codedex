#asdf.py
class Test:
    def __init__(self, name, is_caught=False):
        self.name = name
        self.is_caught = is_caught
        
me = Test("Jerry", True)
him = Test([3, 5, 7])
print(me.is_caught)
print(him.is_caught)
