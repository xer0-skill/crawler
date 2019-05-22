from aiohttp import web
import json


def json_response(data):
    return web.Response(text=json.dumps(data), headers={'content-type': 'application/json'})


dsn = "dbname={} user={} password={} host= {}".format(
    'asynctest',
    'oleg',
    'elastispasswd',
    '127.0.0.1'
)
