class Alarm:
    """Represents a single alarm."""

    def __init__(self, alarm_type, level):
        self.alarm_type = alarm_type
        self.level = level

    def is_triggered(self, current_value):
        """Checks if the alarm has been triggered."""
        return current_value >= self.level

    def get_warning_message(self, current_value):
        """Returns the warning message."""
        return f"***VARNING, LARM AKTIVERAT, {self.alarm_type.upper()} ANVÄNDNING ÖVERSTIGER {self.level}%***"


class AlarmManager:
    """Manages all the alarms."""

    def __init__(self):
        self.alarms = []

    def add_alarm(self, alarm_type, level):
        """Adds a new alarm."""
        alarm = Alarm(alarm_type, level)
        self.alarms.append(alarm)

    def check_all_alarms(self, cpu, memory, disk):
        """Checks all alarms and returns the triggered ones."""
        triggered = []

        for alarm in self.alarms:
            if alarm.alarm_type == "CPU" and alarm.is_triggered(cpu):
                triggered.append(alarm)
            elif alarm.alarm_type == "Memory" and alarm.is_triggered(memory):
                triggered.append(alarm)
            elif alarm.alarm_type == "Disk" and alarm.is_triggered(disk):
                triggered.append(alarm)

        return triggered

    def get_sorted_alarms(self):
        """Returns the alarms sorted by type."""

        def get_alarm_type(alarm):
            return alarm.alarm_type

        return sorted(self.alarms, key=get_alarm_type)


# Test code
if __name__ == "__main__":

    print("--- Testing Alarm class ---")
    # Create a test alarm
    test_alarm = Alarm("CPU", 80)

    # Test: Alarm triggered (85 >= 80)
    result = test_alarm.is_triggered(85)
    print(f"Alarm triggered (85 >= 80): {result}")

    # Test: Alarm not triggered (75 < 80)
    result = test_alarm.is_triggered(75)
    print(f"Alarm triggered (75 < 80): {result}")

    # Test: Warning message
    message = test_alarm.get_warning_message(85)
    print(f"Warning message: {message}")

    print("\n--- Testing AlarmManager class ---")
    manager = AlarmManager()

    # Test: Add alarms
    manager.add_alarm("CPU", 80)
    manager.add_alarm("Memory", 70)
    manager.add_alarm("Disk", 90)
    print(f"Number of alarms: {len(manager.alarms)}")

    # Test: Check alarms (some triggered)
    triggered_alarms = manager.check_all_alarms(cpu=85, memory=75, disk=80)
    print(f"Number of triggered alarms (should be 2): {len(triggered_alarms)}")
    for alarm in triggered_alarms:
        print(f"- Triggered: {alarm.alarm_type}")

    # Test: Check alarms (none triggered)
    triggered_none = manager.check_all_alarms(cpu=75, memory=60, disk=60)
    print(f"Number of triggered alarms (should be 0): {len(triggered_none)}")
