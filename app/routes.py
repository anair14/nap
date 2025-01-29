"""
Author: Ashwin Nair
Date: 2025-01-28
Project name: routes.py
Summary: Enter summary here.
"""

from flask import render_template, request, jsonify
from app import app
from app.utils import network_tools, packet_sniffer, api_integration

@app.route('/')
def dashboard():
    stats = network_tools.get_network_stats()
    return render_template('dashboard.html', stats=stats)

@app.route('/devices')
def devices():
    connected_devices = network_tools.get_connected_devices()
    return render_template('devices.html', devices=connected_devices)

@app.route('/packet-analysis')
def packet_analysis():
    packets = packet_sniffer.sniff_packets(count=10)
    return render_template('packet_analysis.html', packets=packets)

@app.route('/speed-test')
def speed_test():
    speed_data = network_tools.run_speed_test()
    return render_template('speed_test.html', speed_data=speed_data)

@app.route('/ip-reputation', methods=['POST'])
def ip_reputation():
    ip_address = request.form.get('ip_address')
    reputation = api_integration.check_ip_reputation(ip_address)
    return jsonify(reputation)
