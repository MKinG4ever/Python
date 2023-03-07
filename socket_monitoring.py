from threading import Thread
import socket


class SocketTool:
    def __init__(self, ip, port):
        self._ip = ip
        self._port = port

    @property
    def addr(self):
        return self._ip, self._port

    @property
    def tcp_portal(self):
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    @property
    def udp_portal(self):
        return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def portal_listen(self):
        portal = self.tcp_portal
        portal.bind(self.addr)
        portal.listen(9)
        loop = 0
        print(self._port, end='|')
        while True:
            loop += 1
            _client, _addr = portal.accept()  # if data received
            _log = f'[{loop}] input connection: {_addr} -> {self.addr}'
            with open('Log.txt', 'a') as f:
                f.write(_log + '\n')
            print(_log)  # Client Address
            _client.close()

    def ports(self):
        # monitor first 1000 ports
        t = []
        for i in range(1000):
            try:
                t.append(Thread(target=SocketTool(self._ip, i).portal_listen))
            except BaseException as exc:
                print(f'Error! {exc}\n')
        for m in t:
            m.start()
        for n in t:
            n.join()
