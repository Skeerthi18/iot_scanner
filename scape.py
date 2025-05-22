from scapy.all import sniff

def packet_callback(packet):
    if packet.haslayer("IP"):
        print(f"Packet: {packet.summary()}")

sniff(prn=packet_callback, count=10)
