from operations import read_file, write_file

numbers = read_file("random_numbers")
write_file(numbers, "output_numbers")