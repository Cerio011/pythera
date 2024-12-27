from scapy.all import ARP, Ether, srp

def arp_discovery(target_subnet):
    try:
        arp = ARP(pdst=target_subnet)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether / arp
        result, _ = srp(packet, timeout=2, iface_hint=target_subnet, verbose=False)

        active_hosts = []
        for sent, received in result:
            active_hosts.append({'ip': received.psrc, 'mac': received.hwsrc})
        return active_hosts
    except Exception as e:
        print(f"Erro durante a descoberta ARP: {e}")
        return []

if __name__ == "__main__":
    active_hosts = arp_discovery("192.168.15.0/24")
    print("Active hosts:", active_hosts)
