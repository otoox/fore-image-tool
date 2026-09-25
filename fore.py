from PIL import Image
from PIL import ExifTags

def main():
  # Ask the user for the image filename
  filename = input("Enter the image filename: ").strip()

  try:
    # Open the image file
    image = Image.open(filename)

    # Extract EXIF data
    exif_data = image.getexif()

    if not exif_data:
      print("No EXIF metadata found in this image.")
      return

    print(f"\nFound EXIF data for {filename}:\n")

    # Loop through and print out the readable tag names and values
    for tag_id, value in exif_data.items():
      tag = ExifTags.TAGS.get(tag_id, tag_id)
      print(f"{tag}: {value}")

  except FileNotFoundError:
    print(f"The file '{filename}' doesn't exist. Check the name and try again.")
  except Exception as e:
    print(f"Something went wrong: {e}")


if __name__ == "__main__":
  main()