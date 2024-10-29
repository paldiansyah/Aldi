logika = "saya suka pengurangan,saya suka makan"
print (logika)
# Mendefinisikan dua variabel boolean
is_raining = True
is_weekend = False

# Menggunakan operator logika AND
can_go_outside = not is_raining and is_weekend
print("Bisa keluar rumah:", can_go_outside)  # False

# Menggunakan operator logika OR
stay_home = is_raining or not is_weekend
print("Tetap di rumah:", stay_home)