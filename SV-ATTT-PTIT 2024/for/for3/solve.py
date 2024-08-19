def swap_hex_pairs(input_file, output_file):
    """
    Reads a binary file, swaps every two hex digits, and writes the result to a new file.
    
    :param input_file: Path to the input file with swapped hex bytes.
    :param output_file: Path to the output file where the corrected data will be saved.
    """
    try:
        # Open the input file in binary read mode
        with open(input_file, 'rb') as infile:
            # Read the entire file content
            data = infile.read()
        
        # Prepare a list to hold the corrected data
        corrected_data = bytearray()
        
        # Iterate over the data two bytes at a time
        for i in range(0, len(data), 2):
            # Read two bytes (one pair of swapped hex values)
            byte_pair = data[i:i+2]
            
            # Ensure we have exactly two bytes
            if len(byte_pair) == 2:
                # Swap the bytes and append to the corrected data
                corrected_data.extend(byte_pair[::-1])
            else:
                # If the data length is not a multiple of 2, just append the remaining byte
                corrected_data.extend(byte_pair)
        
        # Open the output file in binary write mode
        with open(output_file, 'wb') as outfile:
            # Write the corrected data
            outfile.write(corrected_data)
        
        print(f"Successfully swapped hex pairs and saved to {output_file}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_filename = 'file.png'
output_filename = 'output_corrected.png'

swap_hex_pairs(input_filename, output_filename)
