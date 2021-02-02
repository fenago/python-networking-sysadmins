import http.client

con_obj = http.client.HTTPConnection('www.fenago.com', 80, timeout=100)
print(con_obj)
