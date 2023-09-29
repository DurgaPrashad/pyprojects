import subprocess

# Function to get Wi-Fi profiles and passwords
def get_wifi_passwords():
    try:
        # Get a list of Wi-Fi profiles
        profiles = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
        profile_names = [line.split(":")[1].strip() for line in profiles if "All User Profile" in line]

        print("{:<30} | {:<}".format("Wi-Fi Name", "Password"))
        print("-" * 45)

        for profile_name in profile_names:
            try:
                # Get the password for each profile
                password = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile_name, 'key=clear']).decode('utf-8')
                password = [line.split(":")[1].strip() for line in password.split('\n') if "Key Content" in line][0]
                print("{:<30} | {:<}".format(profile_name, password))
            except Exception as e:
                print("{:<30} | {:<}".format(profile_name, "Password not available"))

    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    get_wifi_passwords()
    input("Press Enter to exit...")
