# there are a few ways to do this

def fn_name():
    return 'brea'

class IPrintThings:
    def other_fn(self):
        print(f'I like {fn_name()}d')

class Test(IPrintThings):
    def test_fn(self):
        self.other_fn()
        globals()['fn_name'] = lambda: 'foo'
        self.other_fn()

Test().test_fn()
