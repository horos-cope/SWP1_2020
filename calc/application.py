from cgi import parse_qs
from template import html

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]

    if '' in [a,b]:
        a, b = int(a), int(b)
        add = a+b
        mul = a*b
        #add와 mul을 저장.
    response_body = html
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
        ])
    return [response_body]
