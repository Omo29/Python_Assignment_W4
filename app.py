def process_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r', encoding='utf-8') as infile:
            content = infile.read()
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
        return
    except PermissionError:
        print(f"Error: No permission to read '{input_filename}'.")
        return
    except OSError as e:
        print(f"I/O error reading '{input_filename}': {e}")
        return

    # Example transformation: make content uppercase
    modified_content = content.upper()

    try:
        with open(output_filename, 'w', encoding='utf-8') as outfile:
            outfile.write(modified_content)
    except PermissionError:
        print(f"Error: No permission to write '{output_filename}'.")
    except OSError as e:
        print(f"I/O error writing '{output_filename}': {e}")
    else:
        print(f"Successfully wrote modified content to '{output_filename}'.")


def main():
    input_filename = input("Enter the input filename: ").strip()
    output_filename = input("Enter the output filename: ").strip()
    process_file(input_filename, output_filename)


if __name__ == "__main__":
    main()