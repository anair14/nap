"""
Author: Ashwin Nair
Date: 2025-01-28
Project name: network_tools.py
Summary: Enter summary here.
"""
import psutil
import speedtest
import socket

def get_network_stats():
    stats = {
        'bytes_sent': psutil.net_io_counters().bytes_sent,
        'bytes_recv': psutil.net_io_counters().bytes_recv,
        'connections': len(psutil.net_connections()),
    }
    return stats


def get_connected_devices():
    devices = []
    for nic, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET:
                devices.append({
                    "device_name": nic,
                    "ip": addr.address,
                    "mac": addr.netmask or "N/A"
                })
    return devices


def run_speed_test():
    st = speedtest.Speedtest()
    st.get_best_server()
    st.download()
    st.upload()
    return {
        "download_speed": st.results.download / 1_000_000,
        "upload_speed": st.results.upload / 1_000_000,
        "ping": st.results.ping
    }
