def new_rand():
    pw_entry.delete(0,END)
    pw_length = int(ny_entry.get())
    ny_password = "

    for_in range(pw_length):
        pw_password+=chr(randit(33,126))
    pw_entry.insert(0, ny_password)
