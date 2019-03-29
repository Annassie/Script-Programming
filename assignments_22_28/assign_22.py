# -*- coding: UTF-8 -*-
def speeding_ticket(speed,limit):
    if speed >= 70:
        return (500, True)
    elif speed <= limit:
        return (0, False)
    else:
        return (100, False)


print(speeding_ticket(50, 50)) #No fine. Prints: (0, False)
print(speeding_ticket(60, 50)) #100€ fine, doesn't lose license. Prints: (100, False)
print(speeding_ticket(70, 50)) #500€ fine, loses license. Prints: (500, True)
print(speeding_ticket(100, 50)) #500€ fine, loses license. Prints: (500, True)

