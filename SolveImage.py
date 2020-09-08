# libraries
from pprint import pprint
from PIL import ImageGrab
import pytesseract
from SudokuSolver import solve
import mouse
import keyboard

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
# Include the above line, if you don't have tesseract executable in your PATH
OFFSET = 5  # how much of the cell edge to cut off of the image


# gether the data for a board from a PIL.Image
def gather_grid_data(image):
    grid = []
    w, h = image.size
    cell_size = w / 9
    for r in range(9):
        row_data = []
        for c in range(9):
            x = c * cell_size
            y = r * cell_size
            temp_image = image.crop([x + OFFSET, y + OFFSET, x + cell_size - OFFSET, y + cell_size - OFFSET])
            # temp_image.save('debug/'+str(r)+str(c)+'.jpg', "JPEG")
            text = pytesseract.image_to_string(temp_image, lang='eng',
                                               config='--psm 10 --oem 3 -c tessedit_char_whitelist=123456789')
            if text == '':
                row_data.append(0)
            elif 1 <= int(text) <= 9:
                row_data.append(int(text))
            else:
                raise RuntimeError(
                    f"There was an error in data collection: row {r}, col {c} was incorrectly scanned as {text}")

        grid.append(row_data)
    return grid


# take a screenshot at the specified position
def screenshot(x1, y1, x2, y2):
    image = ImageGrab.grab().crop([x1, y1, x2, y2])
    # image.save("screenshot.jpg", "JPEG")
    return image


if __name__ == "__main__":
    print("move mouse to top left of sudoku puzzle and press y")
    keyboard.wait('y')
    textPos1 = mouse.get_position()
    print("move mouse to bottom right of sudoku puzzle and press y")
    keyboard.wait('y')
    textPos2 = mouse.get_position()

    image = screenshot(textPos1[0], textPos1[1], textPos2[0], textPos2[1])
    print("Processing image...")
    board = gather_grid_data(image)
    print("The scanned sudoku:")
    pprint(board)
    print("Solving...")
    if solve(board):
        print("Successfully solved!")
    else:
        print("Unable to find correct solution. The sudoku most likely scanned incorrectly")
    pprint(board)
