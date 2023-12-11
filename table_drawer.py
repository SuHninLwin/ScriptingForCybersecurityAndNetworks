"""
table_drawer.py
All function comes to this py file and creates into visualize tables.
"""
import datetime
from prettytable import PrettyTable
import data_filter
import packet_calculator


def email_table_drawer(info):
    """
    This function takes one parameter (a list) to iterate.
    Drawing the table of pcap data (Sender and Receiver Emails)
    with prettytable module.
    """
    receiver_email, sender_email = data_filter.email_filter(info)
    table = PrettyTable()
    column_name = ["Sender Email", "Receiver Email"]
    table_adjustment(receiver_email, sender_email)
    table.add_column(column_name[0], receiver_email)
    table.add_column(column_name[1], sender_email)
    return table


def image_table_drawer(info):
    """
    This function takes one parameter (a list) to iterate.
    Drawing the table of pcap data (PNG, JPG, GIF) with prettytable module.
    """
    png_list, jpg_list, gif_list = data_filter.image_filter(info)
    table = PrettyTable()
    column_name = ["PNG Image", "JPG Image", "GIF Image"]
    table_adjustment(png_list, jpg_list, gif_list)
    table.add_column(column_name[0], png_list)
    table.add_column(column_name[1], jpg_list)
    table.add_column(column_name[2], gif_list)
    return table


def ips_table_drawer(info):
    """
    This function takes one parameter (a list) to iterate.
    Drawing the table of pcap data (Sender and Destination IPs Pair
    and counts of each pair) with prettytable module.
    """
    dic = packet_calculator.dictionary_counter(info)
    table = PrettyTable()
    table.field_names = ["IPs (Src -> Dst)", "Count"]
    for key in dic:
        table.add_row([key[0], key[1]])
    return table


def packet_table_drawer(info):
    """
    This function takes one parameter (a list) to iterate.
    Drawing the table of pcap data
    (no. of packets, mean packet, first and last timestamp)
    with prettytable module.
    """
    try:
        (packet, mean) = packet_calculator.mean_calculator(info)
        table = PrettyTable()
        table.field_names = ["No. of Packets", "Mean Packets",
                             "First Timestamp", "Last Timestamp"]
        table.add_row([packet, mean,
                       datetime.datetime.utcfromtimestamp(
                           info[3][0]),
                       datetime.datetime.utcfromtimestamp(
                           info[3][len(info[3])-1])])
        return table
    except TypeError:
        print(f"[-] Passed variable cannot be iterated! Error: {TypeError}")
    return None


def table_adjustment(*columns):
    """
    This function takes all the parameters that are passed to it.
    Formatting the columns of prettytable.
    Not specific lengths of columns can be added to the table.
    Copy from stackoverflow
    Author: Matt Miguel
    Edited Time: Jan 20 at 8:57
    """
    max_len = max([len(col) for col in columns])
    for col in columns:
        col.extend([""]*(max_len-len(col)))


def uri_table_drawer(info):
    """
    This function takes one parameter (a list) to iterate.
    Drawing the table of pcap data (URIs list) with prettytable module.
    """
    uri_list = data_filter.uri_filter(info)
    table = PrettyTable()
    column_name = ["HTTP Link Request"]
    table.add_column(column_name[0], uri_list)
    return table
