from datetime import datetime

class Logger():

    def __init__(self):
        self.write("Starting Kubewol")

    def write(self,message):
        log_file = open("instance/wol.log", "a")
        log_file.write(f"{datetime.today().strftime('%Y/%m/%d %H:%M')} - {message}\n")
        log_file.close()
    
    def wol(self,hostname):
        self.write(f"WOL;{datetime.today().strftime('%Y/%m/%d %H:%M')};{hostname}\n")
