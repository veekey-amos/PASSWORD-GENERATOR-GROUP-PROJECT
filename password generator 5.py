ny_frame = Frame(root, bg="midnightblue")
ny_frame.pack(pady=20)

ny_button = Button(ny_frame, text="Generate unique password", command=new_rand, bg="black", fg="white")
ny_button.grid(row=0, column=0, padx=10)
