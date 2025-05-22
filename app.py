import streamlit as st
import time
from scanner import scan_network
from vuln import check_vulnerabilities

# Set Streamlit Page Config
st.set_page_config(page_title="IoT Security Scanner", page_icon="🛡️", layout="wide")

# Custom CSS for a Dark Hacker Theme
st.markdown("""
    <style>
        body { background-color: #0D0D0D; color: white; font-family: 'Courier New', monospace; }
        .reportview-container { background: #0D0D0D; }
        h1 { color: #00FF00; text-align: center; text-shadow: 2px 2px 5px #00FF00; }
        .stButton>button { background-color: #FF0000; color: white; font-size: 18px; }
        .stDataFrame { border: 2px solid #00FF00; }
        .secure { color: #00FF00; font-weight: bold; }
        .vulnerable { color: #FF0000; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# Title with Cybersecurity Theme
st.markdown("<h1>🛡️ IoT Security Vulnerability Scanner</h1>", unsafe_allow_html=True)
st.write("### Scan your network for connected IoT devices and identify vulnerabilities.")

# Input Field for IP Range
ip_range = st.text_input("Enter IP Address or Range:")

# Button to Start Scanning
if st.button("🔍 Start Scanning", use_container_width=True):
    if not ip_range:
        st.warning("⚠️ Please enter a valid IP address or range.")
    else:
        st.write("⏳ **Scanning for IoT devices... Please wait!**")
        
        # Simulate Loading Effect
        with st.spinner("Scanning Network..."):
            time.sleep(2)  # Simulate delay
            try:
                iot_devices = scan_network(ip_range)
                st.success("✅ Scan Completed!")
            except Exception as e:
                st.error(f"⚠️ Error occurred: {e}")
                iot_devices = []
        
        # Show the Devices Found
        if iot_devices:
            st.write("### **🔎 Discovered IoT Devices:**")
            
            device_data = []
            
            for device in iot_devices:
                vulnerabilities = check_vulnerabilities(device)
                status = "Secure ✅" if not vulnerabilities else "⚠️ Vulnerable ❌"
                color_class = "secure" if not vulnerabilities else "vulnerable"
                
                # Add to Table Data
                device_data.append([
                    f"**{device.get('Device Name', 'Unknown')}**",  
                    f"**{device.get('IP', 'N/A')}**",  
                    f"**{device.get('MAC', 'N/A')}**",  
                    f"<span class='{color_class}'>{status}</span>",
                    f"<span class='{color_class}'>{', '.join(vulnerabilities) if vulnerabilities else 'None'}</span>"
                ])
            
            # Display Devices in Table Format
            st.markdown("""
                <style>
                    table { width: 100%; border-collapse: collapse; }
                    th, td { padding: 10px; border: 1px solid #00FF00; text-align: left; }
                    th { background-color: #00FF00; color: black; }
                </style>
            """, unsafe_allow_html=True)

            st.markdown("<table><tr><th>Device Name</th><th>IP Address</th><th>MAC Address</th><th>Status</th><th>Vulnerabilities</th></tr>" +
                        "".join([f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td><td>{row[4]}</td></tr>" for row in device_data]) +
                        "</table>", unsafe_allow_html=True)
        else:
            st.warning("⚠️ No IoT devices found on the network!")
