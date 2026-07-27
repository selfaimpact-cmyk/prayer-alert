import requests


def get_live_prayer_times(city, country):
    print(f"\n[Connecting] Fetching live data for {city}, {country}...")

    # Free public endpoint - 100% free tool standard
    url = f"https://api.aladhan.com/v1/timingsByCity"
    params = {"city": city, "country": country, "method": 2}  # 2 = ISNA method

    try:
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            timings = data["data"]["timings"]
            date_readable = data["data"]["date"]["readable"]

            print("=" * 50)
            print(f"       LIVE PRAYER TIMES FOR: {city.upper()} ")
            print(f"       Date: {date_readable}")
            print("=" * 50)

            # Display the core times dynamically fetched
            print(f"🌅 Fajr:    {timings['Fajr']}")
            print(f"☀️ Dhuhr:   {timings['Dhuhr']}")
            print(f"🌇 Asr:     {timings['Asr']}")
            print(f"🌆 Maghrib: {timings['Maghrib']}")
            print(f"🌌 Isha:    {timings['Isha']}")
            print("=" * 50)
        else:
            print(f"⚠️ API Error: Unable to fetch times (Status: {response.status_code})")

    except Exception as e:
        print(f"⚠️ Connection Error: {e}")


if __name__ == "__main__":
    # Test your current city or region!
    # Let's check the schedule for Jos, Nigeria
    get_live_prayer_times(city="Jos", country="Nigeria")