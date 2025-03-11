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

print("=== Alice's Setup ===")
print(f"Public Parameters:\n  Prime (p): {p}\n  Generator (g): {g}\n")

# Alice generates her private and public keys
alice_private = random.randint(1, p-1)  # Alice's private key
print(f"Alice's Private Key: {alice_private}")

alice_public = mod_exp(g, alice_private, p)  # Alice's public key
print(f"Alice's Public Key: {alice_public}\n")

# Set up the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0'  # Listen on all available interfaces
port = 12345      # Port number
server_socket.bind((host, port))
server_socket.listen(1)

print("Alice is waiting for Bob to connect...")
connection, address = server_socket.accept()
print(f"\nConnected to Bob at {address}")

# Send Alice's public key to Bob
print("\nSending Alice's Public Key to Bob...")
time.sleep(2)  # Simulate a delay for observation
connection.send(str(alice_public).encode())

# Receive Bob's public key
bob_public = int(connection.recv(1024).decode())
print(f"\nReceived Bob's Public Key: {bob_public}")

# Compute the shared secret
print("\nCalculating Shared Secret...")
time.sleep(2)  # Simulate a delay for observation
shared_secret = mod_exp(bob_public, alice_private, p)
print(f"Alice's Computed Shared Secret: {shared_secret}\n")

# Close the connection
connection.close()
server_socket.close()
