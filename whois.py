import socket
import time

def whois_lookup(domain: str):
    print("Looking up target", domain + "...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("whois.iana.org", 43))
    s.send(f"{domain}\r\n".encode())
    response = s.recv(4096).decode()
    s.close()

    if "returned 0 objects" in response:
        print("Lookup failed: No results found.\n")
    else:
        print("Lookup completed.\n")
    return response

print(whois_lookup("google.com"))
