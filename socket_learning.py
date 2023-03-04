from time import sleep as delay
import socket


def main():
    c = Server()  # client
    s = Server()  # server
    print('for start choose a mode:')
    print('1. SERVER\n2. CLIENT\n')
    a = input()
    if a == '1':
        s.get_ip()
        s.get_data()
        print()
        s.listen()
    elif a == '2':
        c.get_ip()
        print()
        c.send()


class Server:
    def __init__(self):
        self.ip = '127.0.0.1'
        self.port = 80
        self.data = b'- Data [..]'
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # tcp connection
        self.udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # udp connection

    def get_ip(self):
        self.ip = self.question('IP: ', '127.0.0.1')
        self.port = int(self.question('Port: ', '80'))

    def get_data(self):
        self.data = input('Data: ').encode()

    def listen(self):
        print('> SERVER')
        print(f'<{self.ip}:{self.port}>')
        print('Listening...')
        tcp = self.tcp
        tcp.bind((self.ip, self.port))
        tcp.listen(5)
        while True:
            client, addr = tcp.accept()
            print(f'input connection: {addr}\n{client}')
            client.send(self.data)
            client.close()

    def send(self):
        print('> CLIENT')
        print(f'<{self.ip}:{self.port}>')
        print('Sending packet...')
        tcp = self.tcp
        tcp.connect((self.ip, self.port))
        data = tcp.recv(1024)
        print(f'Data: {data}')
        input('Enter any key to EXIT.')
        tcp.close()

    @staticmethod
    def question(quest, answer):
        """make sure answer is not ''(empty str) or just ' '(spaces)"""
        print(f'Default: ({answer})')
        a = input(quest).strip()
        if a and a != answer:
            answer = a
        return answer


if __name__ == '__main__':
    main()
