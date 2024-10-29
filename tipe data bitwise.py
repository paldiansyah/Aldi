bitwise = "mahasiswa"
print (bitwise)
# Mendefinisikan dua variabel
a = 10  # (biner: 1010)
b = 4   # (biner: 0100)

# Menggunakan operator bitwise
bitwise_and = a & b        # AND
bitwise_or = a | b         # OR
bitwise_xor = a ^ b        # XOR
bitwise_not = ~a           # NOT
bitwise_left_shift = a << 1  # Left Shift
bitwise_right_shift = a >> 1 # Right Shift

print("AND:", bitwise_and)              # 0
print("OR:", bitwise_or)                # 14
print("XOR:", bitwise_xor)              # 14
print("NOT:", bitwise_not)              # -11
print