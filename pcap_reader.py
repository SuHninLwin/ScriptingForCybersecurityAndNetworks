"""
pcap_reader.py
Reading the pcap file and get all information
and passes them with different types of objects.
"""
import socket
import dpkt


def pcap_reader(pcap_file):
    """
    This function takes one parameter from the main function.
    Getting all information from pcap in the binary format and
    pass them to other functions in the list objects.
    """
    tcp_info, tcp_ips, tcp_isrc = [], [], []
    tcp_idst, tcp_timestamp, tcp_data, tcp = [], [], [], []
    udp_info, udp_ips, udp_isrc = [], [], []
    udp_idst, udp_timestamp, udp_data, udp = [], [], [], []
    igmp_info, igmp_ips, igmp_isrc = [], [], []
    igmp_idst, igmp_timestamp, igmp_data, igmp = [], [], [], []
    try:
        with open(pcap_file, "rb") as pcap_file_reader:
            pcap_info = dpkt.pcap.Reader(pcap_file_reader)
            for time_stamp, buffer in pcap_info:
                eth = dpkt.ethernet.Ethernet(buffer)
                ip_data = eth.data
                if repr(eth.data.data).startswith("TCP"):
                    tcp_data.append(repr(eth.data.data))
                    tcp.append(ip_data.data)
                    src_ip = socket.inet_ntoa(ip_data.src)
                    dst_ip = socket.inet_ntoa(ip_data.dst)
                    tcp_isrc.append(src_ip)
                    tcp_idst.append(dst_ip)
                    tcp_ips.append(f"{src_ip} -> {dst_ip}")
                    tcp_timestamp.append(time_stamp)
                elif repr(eth.data.data).startswith("UDP"):
                    udp_data.append(repr(eth.data.data))
                    udp.append(ip_data.data)
                    src_ip = socket.inet_ntoa(ip_data.src)
                    dst_ip = socket.inet_ntoa(ip_data.dst)
                    udp_isrc.append(src_ip)
                    udp_idst.append(dst_ip)
                    udp_ips.append(f"{src_ip} -> {dst_ip}")
                    udp_timestamp.append(time_stamp)
                elif repr(eth.data.data).startswith("IGMP"):
                    igmp_data.append(repr(eth.data.data))
                    igmp.append(ip_data.data)
                    src_ip = socket.inet_ntoa(ip_data.src)
                    dst_ip = socket.inet_ntoa(ip_data.dst)
                    igmp_isrc.append(src_ip)
                    igmp_idst.append(dst_ip)
                    igmp_ips.append(f"{src_ip} -> {dst_ip}")
                    igmp_timestamp.append(time_stamp)
            tcp_info = [tcp_ips, tcp_isrc, tcp_idst,
                        tcp_timestamp, tcp_data, tcp]
            udp_info = [udp_ips, udp_isrc, udp_idst,
                        udp_timestamp, udp_data, udp]
            igmp_info = [igmp_ips, igmp_isrc, igmp_idst,
                         igmp_timestamp, igmp_data, igmp]
        return tcp_info, udp_info, igmp_info
    except FileNotFoundError:
        print("[-] Your file is not found! ")
        print(f"Error: {FileNotFoundError}")
    except ValueError:
        print("[-] Your input file has incorrect extension!")
        print(f"Error: {ValueError}")
    except TypeError:
        print("[-] Your input file type has wrong object type!")
        print(f"Error: {TypeError}")
    return None
