import os
import subprocess
import argparse

# --- CONFIGURATION ---
# IMPORTANT: Update this path to your Aseprite executable
# Examples:
# Windows: "C:\\Program Files\\Aseprite\\aseprite.exe"
# macOS: "/Applications/Aseprite.app/Contents/MacOS/aseprite"
# Linux: "aseprite" (if it's in your system's PATH)
ASEPRITE_PATH = "aseprite" 

def convert_assets(input_folder):
    """
    Converts all .ase and .aseprite files in the input folder to PNG spritesheets.
    """
    output_folder = os.path.join(input_folder, "spritesheets")

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created directory: {output_folder}")

    print(f"Scanning for .ase and .aseprite files in: {input_folder}")

    for filename in os.listdir(input_folder):
        if filename.endswith(".ase") or filename.endswith(".aseprite"):
            source_file = os.path.join(input_folder, filename)
            
            # Sanitize filename for output
            base_name = os.path.splitext(filename)[0].replace(" ", "-").lower()
            output_basename = os.path.join(output_folder, base_name)
            
            output_png = f"{output_basename}.png"
            output_json = f"{output_basename}.json"

            print(f"Converting: {filename} -> {os.path.basename(output_png)}")

            # Construct the Aseprite CLI command
            command = [
                ASEPRITE_PATH,
                "-b",  # Run in batch mode
                source_file,
                "--sheet", output_png,
                "--data", output_json,
                "--format", "json-array" # Format needed for easy parsing
            ]

            # Execute the command
            try:
                subprocess.run(command, check=True, capture_output=True, text=True)
            except FileNotFoundError:
                print("\n---")
                print(f"ERROR: Aseprite executable not found at '{ASEPRITE_PATH}'")
                print("Please update the ASEPRITE_PATH variable in this script.")
                print("---\n")
                return
            except subprocess.CalledProcessError as e:
                print(f"  ERROR converting {filename}:")
                print(f"  Aseprite output:\n{e.stderr}")


    print("\nConversion complete!")
    print(f"All spritesheets have been saved to: {output_folder}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert Aseprite files to PNG spritesheets and JSON data."
    )
    parser.add_argument(
        "input_folder",
        type=str,
        help="The path to the folder containing .aseprite files."
    )
    args = parser.parse_args()
    
    convert_assets(args.input_folder)
