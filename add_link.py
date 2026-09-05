import json
import os

CONFIG_FILE = "config.json"

def load_config():
    if not os.path.exists(CONFIG_FILE):
        return {}
    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_config(data):
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    print(f"\n[+] Successfully saved to {CONFIG_FILE}!")

def main():
    print("=" * 50)
    print("   Flipkart Scraper - Add New Tracking Link")
    print("=" * 50)

    data = load_config()
    
    # 1. Select Category
    categories = list(data.keys())
    print("\nAvailable Categories:")
    for i, cat in enumerate(categories, 1):
        print(f"  {i}. {cat}")
    
    print("\nEnter the number of an existing category, or type a new category name (e.g., 'my_new_category/'):")
    cat_input = input("> ").strip()
    
    if cat_input.isdigit() and 1 <= int(cat_input) <= len(categories):
        category = categories[int(cat_input) - 1]
    else:
        category = cat_input
        if not category.endswith('/'):
            category += '/'
            
    if category not in data:
        data[category] = []
        print(f"[*] Created new category: {category}")
        
    # 2. Enter Filename
    print(f"\nEnter the filename to save results (e.g., 'my_tracking.txt'):")
    filename = input("> ").strip()
    if not filename.endswith('.txt'):
        filename += '.txt'
        
    # 3. Enter URL
    print("\nEnter the Flipkart search URL to track:")
    url = input("> ").strip()
    if not url.startswith("http"):
        print("[-] Invalid URL. Must start with http or https.")
        return
        
    # 4. Settings
    print("\nForce checkout for these products even if condition isn't met? (y/N):")
    force_val = input("> ").strip().lower()
    force = 1 if force_val == 'y' else 0
    
    print("\nScrape non-assured products as well? (y/N):")
    notassured_val = input("> ").strip().lower()
    notassured = True if notassured_val == 'y' else False
    
    # Build task object
    new_task = {
        "filename": filename,
        "force": force,
        "notassured": notassured,
        "url": url,
        "source_script": "manual_entry"
    }
    
    # Check if filename already exists in this category
    existing_index = next((i for i, task in enumerate(data[category]) if task['filename'] == filename), -1)
    
    if existing_index >= 0:
        print(f"\n[!] A tracking task with filename '{filename}' already exists in '{category}'.")
        print("Overwrite? (y/N):")
        if input("> ").strip().lower() == 'y':
            data[category][existing_index] = new_task
            print("[*] Overwritten existing task.")
        else:
            print("[-] Cancelled.")
            return
    else:
        data[category].append(new_task)
        print(f"[*] Added new task '{filename}' to '{category}'.")
        
    save_config(data)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[-] Cancelled.")
