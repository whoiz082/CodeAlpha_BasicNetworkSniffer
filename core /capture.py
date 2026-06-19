from scapy.all import sniff


def start_capture(packet_callback):

    print("=" * 60)
    print(" Starting Live Packet Capture... Press Ctrl+C to stop ")
    print("=" * 60)

    sniff(
        prn=packet_callback,
        store=0
    )
