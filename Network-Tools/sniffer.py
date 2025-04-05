import scapy.all as scapy

def sniff_packets(interface):
    print(f"Sniffing on interface {interface}...")
    scapy.sniff(iface=interface, store=False, prn=process_packet)

def process_packet(packet):
    print(packet.summary())

# Example usage
if __name__ == "__main__":
    sniff_packets("eth0")
