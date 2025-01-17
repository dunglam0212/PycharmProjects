from Module2.C31Split_URL.Process import Split_URL

url = "http://www.mywebsite.com/apparel/skirt.php?sku=123&lang=en&sect=silk"
print(url.split("/"))

protocol, domain_name, directory, filename, query_parameters = Split_URL(url)
print(protocol)
print(domain_name)
print(directory)
print(filename)
print(query_parameters)