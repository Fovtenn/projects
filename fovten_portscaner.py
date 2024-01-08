import socket
import subprocess
import sys
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex((remote_server_ip, port))
        if result == 0:
            print("Port {}: Açık".format(port))
        sock.close()
    except Exception as e:
        print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    subprocess.call('clear', shell=True)

    remote_server = input("IP girisi saglayin: ")

    try:
        remote_server_ip = socket.gethostbyname(remote_server)
    except socket.gaierror:
        print("Hata: Ana makine adi cozumlenemedi. Cikiliyor")
        sys.exit()

    print("_" * 60)
    print("Lutfen uzak bilgisayari tararken bekleyin", remote_server_ip)
    print("_" * 60)

    t1 = datetime.now()

    try:
        with ThreadPoolExecutor(max_workers=50) as executor:
            executor.map(scan_port, range(1, 1025))

    except KeyboardInterrupt:
        print("Islemi kapatmak icin Ctrl+c ")
        sys.exit()

    except socket.error:
        print("Servere baglanamadi")
        sys.exit()

    t2 = datetime.now()
    total = t2 - t1

    print("Tarama Tamamlandi", total)
