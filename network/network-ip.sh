#!/bin/bash

# Obter o endereço IP usando o comando diretamente
ip_address=$(ip addr show | grep 'inet ' | grep -v '127.0.0.1' | awk '{print $2}')

python3 /home/esperanca/scripts/network/calculate-network-ip.py "$ip_address"
