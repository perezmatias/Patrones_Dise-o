from PrenderServer import PrenderServer
from BrasilServer import BrasilServer
from Invoker import Invoker

def main():
    commander = PrenderServer(BrasilServer())
    serverAdmin = Invoker(commander)
    serverAdmin.run()

if __name__ == "__main__":
    main()
