import subprocess

meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
data = meta_data.decode('utf-8', errors="backslashreplace")
data = data.split('\n')
profiles = []
for i in data:
    # Change it into your language -- can be found by running "netsh wlan show profiles" on cmd
    if "Tutti i profili utente" in i:
        i = i.split(":")
        i = i[1]
        i = i[1:-1]
        #print(i)
        profiles.append(i)

print("{:<30}| {:<}.".format("Wi-Fi Name", "Password"))
print("----------------------------------------------")

for i in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear'])
        results = results.decode('utf-8', errors="backslashreplace")
        results = results.split('\n')
        # Change it into your language -- can be found by running "netsh wlan show profile [profile name] key=clear" on cmd
        results = [b.split(":")[1][1:-1] for b in results if "Contenuto chiave" in b]

        try:
            print("{:<30}| {:<}".format(i, results[0]))
        
        except IndexError:
            print("{:<30}| {:<}".format(i, "@No Password@"))

    except subprocess.CalledProcessError:
        print("Encoding Error")
