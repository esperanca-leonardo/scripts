#!/usr/bin/python3

import sys

def calculate_network(ip_cidr):
    # Split IP and subnet mask
    ip, cidr_mask = ip_cidr.split('/')
    cidr_mask = int(cidr_mask)

    # Calculate subnet mask
    mask_octets = [0, 0, 0, 0]
    for i in range(cidr_mask):
        mask_octets[i//8] += 1 << (7 - i % 8)

    # Split the IP into octets
    ip_octets = [int(octet) for octet in ip.split('.')]

    # Apply the mask to the IP to get the network address
    network_octets = [ip_octets[i] & mask_octets[i] for i in range(4)]

    # Join the octets to form the network address string
    network_address = '.'.join(map(str, network_octets))

    # Join the mask octets to form the subnet mask string
    subnet_mask = '.'.join(map(str, mask_octets))

    # Combine network address and subnet mask into a single string
    network_with_mask = f"{network_address}/{cidr_mask}"

    # Return the combined string
    return network_with_mask

if __name__ == "__main__":
    # Check if a command-line argument is passed
    if len(sys.argv) != 2:
        print("Usage: python name_of_program.py ip_address/subnet_mask")
        sys.exit(1)

    ip_cidr = sys.argv[1]

    result = calculate_network(ip_cidr)
    print(result)
