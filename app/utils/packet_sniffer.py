"""
Author: Ashwin Nair
Date: 2025-01-28
Project name: packet_sniffer.py
Summary: Enter summary here.
"""
from scapy.all import sniff

def packet_callback(packet):
    return packet.summary()


def sniff_packets(count=10):
    packets = sniff(count=count)
    return [packet_callback(packet) for packet in packets]
