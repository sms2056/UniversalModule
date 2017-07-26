from plugins.BaseClass import BaseClass

class SubClass_1(BaseClass):
    def __init__(self):
        self.name = 'SubClass_1'
        self.result_list = []

    def Analysis(self):
        print('SubClass_1')

    def on_call(self):
        return self.Analysis()


if __name__ == '__main__':
    x = SubClass_1()
    x.on_call()