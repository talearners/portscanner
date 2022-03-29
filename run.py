from App import PortScanner
from threading import Thread


if __name__ == '__main__':
    try:
        PortScanner()._args()
    except:
        quit()