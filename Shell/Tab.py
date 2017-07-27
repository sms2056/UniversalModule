#Get System User
from getpass import getuser as GetSystemName
UserName = GetSystemName()
#import prompt
from prompt_toolkit import prompt
#In Memory History
from prompt_toolkit.history import InMemoryHistory
#Auto Suggest From History
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.contrib.completers import WordCompleter
#font style
from prompt_toolkit.token import Token
from prompt_toolkit.styles import style_from_dict
#Hot Key Lib
from prompt_toolkit.key_binding.manager import KeyBindingManager
from prompt_toolkit.keys import Keys

##########################################################
#            Set Auto Suggest From History               #
##########################################################
class AutoSuggest():
    tab_general = ['help', 'cls', 'exit']

    @classmethod
    def DefineCompleter(self):
        tab_define = ['<html>', '<body>', '<head>', '<title>']
        return WordCompleter(tab_define, ignore_case=True)

    @classmethod
    def MainCompleter(self):
        tab_main = ['exploit', 'auxiliary']
        tab_main = tab_main + AutoSuggest.tab_general
        return WordCompleter(tab_main, ignore_case = True)

    @classmethod
    def ExploitCompleter(self):
        tab_exploit = ['back']
        tab_exploit = tab_exploit + AutoSuggest.tab_general
        return WordCompleter(tab_exploit, ignore_case = True)

# end Set Auto Suggest From History
##########################################################



############################################################
#                    Set Hot Key                           #
############################################################
# init hot key manager
hotkey_manager = KeyBindingManager.for_prompt()
# Set Control + Z
@hotkey_manager.registry.add_binding(Keys.ControlZ)
def _(event):
    def bye():
        print('bye-bye')
    event.cli.run_in_terminal(bye)
    exit()
# Set Control + Z
@hotkey_manager.registry.add_binding(Keys.ControlC)
def _(event):
    pass
# end Set Key Hot 
#############################################################

# Prompt_tokens Class:Set prompt style
class Prompt_tokens():
    def __init__(self, name = UserName, at = '[*]', appname = 'xXx', prompt = 'Shell', toolbar_str = ' hello! Welcome! This is xXx TOoL. '):
        self.name = name
        self.at = at
        self.appname = appname
        self.prompt = prompt
        self.toolbar_str = toolbar_str

    def shellstyle_default(self):
        color_gray = '#C0C0C0'
        color_red = '#FF0000'
        
        if self.prompt.lower() in ['shell', '>>']:
            tokenpath_color = color_gray
        else:
            tokenpath_color = color_red
        
        shellstyle_default = style_from_dict({
                                                #toolbar inforation
                                                Token.Toolbar: '#ffffff bg:#333333',
                                                # User input.
                                                Token:          '#ff0066',
                                                # Prompt.
                                                #Token.Username: '#884444 bg:#aaaaff',
                                                Token.Username: '#884444',
                                                Token.At:       '#00aa00',
                                                Token.Colon:    '#00aa00',
                                                Token.Pound:    '#00aa00',
                                                Token.Appname:  '#000088',
                                                Token.Path:     tokenpath_color,
                                            })
        return shellstyle_default

    # Set toolbar
    def get_bottom_toolbar_tokens(self, cli):
        return [(Token.Toolbar, self.toolbar_str)]


    def get_prompt_tokens(self, cli):
        return [
                (Token.Username, self.name),
                (Token.At,       self.at),
                (Token.Appname,  self.appname),
                (Token.Colon,    ':'),
                (Token.Path,     self.prompt),
                (Token.Pound,    '# '),
                ]
# end Prompt_tokens Class

# Set History In Memory 
history = InMemoryHistory()
# end Set History In Memory 

# define TabShow Function
def TabShow(completer = AutoSuggest.DefineCompleter(), hint = '>>'):
    PromptTokens = Prompt_tokens(prompt = hint)
    user_input = prompt(  
                        get_prompt_tokens = PromptTokens.get_prompt_tokens,
                        history = history, 
                        completer = completer, 
                        auto_suggest = AutoSuggestFromHistory(),
                        get_bottom_toolbar_tokens = PromptTokens.get_bottom_toolbar_tokens,
                        style = PromptTokens.shellstyle_default(),
                        key_bindings_registry=hotkey_manager.registry
                        )
    return user_input
# end define TabShow Function

if __name__ == '__main__':
    while True:
        text = TabShow(hint = 'Exploit', completer = AutoSuggest.ExploitCompleter())
        print('You said: %s' % text)