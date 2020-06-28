from cgi import parse_qs
from template import html

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]

    sum, mul = -2147483648, -2147483648 

    try:
        a, b = int(a), int(b)
        sum = a+b
        mul = a*b
    except ValueError:
	sum = -2147483647
	mul = -2147483647    
    response_body = html % {'sum':sum, 'mul':mul}
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
        ])
    return [response_body]
