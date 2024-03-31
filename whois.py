# File: lookup.py
import socket
import sys

def whois_lookup(target: str):
    print("WHOIS Lookup on target", target + "...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("whois.iana.org", 43))
    s.send(f"{target}\r\n".encode())
    response = s.recv(4096).decode()
    s.close()

    if "returned 0 objects" in response:
        print("WHOIS Lookup failed: No results found.\n")
    else:
        print("WHOIS Lookup completed.\n")
    return response

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 whois.py <target>")
        sys.exit(1)
    
    target = sys.argv[1]
    print(whois_lookup(target))
