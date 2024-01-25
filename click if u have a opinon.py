import socket

def get_ip_address():
    try:
        # Get the local machine's IP address
        ip_address = socket.gethostbyname(socket.gethostname())
        print(f"Your IP address is: {ip_address}")
    except Exception as e:
        print(f"Error occurred: {e}")

# Call the function to get and print the IP address
get_ip_address()
