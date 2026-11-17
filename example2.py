rooms={
    "Math":"A101",
    "Physics":"B206",
    "English":"C310",
    "History":"ABC01"
}
print("Physics" in rooms)
print("Chemistry" in rooms)
print(rooms.get("History"))
print(rooms.get("History","not found"))
def find_room(rooms, subject):
    return rooms.get(subject, "not found")

assert find_room(rooms, "Math") == "A101"
assert find_room(rooms, "History") == "ABC01"
assert find_room(rooms, "math") == "not found"