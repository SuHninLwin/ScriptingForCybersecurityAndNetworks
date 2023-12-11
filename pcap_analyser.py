"""
pcap_analyser.py
main function to run the scripts
"""
import pcap_reader
import table_drawer
import file_creator
import packet_calculator
import packet_analysis_matplotlib


def main():
    """
    Show all data analyzed from other functions
    """
    pcap = r"Pcap files/evidence-packet-analysis.pcap"
    (tcp_info, udp_info, igmp_info) = pcap_reader.pcap_reader(pcap)
    print(f"[+] Successfully reading: {pcap}\n")
    print()
    print("Reporting data from pcap file ... ")
    print()
    print()
    print("Table with contents from TCP")
    print("============================")
    print(table_drawer.packet_table_drawer(tcp_info))
    print()
    print()
    print("Table with contents from UDP")
    print("============================")
    print(table_drawer.packet_table_drawer(udp_info))
    print()
    print()
    print("Table with contents from IGMP")
    print("============================")
    print(table_drawer.packet_table_drawer(igmp_info))
    print()
    print()
    print("Finding Email Request")
    print("=====================")
    print(table_drawer.email_table_drawer(tcp_info))
    print()
    print()
    print("Finding Image File Request")
    print("==========================")
    print(table_drawer.image_table_drawer(tcp_info))
    print()
    print()
    print("Finding URIs Request")
    print("====================")
    print(table_drawer.uri_table_drawer(tcp_info))
    print()
    print()
    print("Sender & Destination IP Address Pairs (TCP)")
    print("===========================================")
    print(table_drawer.ips_table_drawer(tcp_info))
    print()
    print()
    print("Sender & Destination IP Address Pairs (UDP)")
    print("===========================================")
    print(table_drawer.ips_table_drawer(udp_info))
    print()
    print()
    print("Sender & Destination IP Address Pairs (IGMP)")
    print("============================================")
    print(table_drawer.ips_table_drawer(igmp_info))
    print()
    print()
    print("Way to write data to the file ... ")
    print()
    writing_txt = ({"Table with contents from TCP": tcp_info},
                   {"Table with contents from UDP": udp_info},
                   {"Table with contents from IGMP": igmp_info},
                   {"Finding Email Request": tcp_info},
                   {"Finding Image Request": tcp_info},
                   {"Finding URIs Request": tcp_info},
                   {"Sender & Destination IP Address Pairs (TCP)": tcp_info},
                   {"Sender & Destination IP Address Pairs (UDP)": udp_info},
                   {"Sender & Destination IP Address Pairs (IGMP)": igmp_info},
                   [
                       packet_calculator.dictionary_counter(tcp_info),
                       packet_calculator.dictionary_counter(udp_info),
                       packet_calculator.dictionary_counter(igmp_info)])
    foldername = "Coursework_test"
    dir_name = str(file_creator.creating_dir(foldername))
    txt_name = "Coursework_test.txt"
    file_creator.creating_file(txt_name, dir_name, writing_txt)
    json_name = "Coursework_Json.json"
    file_creator.creating_json(json_name, dir_name, writing_txt[9])
    print()
    print("Creating packet analyser graph with matplotlib")
    packet_analysis_matplotlib.packet_visualization(
        tcp_info, udp_info, igmp_info)


if __name__ == "__main__":
    main()
