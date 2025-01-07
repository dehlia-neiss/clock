import time

class Clock:
    #recupérer le temps réel
    def __init__(self):
        self.current_timestamp = time.time()
        self.alarm = None

    def display_time(self):
        hours, minutes, seconds = self.convert_timestamp(self.current_timestamp)
        print(f"{hours:02}:{minutes:02}:{seconds:02}")

    def set_alarm(self, alarm_time):
        #programmer l'alarme
        try:
            hours, minutes, seconds = alarm_time
            now = time.time()
            current_hours, current_minutes, current_seconds = self.convert_timestamp(now)
            offset = ((hours - current_hours) * 3600 + 
                      (minutes - current_minutes) * 60 + 
                      (seconds - current_seconds))
            self.alarm = now + offset
            print(f"Alarm set for {hours:02}:{minutes:02}:{seconds:02}.")
        except ValueError:
            print("Error: Please provide a valid time in the format (hours, minutes, seconds).")

    def check_alarm(self):
        #verifié l'alarme 
        if self.alarm and int(self.current_timestamp) == int(self.alarm):
            print("\nAlarm! It's time!\n")
            self.alarm = None

    def convert_timestamp(self, timestamp):
        #convertir le timestamp en temp réel
        local_time = time.localtime(timestamp)
        hours = local_time.tm_hour
        minutes = local_time.tm_min
        seconds = local_time.tm_sec
        return hours, minutes, seconds

    def start(self):
        try:
            while True:
                self.display_time()
                self.check_alarm()
                self.current_timestamp += 1
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nClock stopped.")


if __name__ == "__main__":
    #programmer l'alarme 
    clock = Clock() 
    clock.set_alarm((16, 30, 10)) 

    clock.start()
