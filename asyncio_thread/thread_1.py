import threading

if __name__ == "__main__":
    x = threading.Thread(target=tsu_watchdog, daemon= True)
    x.setDaemon()