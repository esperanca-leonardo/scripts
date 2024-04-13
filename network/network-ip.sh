#!/bin/bash

# Obtain the IP address using the command directly
ip_address=$(ip addr show | grep 'inet ' | grep -v '127.0.0.1' | awk '{print $2}')

python3 $HOME/scripts/network/calculate-network-ip.py "$ip_address"
