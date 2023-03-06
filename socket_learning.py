import socket
import time


def main():
    s = SocketWiz()
    c = SocketWiz()
    print('1.Server\n2.Client\n')
    ans = input()
    if ans == '1':
        print('\n> SERVER\n')
        try:
            s.change_addr()
            s.server_listen()
        except BaseException as exc:
            print(f'Error! {exc}\n')
            s.change_addr()
            s.server_listen()
    elif ans == '2':
        print('\n> CLIENT\n')
        c.change_addr()
        c.client_connect()


class SocketWiz:
    def __init__(self):
        self._ip = '127.0.0.1'
        self._port = 5555

    @property
    def addr(self):
        return tuple((self._ip, self._port))

    @property
    def tcp_portal(self):
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    @property
    def udp_portal(self):
        return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    @staticmethod
    def question(quest, answer):
        """make sure answer is not ''(empty str) or just ' '(spaces)"""
        print(f'Default: ({answer})')
        a = input(quest).strip()
        if a and a != answer:
            answer = a
        return answer

    def change_addr(self):
        self._ip = self.question('IP: ', self._ip)
        self._port = int(self.question('PORT: ', self._port))

    def server_listen(self):
        print(f'binding <{self._ip}> : <{self._port}>')
        portal = self.tcp_portal
        portal.bind(self.addr)
        portal.listen(5)  # 5 connection per-time
        print('listening...')
        loop = 0  # counting inputs
        while True:
            loop += 1
            _client, _addr = portal.accept()  # if data received
            print(f'[{loop}] input connection: {_addr}\n{_client}')  # Client Address
            _client.send(b'- Data (Server>Client): [..]')  # sending data to client
            print('packet send.\n')
            _client.close()  # end of connection

    def client_connect(self):
        portal = self.tcp_portal
        portal.connect(self.addr)
        data = portal.recv(2048)
        print(f'[Data]: {data}')
        for i in range(25):
            print(f'\rexit in: {25 - i}', end='')
            time.sleep(1)
        print()
        portal.close()


if __name__ == '__main__':
    main()
