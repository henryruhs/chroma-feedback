import os
import socket
from typing import List

from chroma_feedback import helper


def discover_ips(host : str, port : int, search_target : str = 'ssdp:all') -> List[str]:
	ips = []
	message =\
	[
		'M-SEARCH * HTTP/1.1',
		'MAN: "ssdp:discover"',
		'ST: ' + search_target
	]

	discovery = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
	discovery.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	discovery.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 1)
	discovery.settimeout(2)
	discovery.sendto(os.linesep.join(message).encode(), (host, port))

	while True:
		try:
			ips.append(discovery.recvfrom(65507)[1][0])
		except socket.timeout:
			break
	return helper.remove_duplicate(ips)
