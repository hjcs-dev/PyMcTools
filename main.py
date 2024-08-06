import dns.resolver
import requests
from mcrcon import MCRcon
import socket

def menu():
    print("""
    PyMcTools Menu:
    1. Connect to Minecraft Server via RCON
    2. Look Up DNS A Records
    3. Find Minecraft Server Image Link
    4. Get Server MOTD
    5. Get Server Version
    6. List Server Players
    7. Server Ping Test
    8. Get DNS TXT Records
    9. Get DNS MX Records
    10. Get DNS NS Records
    11. Get DNS SOA Records
    12. Get DNS CNAME Records
    13. Get DNS AAAA Records
    14. Get DNS PTR Records
    15. Get Server Status
    16. Get Player Count
    17. Get Max Players
    18. Check Server Online Status
    19. Get Server IP
    20. Exit
    """)

def connect_rcon():
    server = input("Enter Minecraft server address: ")
    password = input("Enter RCON password: ")
    port = input("Enter RCON port (default 25575): ")
    port = int(port) if port else 25575

    try:
        with MCRcon(server, password, port) as mcr:
            print("Connected to RCON. Type 'exit' to quit.")
            while True:
                command = input("RCON> ")
                if command.lower() == 'exit':
                    break
                response = mcr.command(command)
                print("Response: ", response)
    except Exception as e:
        print(f"Failed to connect via RCON: {e}")

def get_dns_records(record_type):
    domain = input("Enter domain: ")
    try:
        answers = dns.resolver.resolve(domain, record_type)
        records = [rdata.to_text() for rdata in answers]
        print(f"{record_type} Records: ", records)
    except Exception as e:
        print(f"Failed to get DNS {record_type} records: {e}")

def find_server_image_link():
    server = input("Enter Minecraft server address: ")
    try:
        response = requests.get(f'https://api.mcsrvstat.us/2/{server}')
        data = response.json()
        image_url = data.get('icon', 'No image found')
        print("Server Image Link: ", image_url)
    except Exception as e:
        print(f"Failed to find server image link: {e}")

def get_server_motd():
    server = input("Enter Minecraft server address: ")
    try:
        response = requests.get(f'https://api.mcsrvstat.us/2/{server}')
        data = response.json()
        motd = data.get('motd', {}).get('clean', 'No MOTD found')
        print("Server MOTD: ", motd)
    except Exception as e:
        print(f"Failed to get server MOTD: {e}")

def get_server_version():
    server = input("Enter Minecraft server address: ")
    try:
        response = requests.get(f'https://api.mcsrvstat.us/2/{server}')
        data = response.json()
        version = data.get('version', 'No version found')
        print("Server Version: ", version)
    except Exception as e:
        print(f"Failed to get server version: {e}")

def get_list_of_players():
    server = input("Enter Minecraft server address: ")
    try:
        response = requests.get(f'https://api.mcsrvstat.us/2/{server}')
        data = response.json()
        players = data.get('players', {}).get('list', 'No player list found')
        print("Player List: ", players)
    except Exception as e:
        print(f"Failed to get list of players: {e}")

def server_ping_test():
    server = input("Enter Minecraft server address: ")
    try:
        response = requests.get(f'https://api.mcsrvstat.us/2/{server}')
        latency = response.elapsed.total_seconds()
        print("Server Ping: ", latency, "seconds")
    except Exception as e:
        print(f"Failed to ping server: {e}")

def get_dns_txt_records():
    get_dns_records('TXT')

def get_dns_mx_records():
    get_dns_records('MX')

def get_dns_ns_records():
    get_dns_records('NS')

def get_dns_soa_records():
    get_dns_records('SOA')

def get_dns_cname_records():
    get_dns_records('CNAME')

def get_dns_aaaa_records():
    get_dns_records('AAAA')

def get_dns_ptr_records():
    get_dns_records('PTR')

def get_server_status():
    server = input("Enter Minecraft server address: ")
    try:
        response = requests.get(f'https://api.mcsrvstat.us/2/{server}')
        data = response.json()
        status = data.get('online', 'No status found')
        print("Server Status: ", "Online" if status else "Offline")
    except Exception as e:
        print(f"Failed to get server status: {e}")

def get_player_count():
    server = input("Enter Minecraft server address: ")
    try:
        response = requests.get(f'https://api.mcsrvstat.us/2/{server}')
        data = response.json()
        player_count = data.get('players', {}).get('online', 'No data')
        print("Player Count: ", player_count)
    except Exception as e:
        print(f"Failed to get player count: {e}")

def get_max_players():
    server = input("Enter Minecraft server address: ")
    try:
        response = requests.get(f'https://api.mcsrvstat.us/2/{server}')
        data = response.json()
        max_players = data.get('players', {}).get('max', 'No data')
        print("Max Players: ", max_players)
    except Exception as e:
        print(f"Failed to get max players: {e}")

def check_server_online_status():
    server = input("Enter Minecraft server address: ")
    try:
        response = requests.get(f'https://api.mcsrvstat.us/2/{server}')
        data = response.json()
        online_status = data.get('online', False)
        print("Server Online Status: ", "Online" if online_status else "Offline")
    except Exception as e:
        print(f"Failed to check server online status: {e}")

def get_server_ip():
    server = input("Enter Minecraft server address: ")
    try:
        ip = socket.gethostbyname(server)
        print("Server IP: ", ip)
    except Exception as e:
        print(f"Failed to get server IP: {e}")

def main():
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            connect_rcon()
        elif choice == '2':
            get_dns_records('A')
        elif choice == '3':
            find_server_image_link()
        elif choice == '4':
            get_server_motd()
        elif choice == '5':
            get_server_version()
        elif choice == '6':
            get_list_of_players()
        elif choice == '7':
            server_ping_test()
        elif choice == '8':
            get_dns_txt_records()
        elif choice == '9':
            get_dns_mx_records()
        elif choice == '10':
            get_dns_ns_records()
        elif choice == '11':
            get_dns_soa_records()
        elif choice == '12':
            get_dns_cname_records()
        elif choice == '13':
            get_dns_aaaa_records()
        elif choice == '14':
            get_dns_ptr_records()
        elif choice == '15':
            get_server_status()
        elif choice == '16':
            get_player_count()
        elif choice == '17':
            get_max_players()
        elif choice == '18':
            check_server_online_status()
        elif choice == '19':
            get_server_ip()
        elif choice == '20':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 20.")

if __name__ == "__main__":
    main()
