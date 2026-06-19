from core.capture import start_capture


def analyze_packet(packet):

    print(packet.summary())


if __name__ == "__main__":

    start_capture(analyze_packet)
