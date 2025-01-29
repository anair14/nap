from flask import Flask, render_template, request
import socket
import requests

app = Flask(__name__)

def get_network_info():
    # Get local IP address
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    
    # External IP and location details
    external_ip = requests.get('https://api.ipify.org').text
    geo_info = requests.get(f'https://ipapi.co/{external_ip}/json/').json()
    
    return {
        "hostname": hostname,
        "local_ip": local_ip,
        "external_ip": external_ip,
        "location": geo_info.get("city", "Unknown"),
        "region": geo_info.get("region", "Unknown"),
        "country": geo_info.get("country_name", "Unknown"),
        "isp": geo_info.get("org", "Unknown")
    }

@app.route("/")
def dashboard():
    network_info = get_network_info()
    return render_template("dashboard.html", network_info=network_info)

if __name__ == "__main__":
    app.run(debug=True)

