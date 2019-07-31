import argparse
from service import *

def main():
    parser = argparse.ArgumentParser()  
    parser.add_argument("-s", "--server", help="IP del servidor. ej: 192.168.0.2:80")
    arguments = parser.parse_args()        
    
    arg=str(arguments.server).split(':')
    try:
        host=arg[0]
        port=arg[1]
        server=service(host, int(port))
    except:
        server=service()
        
    
    server.start()
    

if __name__ == "__main__":
    main()
