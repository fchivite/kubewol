from datetime import datetime

class Logger():

    def write(message):
        log_file = open("instance/wol.log", "a")
        log_file.write(f"{datetime.today().strftime('%Y/%m/%d %H:%M')} - {message}\n")
        log_file.close()
    
    def wol(hostname):
        log_file = open("instance/wol.log", "a")
        log_file.write(f"WOL;{datetime.today().strftime('%Y/%m/%d %H:%M')};{hostname}\n")
        log_file.close()