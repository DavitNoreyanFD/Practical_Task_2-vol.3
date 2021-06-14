"""
module main.py main working module where imported websocketserver module
"""
import websocketserver
import constants


if __name__ == '__main__':
    ip, prt = (constants.ip, constants.port)
    websocketserver.function_to_start_the_server(ip, prt)