
# Simple network sniffer to capture and display IP packets with protocol info

from scapy.all import sniff, IP, TCP, UDP
from datetime import datetime

packet_count = 0

def packet_callback(packet):
    global packet_count
    packet_count += 1

    if IP in packet:
        time_stamp = datetime.now().strftime("%H:%M:%S")
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"
        else:
            protocol = "Other"

        # Print captured packet details
        print(f"[{packet_count}] {time_stamp} | {protocol:<5} | {src_ip} → {dst_ip}")

        # Show progress every 5 packets
        if packet_count % 5 == 0:
            print(f"💡 {packet_count} packets captured so far...\n")

print("Network Sniffer Started. Press Ctrl + C to stop capturing packets.\n")

# Start sniffing packets (store=False avoids storing in memory)
sniff(prn=packet_callback, store=False)
