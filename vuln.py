import nmap

def check_vulnerabilities(device):
    # Ensure device is a dictionary
    if isinstance(device, str):
        return []  # If it's a string, return an empty list (No vulnerabilities)

    ip = device.get("IP", None)
    if not ip:
        return []  # If no IP found, return an empty list

    # Simulate vulnerability check (Replace with real check)
    vulnerabilities = []
    if ip.endswith(".10"):  # Example: Assume ".10" IPs are vulnerable
        vulnerabilities.append("Default Credential")
    
    return vulnerabilities
