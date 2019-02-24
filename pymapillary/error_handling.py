from pymapillary import Mappilary

import requests

def http_error_handler(http_status_code):

    '''Displays reason for http status code

    param http_stats_code(int): The http status code from a web request

    '''

    if http_status_code is 400:
        raise Exception("400: The URL parameters or the JSON body in the request are invalid.")
    elif http_status_code is 401:
        raise Exception("401: The request requires user authentication.")
    elif http_status_code is 404:
        raise Exception("404: The requested resource is not found.")
    elif http_status_code is 500:
        raise Exception("500: Servers refuse to work. Either systems are not operational, or it is a service bug which is worth a report at https://github.com/mapillary/mapillary_issues")
    else:
        return None
