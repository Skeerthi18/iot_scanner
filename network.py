import nmap

def scan_network(network_range):
    scanner = nmap.PortScanner()
    scanner.scan(hosts=network_range, arguments='-Pn -sV')

    devices = []
    for host in scanner.all_hosts():
        device_info = {
            "ip": host,
            "hostname": scanner[host].hostname(),
            "open_ports": scanner[host]['tcp'].keys() if 'tcp' in scanner[host] else []
        }
        devices.append(device_info)
    
    return devices

network_range = "192.168.1.0/24"
devices = scan_network(network_range)
for device in devices:
    print(device)
