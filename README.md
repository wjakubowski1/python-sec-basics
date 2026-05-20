# Python Security Basics

Welcome to my personal playground for learning Python, networking, and cybersecurity fundamentals. This repository contains simple, hands-on scripts built from scratch to understand how network protocols work and how security mechanisms operate under the hood.

## Repository Contents

### 1. Network Recon Scanner (`network_recon.py`)
A lightweight, raw TCP port scanner built using Python's native `socket` library. 
- **What it does:** Takes a target IP address and scans a list of critical ports (21, 22, 80, 443, 3389) to check if they are open.
- **Security Logic:** It doesn't just check if a port is open; it identifies the potential risks associated with exposed services (like SSH or RDP) and flags critical exposures.
- **Key Learning Points:** Implementing network sockets, managing timeouts, and handling conditional mapping without external dependencies.
