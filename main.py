from core.capture import start_capture
from core.parser import parse_packet



def analyze_packet(packet):

    data = parse_packet(packet)

    if data:

        print("\n--- Packet Information ---")

        for key, value in data.items():

            print(f"{key}: {value}")



if __name__ == "__main__":

    start_capture(analyze_packet)
