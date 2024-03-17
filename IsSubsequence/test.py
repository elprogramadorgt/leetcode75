import random
import string

def generate_test_data():
    s_length = 100
    t_length = 10000

    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(s_length))
    t = ''.join(random.choice(string.ascii_lowercase) for _ in range(t_length))

    return s, t

def write_to_file(file_path, s, t):
    with open(file_path, 'w') as file:
        file.write(f"s = \"{s}\"\n")
        file.write(f"t = \"{t}\"\n")

if __name__ == "__main__":
    file_path = "testing_data.txt"

    s, t = generate_test_data()
    write_to_file(file_path, s, t)

    print(f"Testing data generated and saved to {file_path}.\n")
    print(f"s = \"{s}\"\n")
    print(f"t = \"{t}\"\n")