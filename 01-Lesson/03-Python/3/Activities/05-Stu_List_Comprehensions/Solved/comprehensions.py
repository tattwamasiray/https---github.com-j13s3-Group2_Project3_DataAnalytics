names = []
for _ in range(1):
    name = input("Please enter the name of someone you know. ")
    names.append(name)

lowercased = [name.lower() for name in names]
print(lowercased)
title_cased = [name.title() for name in lowercased]
print(title_cased)
invitations = [
    f"Dear {name}, please come to the wedding this Saturday!"]
    # for name in title_cased]

# for invitation in invitations:
#     print(invitation)
