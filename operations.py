def read_file(file_path):
    print("read")
    with open(f"{file_path}.txt", "r") as file:
        lines = file.readlines()
        numbers = [int(line.strip()) for line in lines]
        numbers.sort()
        return numbers

def write_file(numbers, output_name):
    print("write")
    with open(f"{output_name}.txt", "w") as file:
        formatted_numbers = [f"{number}\n" for number in numbers]
        file.writelines(formatted_numbers)


