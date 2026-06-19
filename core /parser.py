from scapy.layers.inet import IP, TCP, UDP, ICMP


def parse_packet(packet):

    packet_info = {}

    if packet.haslayer(IP):

        ip_layer = packet[IP]

        packet_info["source_ip"] = ip_layer.src
        packet_info["destination_ip"] = ip_layer.dst
        packet_info["packet_size"] = len(packet)


        # TCP Analysis
        if packet.haslayer(TCP):

            tcp_layer = packet[TCP]

            packet_info["protocol"] = "TCP"
            packet_info["source_port"] = tcp_layer.sport
            packet_info["destination_port"] = tcp_layer.dport


        # UDP Analysis
        elif packet.haslayer(UDP):

            udp_layer = packet[UDP]

            packet_info["protocol"] = "UDP"
            packet_info["source_port"] = udp_layer.sport
            packet_info["destination_port"] = udp_layer.dport


        # ICMP Analysis
        elif packet.haslayer(ICMP):

            packet_info["protocol"] = "ICMP"


        else:

            packet_info["protocol"] = "Other"


    return packet_info
