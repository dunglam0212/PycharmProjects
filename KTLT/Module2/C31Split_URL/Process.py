def Split_URL(url):
    parts = url.split("/")
    protocol = parts[0] + "//"
    hostname = parts[2]
    hostname_parts = hostname.split(".")
    domain_name = hostname_parts[1]
    directory = parts[3]
    others = parts[4].split("?")
    filename = others[0]
    query_parameters = others[1]
    return protocol, domain_name, directory, filename, query_parameters
