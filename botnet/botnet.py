import paramiko
import time

class Client:
    def __init__(self,host,user,password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.getSSHSession()


    def getSSHSession(self):
        # Set up SSH
        sshSession = paramiko.SSHClient()
        sshSession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        while True:
            try:
                sshSession.connect(hostname=self.host, username=self.user, password=self.password)
                break
            except Exception as e:
                print(e)
                time.sleep(5)

        return sshSession


    def send_command(self,cmd):
        try:
            stdin, stdout, stderr = self.session.exec_command(cmd)
            # Wait for command to finish (may take a while for long commands)
            while not stdout.channel.exit_status_ready() or not stderr.channel.exit_status_ready():
                time.sleep(1)
        except Exception as e:
            print(e)
            return None
        else:
            # exec_command() completed successfully
            # Check if command printed anything to stderr
            err = stderr.readlines()
            err = ''.join(err)  # Convert to single string
            if err:
                print(err)
            # Check if command printed anything to stdout
            out = stdout.readlines()
            out = ''.join(out)  # Convert to single string
            if out:
                print(out)
        return (out, err)


def botNetCommand(command):
    for client in botNet:
        out, err = client.send_command(command)
        print('[*] Output from ' + client.host)
        print('[+] ' + out)


def addClient(host,user,password):
    client = Client(host,user,password)
    botNet.append(client)


botNet=[]


if __name__ == '__main__':
    addClient('', '', '')
    botNetCommand('uname -a')
