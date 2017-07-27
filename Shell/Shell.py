from Tab import TabShow
from Tab import AutoSuggest

from ShellClass import TemplateShell
from prettytable import PrettyTable



class MainShell(TemplateShell):
    def __init__(self, prompt = 'Shell'):
        super(MainShell, self).__init__()
        self.prompt = prompt

    def help_menu(self):
        """ Prints a pretty help menu """
        t = PrettyTable(['command', 'description'])
        t.align = 'l'
        #general
        t.add_row(['help', 'self.help()'])
        t.add_row(['exit', 'Exists this interactive shell'])
        print(t)
        
    def loop(self):
       while self.stay:
            op, _, tail = TabShow(completer = AutoSuggest.MainCompleter(), hint = self.prompt).strip().partition(' ')

            if op == 'exit':
                print('Goodbye!')
                self.stay = False

            elif op == 'help':
                self.help_menu()
            
            elif op == '':
                continue

if __name__ == '__main__':
    shell = MainShell()
    shell.loop()