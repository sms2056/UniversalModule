from plugins.BaseClass import BaseClass

class SubClass_3(BaseClass):
    def __init__(self):
        self.name = 'SubClass_3'
        self.result_list = []

    def Analysis(self):
        print('SubClass_3')

    def on_call(self):
        return self.Analysis()


if __name__ == '__main__':
    x = SubClass_3()
    x.on_call()