# IoT Security Vulnerability Scanner

## Overview
The **IoT Security Vulnerability Scanner** is a Python-based tool that scans IoT devices for security vulnerabilities using **Nmap** and **Shodan API**. It features a **Streamlit web application** to display scan results in a user-friendly manner.
Before you start the project, creat an account in shodan API to get the unique API. and create a file called "api.env" and paste your api key in that file.

# Features
- Scans local network for connected IoT devices using **Nmap**.
- Uses **Shodan API** to fetch security vulnerabilities of detected devices.
- Identifies open ports and weak credentials in IoT devices.
- Provides a **dark hacker-themed UI** using **Streamlit**.

## Installation

### **Step 1: Clone the Repository**
```sh
https://github.com/Skeerthi18/iot_scanner.git
cd iot_scanner.git

## **Step 2: Install Dependencies**
pip install -r requirements.txt

## **Set Up Environment Variables**
Create a .env file inside the config/ folder and add your Shodan API key:
SHODAN_API_KEY=your_shodan_api_key_here

## **Run the Scanner**
To start scanning IoT devices:
streamlit run app.py
