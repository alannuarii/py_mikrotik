from librouteros import connect

# Konfigurasi koneksi Mikrotik
host = "192.168.x.x"  # Gantilah dengan IP Mikrotik Anda
username = "admin"    # Gantilah dengan username Mikrotik
password = "password" # Gantilah dengan password Mikrotik

# Buat koneksi ke Mikrotik
api = connect(username=username, password=password, host=host)

# Ambil data dari DHCP Leases
dhcp_leases = api.path("ip", "dhcp-server", "lease")

# Iterasi melalui semua entri DHCP Leases yang didapatkan
for lease in dhcp_leases:
    ip = lease.get('address')
    mac_address = lease.get('mac-address')
    host_name = lease.get('host-name')  # Mendapatkan hostname (jika tersedia)
    user_identifier = lease.get('comment')  # Mendapatkan identifier user (jika ada)
    print(f"IP: {ip}, MAC: {mac_address}, Hostname: {host_name}, User: {user_identifier}")
