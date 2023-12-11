"""
packet_analysis_matplotlib.py
Visualizes all the data with line graph.
"""
import datetime
import matplotlib.pyplot as plt


def count_interval(sortedtimestamps_list):
    """
    This function takes a parameter from above function.
    Receives the sorted list of time stamps and count them.
    It passes timestamps and count variables to other function and
    let it make into matplotlib.
    """
    timeintervals = []
    time_intervals = []
    count = []
    interval = 25.0
    first_timestamp = sortedtimestamps_list[0]
    last_timestamp = sortedtimestamps_list[
        len(sortedtimestamps_list)-1]
    for _ in range(len(sortedtimestamps_list)):
        if first_timestamp < last_timestamp:
            first_timestamp = first_timestamp + interval
            time_intervals.append(first_timestamp)
    c_one, c_two, c_three, c_four, c_five = 0, 0, 0, 0, 0
    c_six, c_seven, c_eight, c_nine, c_ten = 0, 0, 0, 0, 0
    for sorted_timestamps in sortedtimestamps_list:
        if sorted_timestamps < time_intervals[0]:
            c_one += 1
        if time_intervals[0] < sorted_timestamps < time_intervals[1]:
            c_two += 1
        if time_intervals[1] < sorted_timestamps < time_intervals[2]:
            c_three += 1
        if time_intervals[2] < sorted_timestamps < time_intervals[3]:
            c_four += 1
        if time_intervals[3] < sorted_timestamps < time_intervals[4]:
            c_five += 1
        if time_intervals[4] < sorted_timestamps < time_intervals[5]:
            c_six += 1
        if time_intervals[5] < sorted_timestamps < time_intervals[6]:
            c_seven += 1
        if time_intervals[6] < sorted_timestamps < time_intervals[7]:
            c_eight += 1
        if time_intervals[7] < sorted_timestamps < time_intervals[8]:
            c_nine += 1
        if time_intervals[8] < sorted_timestamps < time_intervals[9]:
            c_ten += 1
    count.append(c_one)
    count.append(c_two)
    count.append(c_three)
    count.append(c_four)
    count.append(c_five)
    count.append(c_six)
    count.append(c_seven)
    count.append(c_eight)
    count.append(c_nine)
    count.append(c_ten)
    for interval in time_intervals:
        interval = datetime.datetime.fromtimestamp(
            int(str(interval).split(".")[0])).strftime("%H:%M:%S")
        timeintervals.append(interval)
    return (timeintervals, count)


def packet_visualization(tcp_info, udp_info, igmp_info):
    """
    This function takes three parameters from main function.
    Receives the passed data and analyze them in order to
    visualize it. Data from pcap are analyzed and reported
    into line graph with matplotlib.
    """
    all_timestamp_list = []
    timestamps_list = []
    all_timestamp_list.append(tcp_info[3])
    all_timestamp_list.append(udp_info[3])
    all_timestamp_list.append(igmp_info[3])
    for timestamp_list in all_timestamp_list:
        for timestamps in timestamp_list:
            timestamps_list.append(timestamps)
    sorted_timestamps_list = sorted(timestamps_list)
    time_interval, count = count_interval(sorted_timestamps_list)
    plt.figure(figsize=(10, 18))
    plt.plot(time_interval, count, marker="s", label="Packets")
    plt.title("Packet Analysis")
    plt.xlabel("Date Time")
    plt.ylabel("Packet Count")
    plt.xticks(rotation=45, ha="right")
    plt.legend()
    plt.grid(True)
    # Modified from stackoverflow
    # Author: pufferfish
    # Edited Time: Aug 14 '09 at 15:57
    plt.savefig("diagram.png", bbox_inches="tight", dpi=300)
