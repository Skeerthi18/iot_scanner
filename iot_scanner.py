import nmap

def scan_network(target_ip):
    nm = nmap.PortScanner()
    nm.scan(hosts=target_ip, arguments="-sn")  # Ping scan to detect active devices
    
    devices = []
    for host in nm.all_hosts():
        devices.append({
            'IP': host,
            'Status': nm[host].state()
        })
    
    return devices
