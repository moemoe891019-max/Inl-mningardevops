class Alarm:

    # Representerar ett enskilt larm
    def __init__(self, alarm_type, level):
        self.alarm_type = alarm_type
        self.level = level

    def is_triggered(self, current_value):
        # Checkar om larmet har triggats
        return current_value >= self.level

    def get_warning_message(self, current_value):
        # Returnerar varningsmeddelandet
        return f"WARNING LARM IS ACTIVE, {self.alarm_type.upper()} USAAGE IS OVER SETLEVEL {self.level}%"


# TEST-KOD FÖR ALARM
if __name__ == "__main__":

    # Skapa ett test-larm
    test_alarm = Alarm("CPU", 80)

    # Test 1: Larm INTE triggat (70 < 80)
    result1 = test_alarm.is_triggered(70)
    print({result1})
    if result1 == False:
        print("Passsed")
    else:
        print("Failed")

    # Test 2: Larm triggat (85 >= 80)
    result2 = test_alarm.is_triggered(85)
    print({result2})
    if result2 == True:
        print("Passed")
    else:
        print("Failed")

    # Test 3: Varningsmeddelande
    message = test_alarm.get_warning_message(85)
    print({message})
    print("Passed")


class AlarmManager:
    # Hanterar alla larmen

    def __init__(self):
        self.alarms = []

    def add_alarm(self, alarm_type, level):
        # Lägger till ett nytt larm
        alarm = Alarm(alarm_type, level)
        self.alarms.append(alarm)

    def check_all_alarms(self, cpu, memory, disk):
        # Checkar alla larmen och returnerar triggade
        triggered = []

        for alarm in self.alarms:
            if alarm.alarm_type == "CPU" and alarm.is_triggered(cpu):
                triggered.append(alarm)
            elif alarm.alarm_type == "Minne" and alarm.is_triggered(memory):
                triggered.append(alarm)
            elif alarm.alarm_type == "Disk" and alarm.is_triggered(disk):
                triggered.append(alarm)

        return triggered


# TEST-KOD FÖR ALARMMANAGER

manager = AlarmManager()

# Test 1: Lägg till larmen
manager.add_alarm("CPU", 80)
manager.add_alarm("Mem", 70)
manager.add_alarm("Disk", 90)
print({len(manager.alarms)})


# Test 2: Checka larmen
triggered = manager.check_all_alarms(cpu=85, memory=75, disk=90)
print({len(triggered)})


# Test 3: Inget triggat
triggered_none = manager.check_all_alarms(cpu=75, memory=60, disk=60)
print({len(triggered_none)})
