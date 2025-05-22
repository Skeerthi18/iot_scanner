import nmap
import requests
import ipaddress
import socket
import subprocess

def get_ip_class(ip):
    """Determine the class of an IP address."""
    first_octet = int(ip.split('.')[0])

    if 1 <= first_octet <= 126:
        return "Class A"
    elif 128 <= first_octet <= 191:
        return "Class B"
    elif 192 <= first_octet <= 223:
        return "Class C"
    elif 224 <= first_octet <= 239:
        return "Class D (Multicast)"
    elif 240 <= first_octet <= 255:
        return "Class E (Experimental)"
    else:
        return "Unknown"

def get_ip_location(ip):
    """Fetch IP location using ipinfo.io API."""
    try:
        response = requests.get(f"http://ipinfo.io/{ip}/json", timeout=5)
        data = response.json()
        return {
            "City": data.get("city", "Unknown"),
            "Region": data.get("region", "Unknown"),
            "Country": data.get("country", "Unknown"),
            "Coordinates": data.get("loc", "Unknown")
        }
    except Exception as e:
        print(f"⚠️ Error fetching IP location: {e}")
        return {
            "City": "Unknown",
            "Region": "Unknown",
            "Country": "Unknown",
            "Coordinates": "Unknown"
        }

def get_mac_address(ip):
    """Retrieve the MAC address of a device on the local network using ARP."""
    try:
        result = subprocess.run(["arp", "-n", ip], capture_output=True, text=True)
        lines = result.stdout.split('\n')
        for line in lines:
            if ip in line:
                return line.split()[2]  # Extract MAC address
    except Exception as e:
        print(f"⚠️ Error fetching MAC address: {e}")
    return "Unknown MAC"

def get_hostname(ip):
    """Resolve the hostname for an IP address."""
    try:
        return socket.gethostbyaddr(ip)[0]
    except (socket.herror, socket.gaierror):
        return "Unknown Device"

def scan_network(ip_range):
    """Perform a network scan using Nmap on any IP or range."""
    nm = nmap.PortScanner()
    devices = []

    try:
        print(f"🔎 Scanning network: {ip_range} ...")
        nm.scan(hosts=ip_range, arguments='-A -sV -Pn', sudo=True)

        for host in nm.all_hosts():
            device_name = get_hostname(host)
            mac = get_mac_address(host) if ipaddress.ip_address(host).is_private else "N/A"
            os = nm[host]['osmatch'][0]['name'] if 'osmatch' in nm[host] else "Unknown OS"
            
            # Fetch location
            location = get_ip_location(host)

            # Get IP Class
            ip_class = get_ip_class(host)

            # Find Open Ports & Services
            open_ports = []
            services = []
            for proto in nm[host].all_protocols():
                for port in nm[host][proto]:
                    open_ports.append(port)
                    services.append(f"{port}/{nm[host][proto][port]['name']}")

            devices.append({
                "IP": host,
                "Class": ip_class,
                "Device Name": device_name,
                "MAC": mac,
                "OS": os,
                "City": location["City"],
                "Region": location["Region"],
                "Country": location["Country"],
                "Coordinates": location["Coordinates"],
                "Open Ports": open_ports,
                "Services": ", ".join(services)
            })

        return devices

    except Exception as e:
        print(f"⚠️ Nmap scan failed: {str(e)}")
        return []

if __name__ == "__main__":
    ip_range = input("Enter an IP address or range to scan: ")
    results = scan_network(ip_range)

    print("\n🔍 Discovered Devices:")
    for device in results:
        print(f"""
        📡 IP: {device["IP"]} ({device["Class"]})
        💻 Device Name: {device["Device Name"]}
        🌍 Location: {device["City"]}, {device["Region"]}, {device["Country"]}
        📍 Coordinates: {device["Coordinates"]}
        🔍 MAC: {device["MAC"]}
        🖥️ OS: {device["OS"]}
        🚪 Open Ports: {", ".join(map(str, device["Open Ports"]))}
        🛠️ Services: {device["Services"]}
        -------------------------------------
        """)
