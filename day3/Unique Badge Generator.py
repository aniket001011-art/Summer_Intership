all_badges = {"Speaker", "Organizer", "VIP", "Attendee"}
assigned_badges = {"Attendee", "Speaker"}
print("Here are the leftover--",all_badges-assigned_badges)
leftover = all_badges.difference(assigned_badges)
print(leftover)