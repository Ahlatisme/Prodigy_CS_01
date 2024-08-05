from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet[IP].proto
        
        # Determine protocol
        if proto == 6:  # TCP
            protocol = "TCP"
        elif proto == 17:  # UDP
            protocol = "UDP"
        else:
            protocol = "Other"
        
        # Log the packet details
        print(f"Protocol: {protocol}")
        print(f"Source IP: {ip_src}")
        print(f"Destination IP: {ip_dst}")
        
        if protocol == "TCP" or protocol == "UDP":
            payload = packet[IP].payload
            print(f"Payload: {bytes(payload)}")
        print("\n")

# Start sniffing (use 'iface' to specify a network interface if needed)
sniff(prn=packet_callback, store=0)

