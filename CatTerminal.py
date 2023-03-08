import cmd

class MyTerminal(cmd.Cmd):
    intro = "Welcome to CatTerminal! Type 'help' to see the available commands."
    prompt = "> "
    
    def do_hello(self, arg):
        print("Hello, world!")
        
    def do_exit(self, arg):
        print("Пока")
        return True

if __name__ == '__main__':
    MyTerminal().cmdloop()
