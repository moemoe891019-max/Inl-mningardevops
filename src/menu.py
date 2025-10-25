from alarm import AlarmManager, Alarm
from monitoring import Monitor
import threading
import time


class Menu:
    """Handles all I/O and user interaction"""

    def __init__(self):
        self.alarm_manager = AlarmManager()
        self.monitor = Monitor()
        self.monitoring_active = False
        self.surveillance_active = False
        self.monitoring_thread = None

    def show_main_menu(self):
        """Displays the main menu"""
        print("\n=== MONITORING===")
        print("1. Start monitoring")
        print("2. List active surveillance")
        print("3. Create alarm")
        print("4. Show alarms")
        if not self.surveillance_active:
            print("5. Start surveillance mode")
        else:
            print("5. Stop surveillance mode")
        print("6. Exit program")

    def get_user_choice(self):
        """Gets input from the user"""
        return input("\nChoose option (1-6): ")

    def start(self):
        """Starts the main menu loop"""
        while True:
            self.show_main_menu()
            choice = self.get_user_choice()

            if choice == "1":
                self.val_1_start_monitoring()
            elif choice == "2":
                self.val_2_list_monitoring()
            elif choice == "3":
                self.val_3_create_alarm()
            elif choice == "4":
                self.val_4_show_alarm()
            elif choice == "5":
                self.toggle_surveillance_mode()
            elif choice == "6":
                print("Exiting program.")
                if self.surveillance_active:
                    self.toggle_surveillance_mode()  # Stop surveillance before exiting
                break
            else:
                print("Invalid choice. Please try again.")

    def val_1_start_monitoring(self):
        """CHOICE 1: Start monitoring"""
        self.monitoring_active = True
        print("Monitoring started...")

    def val_2_list_monitoring(self):
        """CHOICE 2: List active monitoring"""
        if not self.monitoring_active:
            print("No monitoring is active.")
        else:
            values = self.monitor.get_all_values()
            print(f"\nCPU Usage: {values['cpu']}% ")
            print(
                f"Memory usage: {values['memory']}% ({values['memory_used_gb']:.1f} GB of {values['memory_total_gb']:.1f} GB)"
            )
            print(
                f"Disk usage: {values['disk']}% ({values['disk_used_gb']:.1f} GB of {values['disk_total_gb']:.1f} GB)"
            )

        input("\nPress Enter to return to the menu: ")

    def val_3_create_alarm(self):
        """CHOICE 3: Create alarm"""
        print("\n=== Configure Alarm ===")
        print("1. CPU")
        print("2. Memory")
        print("3. Disk")
        print("4. Return to main menu")

        choice = input("\nChoose an option (1-4): ")

        if choice == "4":
            return
        elif choice == "1":
            alarm_type = "CPU"
        elif choice == "2":
            alarm_type = "Memory"
        elif choice == "3":
            alarm_type = "Disk"
        else:
            print("Invalid choice.")
            return

        try:
            level = int(
                input(
                    f"Set your preferred threshold level (1-100) for the {alarm_type} alarm: "
                )
            )

            if 1 <= level <= 100:
                self.alarm_manager.add_alarm(alarm_type, level)
                print(f"✓ Alarm created: {alarm_type} : {level}%")
            else:
                print("Invalid input, the value must be between 1 and 100.")

        except ValueError:
            print("You must enter a number!")

    def val_4_show_alarm(self):
        """CHOICE 4: Show alarms"""
        if not self.alarm_manager.alarms:
            print("No alarms have been created.")
        else:
            print("\n=== Configured Alarms ===")
            # Sort the alarms (functional programming!)
            sorted_alarms = self.alarm_manager.get_sorted_alarms()

            for alarm in sorted_alarms:
                print(f"{alarm.alarm_type.capitalize()} larm {alarm.level}%")

        input("\nPress Enter to return to the main menu: ")

    def toggle_surveillance_mode(self):
        """CHOICE 5: Start or stop surveillance mode"""
        if not self.surveillance_active:
            self.surveillance_active = True
            print("\nStarting surveillance mode...")
            self.monitoring_thread = threading.Thread(target=self.surveillance_loop)
            self.monitoring_thread.daemon = True
            self.monitoring_thread.start()
            input(
                "\nÖvervakning är aktiv. Tryck på valfri tangent för att återgå till menyn."
            )
        else:
            self.surveillance_active = False
            if self.monitoring_thread and self.monitoring_thread.is_alive():
                self.monitoring_thread.join()
            print("Surveillance stopped.")

    def surveillance_loop(self):
        """Loop that runs the monitoring in the background"""
        try:
            while self.surveillance_active:
                values = self.monitor.get_all_values()
                triggered = self.alarm_manager.check_all_alarms(
                    cpu=values["cpu"], memory=values["memory"], disk=values["disk"]
                )

                for alarm in triggered:
                    current_value = 0

                    if alarm.alarm_type == "CPU":
                        current_value = values["cpu"]
                    elif alarm.alarm_type == "Memory":
                        current_value = values["memory"]
                    elif alarm.alarm_type == "Disk":
                        current_value = values["disk"]

                    print(alarm.get_warning_message(current_value))

                time.sleep(1)

        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    menu = Menu()
    menu.start()
