def read_reverse_write(input_file, output_file):
    # Read the entire file as bytes
    with open(input_file, 'rb') as f:
        data = f.read()

    # Reverse the byte order
    reversed_data = data[::-1]

    # Write the reversed data to the new file
    with open(output_file, 'wb') as f:
        f.write(reversed_data)

    print(f"Reversed data has been written to {output_file}")

# Example usage
if __name__ == "__main__":
    input_file = 'chall.jpg'
    output_file = 'test_output.bin'
    read_reverse_write(input_file, output_file)
