import psutil


def main_menu():
    # Boolean för att spåra om övervakning är aktiv
    övervakning_aktiv = False

    # Lista för att lagra larm
    larm_lista = []

    while True:

        print("\n===Övervakningsystem===")
        print("1. Starta övervakning")
        print("2. Lista aktiv övervakning")
        print("3. Skapa larm")
        print("4. Visa Larm")
        print("5. Starta övervakningsläge")
        print("6. Avsluta programmet")

        val = input("\nVälj alternativ (1-6): ")

        # visa systemstatus
        if val == "1":
            övervakning_aktiv = True
            print("Övervakning startad...")

        # lista övervakning, om aktiv
        elif val == "2":
            if övervakning_aktiv == False:
                print("ogiltigt val, ingen övervakning är aktiv återgå till menuval")

            else:
                print(f"CPU användning: {psutil.cpu_percent(interval=1)}%")

                mem = psutil.virtual_memory()
                print(
                    f"Minnesanvändning: {mem.percent}% ({mem.used / (1024**3):.1f} GB av {mem.total / (1024**3):.1f} GB)"
                )

                disk = psutil.disk_usage("/")
                print(
                    f"Diskanvändning: {disk.percent}% ({disk.used / (1024**3):.1f} GB av {disk.total / (1024**3):.1f} GB)"
                )
        # Anger larm-niveå för den valda resursen
        elif val == "3":

            print("\n===Konfigurera Larm===")
            print("1. CPU")
            print("2. Minne")
            print("3. Disk")
            print("4. Återgå till huvudmeny")

            val_3 = input("\n välj Alternativ (1-4):")

            if val_3 == "4":
                pass

            elif val_3 == "1":
                typ = "CPU"

            elif val_3 == "2":
                typ = "Minne"

            elif val_3 == "3":
                typ = "Disk"

            else:
                print("ogiltigt val, välj mellan (1-4)")

            if val_3 in ["1", "2", "3"]:
                try:
                    nivå = int(input(f"Ställ in nivå för {typ}-larm (1-100): "))

                    if 1 <= nivå <= 100:
                        nytt_larm = {"typ": typ, "nivå": nivå}
                        larm_lista.append(nytt_larm)
                        print(f"✓ Larm skapat: {typ} >= {nivå}%")
                    else:
                        print("Ogiltigt! Nivå måste vara mellan 1-100.")

                except ValueError:
                    print("Fel! Ange en siffra.")

        # Visa konfigurerade larm
        elif val == "4":
            print("\n===konfiguerade larm===")

            if not larm_lista:
                print("\n===Inga skapta larm===")

            else:
                # Funktion för att hämta larmtyp för sortering
                def hämta_typ(larm):
                    return larm["typ"]

                sorterade_larm = sorted(larm_lista, key=hämta_typ)

                # Visa larmen med nummer
                for nummer, larm in enumerate(sorterade_larm, 1):
                    print(f"{nummer}. {larm['typ']}larm{larm['nivå']}%")

            input("\nTryck Enter för att återgå till huvudmenyn:     ")


if __name__ == "__main__":
    main_menu()
