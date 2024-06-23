from PIL import Image

def convert_to_grayscale(image_path, output_path):
  """Converts a JPEG image to grayscale and saves it.

  Args:
    image_path: Path to the input JPEG image.
    output_path: Path to save the grayscale image.
  """
  img = Image.open(image_path).convert('L')  # Convert to grayscale mode 'L'
  img.save(output_path)

# Example usage
image_path ="C:\Users\Dell\Desktop\multimedia\20191003_113355.jpg"
output_path = "C:\Users\Dell\Desktop\multimedia"


convert_to_grayscale(image_path, output_path)

