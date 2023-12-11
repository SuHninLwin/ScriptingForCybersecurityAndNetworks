"""
data_filter.py
Find all the matches with re module
Remove the duplicates values from the list
"""
import re


def email_filter(email_information):
    """
    This function takes one parameter (a list) from pcap reader.
    Filtering out the matched emails from the data of pcap file.
    """
    to_email_list = []
    from_email_list = []
    receiver_email = []
    sender_email = []
    email_info_list = email_information[5]
    for email_info in email_info_list:
        email_info_decode = email_info.data.decode("utf-8", "ignore")
        to_email = re.findall(r"TO: \W\w+@\w+.com\W", email_info_decode)
        if len(to_email) > 0:
            to_email_list.append(to_email)
    for email_info in email_info_list:
        email_info_decode = email_info.data.decode("utf-8", "ignore")
        from_email = re.findall(r"[F|f][R|r][O|o][M|m]: \W\w+@\w+.com\W",
                                email_info_decode)
        if len(from_email) > 0:
            from_email_list.append(from_email)
    for to_emails in to_email_list:
        for to_email in to_emails:
            to_email = to_email.strip("TO: ")
            receiver_email.append(to_email)
    receiver_email = list(dict.fromkeys(receiver_email))
    for from_emails in from_email_list:
        for from_email in from_emails:
            from_email = from_email.strip("FROM: ")
            sender_email.append(from_email)
    sender_email = list(dict.fromkeys(sender_email))
    return receiver_email, sender_email


def image_filter(image_information):
    """
    This function takes one parameter (a list) from pcap reader.
    Filtering out the matched requested images (png| jpg| gif)
    from the data of pcap file.
    """
    png, jpg, gif = [], [], []
    png_list, jpg_list, gif_list = [], [], []
    image_info_list = image_information[5]
    for image_info in image_info_list:
        str_png = repr(image_info.data)
        uri_png = re.findall(r"\w+\.png", str_png)
        if len(uri_png) > 0:
            png.append(uri_png)
    for png_element in png:
        for p_element in png_element:
            png_list.append(p_element)
    png_list = list(dict.fromkeys(png_list))
    for image_info in image_info_list:
        str_jpg = repr(image_info.data)
        uri_jpg = re.findall(r"\w+\.jpg", str_jpg)
        if len(uri_jpg) > 0:
            jpg.append(uri_jpg)
    for jpg_element in jpg:
        for j_element in jpg_element:
            jpg_list.append(j_element)
    jpg_list = list(dict.fromkeys(jpg_list))
    for image_info in image_info_list:
        str_gif = repr(image_info.data)
        uri_gif = re.findall(r"\w+\.gif", str_gif)
        if len(uri_gif) > 0:
            gif.append(uri_gif)
    for gif_element in gif:
        for g_element in gif_element:
            gif_list.append(g_element)
    gif_list = list(dict.fromkeys(gif_list))
    return png_list, jpg_list, gif_list


def uri_filter(uri_information):
    """
    This function takes one parameter (a list) from pcap reader.
    Filtering out the matched uri (http| https) from the data of pcap file.
    """
    uri_link_list = []
    uri_list = []
    uri_info_list = uri_information[5]
    for uri_info in uri_info_list:
        uri_decode = uri_info.data.decode("utf-8", "ignore")
        uri = re.findall(r"(GET \/\w+(\/\w+)+(\.gif)?(\.jpg)?(\.png)?)",
                         uri_decode)
        if len(uri) > 0:
            uri_link_list.append(uri)
    for uri_links in uri_link_list:
        for uri_link in uri_links:
            for uri in uri_link:
                if len(uri) > 15:
                    uri_list.append(uri)
    uri_list = list(dict.fromkeys(uri_list))
    return uri_list
