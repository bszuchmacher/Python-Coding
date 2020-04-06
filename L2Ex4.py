def namechecker(list_of_names):
    for list_of_names in list_of_names:
        yield list_of_names.split()[0]


print(list(namechecker(["Michael Jordan", "Bob Rasta Marley", "Yaakov Shwekey", "Chacham-Ovadia Yosef Shlita"])))