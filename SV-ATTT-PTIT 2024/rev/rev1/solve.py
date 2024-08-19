def sub_401530():
    # Define the string and the list of values to XOR with
    Str = 'reverse'
    dword_403040 = [
        0x22, 0x31, 0x3F, 0x31, 0x31, 0x27, 0x23, 0x09,
        0x21, 0x46, 0x0B, 0x55, 0x07, 0x3A, 0x00, 0x30,
        0x18, 0x3A, 0x41, 0x0B, 0x56, 0x2D, 0x55, 0x00,
        0x55, 0x0F, 0x0A, 0x00, 0x00
    ]

    # Length of the string
    v1 = len(Str)
    
    # Generate the output
    output = []
    for i in range(26):  # Loop from 0 to 25 inclusive
        # XOR the value from dword_403040 with the corresponding character in Str
        value = dword_403040[i] ^ ord(Str[i % v1])
        
        # Convert to character if within printable ASCII range, otherwise to a placeholder
        if 32 <= value <= 126:
            output.append(chr(value))
        else:
            output.append(f'\\x{value:02X}')  # Use hex representation for non-printable characters
    
    # Write the result to a text file
    s = "".join(output)
    print(s)
# Call the function
sub_401530()
