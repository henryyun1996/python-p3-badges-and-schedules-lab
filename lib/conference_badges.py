def badge_maker(name):
    message = (f"Hello, my name is {name}.")
    return message

def batch_badge_creator(names):
    badges = []
    for name in names:
        message = (f"Hello, my name is {name}.")
        badges.append(message)
    return(badges)

def assign_rooms(names):
    rooms = range(1,9)
    room_assignment = []
    for i, name in enumerate(names):
        if i < len(rooms):
            room = rooms[i]
            room_assignment.append(f"Hello, {name}! You'll be assigned to room {room}!")
        else:
            break
    return room_assignment

def printer(names):
    badges = batch_badge_creator(names)
    room_assignments = assign_rooms(names)
    for badge in badges:
        print(badge)
    for room_assignment in room_assignments:
        print(room_assignment)
