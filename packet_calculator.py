"""
packet_calculator.py
Calculating length of packets and mean packets
Counting src and dst IPs pairs
"""
import operator


def dictionary_counter(counter_information):
    """
    This function takes one parameter (a list) from pcap reader.
    Calculating the counts of sender and destination IP pairs.
    """
    dictionary = {}
    ips_list = counter_information[0]
    for ips in ips_list:
        dictionary[ips] = ips_list.count(ips)
    sorted_dict = sorted(dictionary.items(),
                         key=operator.itemgetter(1),
                         reverse=True)
    return sorted_dict


def mean_calculator(calculate_info):
    """
    This function takes one parameter (a list) from pcap reader.
    Calculating the number of packets and mean packets to report the pcap data.
    """
    counter = 0
    packet = len(calculate_info[4])
    try:
        for info in calculate_info[5]:
            counter = counter + len(info)
        mean = counter/packet
        return (packet, mean)
    except ZeroDivisionError:
        print("[-] Packet with zero length causes zero division!")
        print(f" Error: {ZeroDivisionError}")
    return None
