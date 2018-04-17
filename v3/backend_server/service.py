""" Backend Service """
import os
import sys

import operations

from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer  # pylint: disable=import-error

SEVER_HOST = 'localhost'
SEVER_PORT = 4040

def add(num1, num2):
    """Add two numbers."""
    print("add is called with %d and %d" % (num1, num2))  # pylint: disable=superfluous-parens
    return num1 + num2

def get_one_news():
    """Get one news"""
    print("getOneNews is called")  # pylint: disable=superfluous-parens
    return operations.get_one_news()

# Threading RPC SimpleJSONRPCServer
RPC_SERVER = SimpleJSONRPCServer((SEVER_HOST, SEVER_PORT))
RPC_SERVER.register_function(add, 'add')
RPC_SERVER.register_function(get_one_news, 'getOneNews')

print("Starting RPC server on %s:%d" % (SEVER_HOST, SEVER_PORT))  # pylint: disable=superfluous-parens
RPC_SERVER.serve_forever()
