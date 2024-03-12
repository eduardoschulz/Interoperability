import dpkt
from dpkt.utils import inet_to_str

with open('teste.pcap', 'rb') as f:
    pcap = dpkt.pcap.Reader(f)
    for t, buf in pcap:
        eth = dpkt.ethernet.Ethernet(buf)
        if not isinstance(eth.data, dpkt.ip.IP):
            print('Non IP Packet type not supported %s\n' % eth.data.__class__.__name__)
            continue
        ip = eth.data
        if not isinstance(ip.data, dpkt.sctp.SCTP):
            print('Non SCTP Packet type not supported %s\n' % eth.data.__class__.__name__)
            continue
        sctp = ip.data
        print(t, ",", inet_to_str(ip.src), ":", sctp.sport, sep='')
