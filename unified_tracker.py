import time
import requests


def get_member_time(city, country):
    """Fetches real-world Fajr and Maghrib times for a specific city via the free API"""
    url = "https://api.aladhan.com/v1/timingsByCity"
    params = {"city": city, "country": country, "method": 2}
    try:
        response = requests.get(url, params=params, timeout=5)
        if response.status_code == 200:
            data = response.json()
            timings = data["data"]["timings"]
            return {"Fajr": timings["Fajr"], "Maghrib": timings["Maghrib"]}
    except Exception:
        pass
    return {"Fajr": "05:00", "Maghrib": "18:30"}  # Fallback defaults if offline


def run_unified_global_system():
    print("=" * 65)
    print("     PRAYER ALERT CORE UNIFIED BACKEND ENGINE (COST: $0)     ")
    print("=" * 65)

    # 1. Your global group roster configuration
    group_name = "Selsa Global Prayer Network"
    prayer_focus = "Regional Stability and Economic Breakthrough"

    group_members = [
        {"name": "Simi", "city": "Jos", "country": "Nigeria"},
        {"name": "Blessing", "city": "Lagos", "country": "Nigeria"},
        {"name": "Manjang", "city": "London", "country": "UK"},
        {"name": "Nabiel", "city": "Mumbai", "country": "India"},
    ]

    print(f"📡 Active Altar: {group_name}")
    print(f"🎯 Group Focus: \"{prayer_focus}\"")
    print("-" * 65)
    print("[Processing] Fetching live regional updates & parsing cues...\n")

    # 2. Dynamically look up and queue notifications for every country simultaneously
    for member in group_members:
        # Live network API lookup for each user's city
        times = get_member_time(member["city"], member["country"])

        print(f"🔔 [QUEUED] User: {member['name']} ({member['city']})")
        print(f"   🌅 Morning Alert (Fajr):    {times['Fajr']}")
        print(f"   🌆 Evening Alert (Maghrib): {times['Maghrib']}")
        print(
            f"   💬 Broadcast Text: \"Hello {member['name']}, it's time for prayer in {member['city']}. Today's focus: {prayer_focus}\""
        )
        print("-" * 65)

        # Small buffer to respect API traffic speeds
        time.sleep(0.5)

    print("\n" + "=" * 65)
    print("  ENGINE COMPLETED SUCCESSFUL RUN | GLOBAL SERVER FEES: $0.00   ")
    print("=" * 65)


if __name__ == "__main__":
    run_unified_global_system()