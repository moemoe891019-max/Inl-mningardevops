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
