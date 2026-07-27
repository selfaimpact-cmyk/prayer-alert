import time


def simulate_global_broadcast():
    print("=" * 60)
    print("      PRAYER ALERT GLOBAL ROUTING ENGINE (COST: $0)     ")
    print("=" * 60)

    # 1. Simulate a group structure inside our free data tier
    prayer_group = {
        "group_name": "Simi's Global Prayer Chain",
        "leader": "Sarafina",
        "daily_focus": "Gratitude, Peace, and Community Growth",
        "members": [
            {"name": "Blessing", "city": "Jos", "country": "Nigeria"},
            {"name": "John", "city": "London", "country": "UK"},
            {"name": "Ananya", "city": "Mumbai", "country": "India"},
            {"name": "Carlos", "city": "Sao Paulo", "country": "Brazil"},
        ],
    }

    print(f"📡 Group Created: {prayer_group['group_name']}")
    print(f"📝 Today's Shared Focus: \"{prayer_group['daily_focus']}\"\n")
    print("[Processing] Simulating localized browser push delivery...\n")

    # 2. Simulate looping through members instantly across different continents
    for member in prayer_group["members"]:
        print(f"🔔 [FREE WEB PUSH SENT] -> To: {member['name']}")
        print(
            f"   📍 Location: {member['city']}, {member['country']} | Delivery Status: 100% Success"
        )
        print(
            f"   💬 Screen Message: \"Hi {member['name']}, join {prayer_group['leader']}'s altar now. Focus: {prayer_group['daily_focus']}\""
        )
        print("-" * 50)
        time.sleep(0.5)  # Short pause to simulate network transmission speed

    print("\n" + "=" * 60)
    print("  BROADCAST COMPLETE: Total Server Cost to Infrastructure: $0.00   ")
    print("=" * 60)


if __name__ == "__main__":
    simulate_global_broadcast()