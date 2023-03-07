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
        t = [Thread(target=SocketTool(self._ip, _).portal_listen) for _ in range(1, 1000)]
        for m in t:
            m.start()
        for n in t:
            n.join()
