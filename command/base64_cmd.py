from cli.command import command
from cli.log import *
from base64 import b64encode, b64decode
from binascii import Error


@command(['b64e', 'encode64'], 'Convert some text to Base64', [
    {
        'type': 'str',
        'infinite': True
    }
])
def encode_base64(text: str):
    try:
        log(b64encode(text.encode('utf-8')).decode('utf-8'))
    except Error:
        log(' $c| Error >>> $rO-Onee-chan, I c-cannot encode that >n<')


@command(['b64d', 'decode64'], 'Convert some Base64 text to normal text', [
    {
        'type': 'str',
        'infinite': True
    }
])
def decode_base64(text: str):
    try:
        log(' $c|-> $r' + b64decode(text.encode('utf-8')).decode('utf-8'))
    except Error:
        log(' $c| Error >>> $rC-Cannot decode that text >.<')
