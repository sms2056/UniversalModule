from plugins.BaseClass import BaseClass

class SubClass_2(BaseClass):
    def __init__(self):
        self.name = 'SubClass_2'
        self.result_list = []

    def Analysis(self):
        print('SubClass_2')

    def on_call(self):
        return self.Analysis()


if __name__ == '__main__':
    x = SubClass_2()
    x.on_call()