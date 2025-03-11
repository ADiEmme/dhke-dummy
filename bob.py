import socket
import random
import time

# Function to perform modular exponentiation
def mod_exp(base, exp, mod):
    result = pow(base, exp, mod)
    print(f"  Calculating: ({base} ^ {exp}) mod {mod} = {result}")
    return result

# Public parameters
p = 23  # Prime modulus (public)
g = 5   # Generator (public)

print("=== Bob's Setup ===")
print(f"Public Parameters:\n  Prime (p): {p}\n  Generator (g): {g}\n")

# Bob generates his private and public keys
bob_private = random.randint(1, p-1)  # Bob's private key
print(f"Bob's Private Key: {bob_private}")

bob_public = mod_exp(g, bob_private, p)  # Bob's public key
print(f"Bob's Public Key: {bob_public}\n")

# Set up the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = 'SERVER_IP_ADDRESS'  # Replace with the server's IP address
server_port = 12345                # Must match the server's port
client_socket.connect((server_host, server_port))

print("\nConnected to Alice.")

# Receive Alice's public key
alice_public = int(client_socket.recv(1024).decode())
print(f"\nReceived Alice's Public Key: {alice_public}")

# Send Bob's public key to Alice
print("\nSending Bob's Public Key to Alice...")
time.sleep(2)  # Simulate a delay for observation
client_socket.send(str(bob_public).encode())

# Compute the shared secret
print("\nCalculating Shared Secret...")
time.sleep(2)  # Simulate a delay for observation
shared_secret = mod_exp(alice_public, bob_private, p)
print(f"Bob's Computed Shared Secret: {shared_secret}\n")

# Close the connection
client_socket.close()
