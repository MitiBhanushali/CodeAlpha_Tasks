# CodeAlpha – Basic Network Sniffer

## Project Overview
This project is a basic network sniffer developed as part of the
CodeAlpha Cyber Security Internship.

The program captures live network packets and displays key details such as:
- Source IP address
- Destination IP address
- Protocol type
- Timestamp

## Objective
The objective of this project is to understand:
- How data packets travel over a network
- How network traffic can be monitored and analyzed for security purposes

## Technologies Used
- Python 3
- Scapy Library
- VS Code
- Windows 10

Note: Administrator or root privileges may be required to run this program.

## How It Works
The program uses the Scapy library to capture live network packets.
It checks whether the packet contains IP data.
Source and destination IP addresses are extracted.
The protocol type (TCP, UDP, or other) is identified.
Each packet is displayed with a timestamp and packet number.

## How to Run the Program
1. Open Command Prompt or VS Code as Administrator
2. Navigate to the project directory
3. Install Scapy (if not already installed):
   pip install scapy
4. Run the program:
   python sniffer.py
5. Open any website to generate network traffic
6. Press Ctrl + C to stop packet capture

## Sample Output
[1] 15:42:10 | TCP | 192.168.1.5 → 8.8.8.8

## Learning Outcome
- Understanding of network packets and protocols
- Hands-on experience with packet sniffing
- Exposure to basic cybersecurity concepts

## Disclaimer
This project is developed strictly for educational purposes as part of a
cybersecurity internship and should only be used on authorized networks.

## Author
Miti Bhanushali
