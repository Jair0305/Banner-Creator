import argparse
import os
from pyfiglet import Figlet

def generate_banner(text):
    fig = Figlet()
    banner = fig.renderText(text)
    return banner

def save_banner_to_file(banner, file_path):
    with open(file_path, 'w') as file:
        file.write(banner)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a banner to ASCII and save it to a file')
    parser.add_argument('texto', type=str, help='Text to convert to banner')
    args = parser.parse_args()
    banner_result = generate_banner(args.texto)
    script_name = os.path.splitext(os.path.basename(__file__))[0]
    file_name = "banner.txt"
    save_banner_to_file(banner_result, file_name)
    print(f"Banner generated and saved as {file_name}")
