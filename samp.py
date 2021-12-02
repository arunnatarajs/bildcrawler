import requests
try:
    link = 'https://www.apollohospiitals.com/404' 
    request_from_link = requests.get(link) 
# this causes the code to call a timeout if the connection or delays in 
# between the reads take more than 10 seconds
    print(request_from_link.status_code)

except Exception as e:
    print(e)