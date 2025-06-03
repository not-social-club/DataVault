# DataVault

A simple local inventory system that runs in the terminal (CMD), where you can manage categories, items, quantities, and locations.

> Designed for users with **no programming knowledge**, working through a `.exe` executable that runs in the Windows terminal.

---

## Features

- ✅ Create new inventory items
- ✅ Edit quantity, location, or remove items
- ✅ View inventory
- ✅ Export and import inventory in `.json` files
- ✅ Stores data locally on your computer

---

## How to Use

### **Executable Version (.exe)**

1. **Download the files:**
   - `DataVault.exe`
   - `data.json` (Required configuration file)

2. Place both files in the **same folder**.

3. **Double-click `DataVault.exe` to run.**  
   The program will open automatically in the terminal (CMD).

4. Follow the interactive menu on the screen.

### Required Files

- `data.json`: Configuration file with categories and locations. **Required.**
- `inventory.json`: Automatically created after adding the first items.

---

## **Running the Source Code (.py)**

### Requirements:

- Python installed [https://www.python.org/](https://www.python.org/)  
(Recommended Python 3.10 or higher)

### Install dependencies:

No external dependencies are required beyond standard Python.

### Run the program:

python app.py

### Possible Errors & Solutions

## Error 1
data.json not found	
# Cause
Missing file in the folder	
# Solution
Make sure data.json is in the same folder as the .exe.

## Error 2
Window closes immediately	
# Cause
Opened without terminal
# Solution
Open cmd, navigate to the folder, and run DataVault.exe to see error messages.

## Tips
You can edit data.json to add your own categories, items, and locations.

Always keep inventory.json in the same folder to maintain your inventory data.

### Important Note About "New Inventory"

- The **"New Inventory"** option is not for creating a new empty inventory file each time.
- After the first item is created, **this is the option used to add new items to the inventory.**
- The inventory is saved automatically in `inventory.json` and persists between sessions.

> **Note:** This user experience (UX) will be improved in future versions to make this process clearer and more intuitive.

Made by @fbreseghello
DataVault v1.0
