def convert_to_seconds(time_string):
    m,s = time_string.split(":")
    return int(m)*60 + int(s)