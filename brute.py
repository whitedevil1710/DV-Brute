import atexit
from itertools import zip_longest
import readline
import requests
import cmd
import sys
import os
from termcolor import colored
import subprocess



class Mycmd(cmd.Cmd):
    prompt = colored(">>>>", "green")

    def __init__(self):
        super().__init__()
        self.possible_pass=[]
        self.possible_user=[]
        self.user = []
        self.pswd = []
        self.url = ""
        self.user_param = ""
        self.pass_param = ""
        self.pass_file = ""
        self.user_file = ""
        self.success_status_codes = [200, 301 ,302]

    
    def banner(self):
        print(colored("""
██████╗ ██╗   ██╗      ██████╗ ██████╗ ██╗   ██╗████████╗███████╗
██╔══██╗██║   ██║      ██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝
██║  ██║██║   ██║█████╗██████╔╝██████╔╝██║   ██║   ██║   █████╗  
██║  ██║╚██╗ ██╔╝╚════╝██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  
██████╔╝ ╚████╔╝       ██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗
╚═════╝   ╚═══╝        ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝
-------------------c̶o̶d̶e̶d̶ b̶y̶ w̶h̶i̶t̶e̶d̶e̶v̶i̶l̶---------------------------
        ""","cyan"))

    def help_set_pass(self):
        print("Help for set_pass command:")
        print("Usage: set_pass <password filename>")
        print("Description: Set the password file.")

    def help_restart(self):
        print("Help for restart command:")
        print("No arguments.")
        print("Description: Restart the script.")

    def help_set_url(self):
        print("Help for set_url command:")
        print("Usage: set_url <url>")
        print("Description: Set the target URL.")

    def help_count_pass(self):
        print("Help for count_pass command:")
        print("No arguments.")
        print("Description: Count the number of passwords loaded.")

    def help_quit(self):
        print("Help for quit command:")
        print("No arguments.")
        print("Description: Quit the script.")

    def help_print_users(self):
        print("Help for print_users command:")
        print("No arguments.")
        print("Description: Print the loaded usernames.")

    def help_set_user(self):
        print("Help for set_user command:")
        print("Usage: set_user <username or filename>")
        print("Description: Set the username or load usernames from a file.")

    def help_set_param_user(self):
        print("Help for set_param_user command:")
        print("Usage: set_param_user <post parameter>")
        print("Description: Set the parameter for the username in POST requests.")

    def help_set_param_pass(self):
        print("Help for set_param_pass command:")
        print("Usage: set_param_pass <password parameter>")
        print("Description: Set the parameter for the password in POST requests.")

    def help_options(self):
        print("Help for options command:")
        print("No arguments.")
        print("Description: Display the current configuration options.")

    def help_scan(self):
        print("Help for scan command:")
        print("No arguments.")
        print("Description: Perform a login scan using the configured options.")

    def help_add_pass(self):
        print("Help for add_pass command:")
        print("Usage: add_pass <password>")
        print("Description: Add a password to the loaded password list.")

    def help_clear_pass(self):
        print("Help for clear_pass command:")
        print("No arguments.")
        print("Description: Clear the loaded password list.")

    def help_clear_user(self):
        print("Help for clear_user command:")
        print("No arguments.")
        print("Description: Clear the loaded username list.")

    def help_cls(self):
        print("Help for cls command:")
        print("No arguments.")
        print("Description: Clear all the configuration options and loaded data.")

    def help_exit(self):
        print("Help for exit command:")
        print("No arguments.")
        print("Description: Exit the script.")

    def emptyline(self):
            pass

    def save_history(self):
        history_file = os.path.expanduser(".mycmd_history")
        readline.write_history_file(history_file)
        readline.clear_history()
        readline.set_history_length(1000)

    def preloop(self):
        history_file = os.path.expanduser(".mycmd_history")
        if os.path.exists(history_file):
            readline.read_history_file(history_file)

    def postloop(self):
        atexit.register(self.save_history)

    def do_restart(self,args):
        subprocess.run("clear",shell=True)
        python = sys.executable
        exec(open(sys.argv[0]).read())
   
    def do_history(self, args):
        with open(".mycmd_history", 'r') as f:
            max_line_number_width = len(str(sum(1 for _ in f)))

        with open(".mycmd_history", 'r') as f:
            for line_number, line in enumerate(f, start=1):
                formatted_line_number = f"{line_number: <{max_line_number_width}}"
                print(f"{formatted_line_number} {line.rstrip()}")

    def do_clear_history(self,args):
        with open(".mycmd_history", 'w') as f:
            f.truncate(0)
        print("Command history cleared.")
   
    def do_set_pass(self, line):
        if not line:
            print(colored("[!] Error: No argument provided. Usage: set_pass <password filename>", "red"))
            return
        self.pass_file = line
        filename = line.strip()
        try:
            with open(filename, "r") as f:
                print(colored(f"[+] Reading file: {filename}", "green"))
                lines = [line.rstrip('\n') for line in f]
                self.pswd.extend(lines)
        except FileNotFoundError:
            print(colored(f"[!] Error: {filename} doesn't exist", "red"))

    def do_set_url(self, line):
        if not line:
            print(colored("[!] Error: URL not set. \n Usage set_url <url>", "red"))
            return
        else:
            try:
                url = line.strip()
                response = requests.get(url).status_code
                if response != 404:
                    self.url = url
                    print(colored(f"[+] URL set to {self.url}", "green"))
            except requests.RequestException:
                print(colored("[!] Error: URL not found", "red"))
    
    def do_count_pass(self, args):
        count = len(self.pswd)
        print(colored(f"[+] Total number of passwords: {count}", "green"))

    def possibilit(self):
        u=len(self.user)
        p=len(self.pswd)
        return u*p

    def do_quit(self, args):
        Mycmd.exit()
        sys.exit(1)

    def do_print_users(self, args):
        print(colored("USERNAMES", "green"))
        print("=" * 50)
        print("\n".join(self.user))

    def do_set_user(self, line):
        if not line:
            print(colored("[!] Error: No argument provided. \nUsage: set_user <username or filename>", "red"))
            return
        self.user_file = line
        parameter = line.strip()
        if os.path.isfile(parameter):
            try:
                with open(parameter, "r") as f:
                    print(colored(f"[+] Reading file: {parameter}", "green"))
                    lines = [line.rstrip('\n') for line in f]
                    self.user.extend(lines)
            except FileNotFoundError:
                print(colored(f"[!] Error: {parameter} doesn't exist", "red"))
        else:
            self.user.append(parameter)
            print(colored(f"[+] Adding username: {parameter}", "green"))

    def do_set_param_user(self, line):
        if not line:
            print(colored("[!] Error: User parameter not found. \nUsage: set_param_user <post parameter>", "red"))
        else:
            param = line.strip()
            self.user_param = param
            print(colored(f"[+] Username Parameter set to: {param}", "green"))

    def do_set_param_pass(self, line):
        if not line:
            print(colored("[!] Error: Password parameter not found. \nUsage: set_param_pass <password parameter>", "red"))
        else:
            param = line.strip()
            self.pass_param = param
            print(colored(f"[+] Password Parameter set to: {param}", "green"))

    def do_options(self, args):
        user = "none"
        if os.path.isfile(self.user_file):
            user = self.user_file
        else:
            user = ", ".join(self.user)
        print(colored("OPTIONS", "yellow"))
        print("=" * 50)
        print(colored(f"""All parameters are required to run the script.
URL                 : {self.url}
Username            : {user}
Password            : {self.pass_file}
User Parameter      : {self.user_param}
Password Parameter  : {self.pass_param}
""", "yellow"))

    def complete_set_user(self, text, line, begidx, endidx):
        current_dir = os.getcwd()
        files = [f for f in os.listdir(current_dir) if os.path.isfile(os.path.join(current_dir, f))]
        return [f for f in files if f.startswith(text)]

    def content_length(self, res):
        try:
            response = res
            return len(response.text)
        except Exception as e:
            return f"[!] Error: str {e}"

    def do_scan(self, args):
        if not self.user_param or not self.pass_param or not self.url:
            print(colored("[!] Error: Username parameter, Password parameter, or URL not set", "red"))
            return
        if not self.user:
            print(colored("[!] Error: Username not found", "red"))
            return
        if not self.pswd:
            print(colored("[!] Error: Passwords not found", "red"))
            return
        if not self.pass_file:
            print(colored("[!] Error: Password file not set", "red"))
            return
        success = False
        data = {self.user_param: "", self.pass_param: ""}
        #print(data)
        prv = requests.post(self.url, data=data)
        prvresp = self.content_length(prv)
        #print(prvresp)
        print(colored(f"Total possiblities : {self.possibilit()}","cyan"))
        try:
            for i in self.user:
                for j in self.pswd:
                    data = {self.user_param: i, self.pass_param: j}
                    res = requests.post(self.url, data=data)
                    status = res.status_code
                    crresp=self.content_length(res)
                    #print("Status Code: "+str(status))
                    #print("Curret Response:"+ str(crresp))
                    if status in self.success_status_codes and prvresp != crresp:
                        self.possible_user.append(i)
                        self.possible_pass.append(j)    
                        success = True
                        #return
                    else:
                        print(colored(f"[-] Trying: Username: {str(i)} Password: {str(j)}", "red"))
            print(colored("\n [+] Possible Username and Password","green"))
            print("="*50)
            self.print_possible_password()
        except KeyboardInterrupt:
            return "\n"
        if not success:
            print(colored("[!] Password not found", "yellow"))

    def print_possible_password(self):
        for i, j in zip(self.possible_pass, self.possible_user):
            print(colored(f"{j} : {i}", "green"))

    def complete_set_pass(self, text, line, begidx, endidx):
        current_dir = os.getcwd()
        files = [f for f in os.listdir(current_dir) if os.path.isfile(os.path.join(current_dir, f))]
        return [f for f in files if f.startswith(text)]

    def do_add_pass(self, line):
        pas = line
        self.pswd.append(pas)
        if pas not in self.pswd:
            print(colored(f"[+] Password {pas} is added", "green"))
        else:
            print(colored("[-] Password already exist"))

    def do_clear_pass(self,args):
        self.pswd=[]

    def do_clear_user(self,args):
        self.user=[]

    def do_cls(self, args):
        self.user = []
        self.pswd = []
        self.url = ""
        self.user_param = ""
        self.pass_param = ""
        self.pass_file = "none"
        self.user_file = "none"
        self.result = []
        print(colored("[+] Clearing: Username, Password, URL, Parameters, Filenames", "green"))

    def default(self, line):
        try:
            subprocess.run(line, shell=True, check=True)
            if line == "clear":
                self.banner()
            elif line == "exit":
                Mycmd.exit()
                sys.exit(1)
            if line == "run":
                self.do_scan()
            self
        except FileNotFoundError:
            print(colored(f"Command not found: {line}", "red"))
        except KeyboardInterrupt:
            print(colored("\n[!] Execution interrupted by the user", "red"))
        except Exception as e:
            print(colored(f"Error: {str(e)}", "red"))

    def exit():
        print(colored("Thank you for using.\nHoping it was a great experience. If any bugs or fixes, please do a pull request on Github.\n\nGithub: https://github.com/whitedevil1710/DV-Brute", "red"))
        sys.exit(1)

if __name__ == '__main__':
    try:
        Mycmd().banner()
        Mycmd().cmdloop()
    except KeyboardInterrupt:
        print(colored("\n[!] User Interrupted","red"))
        sys.exit(1)
