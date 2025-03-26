import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import pyperclip

def grabnwatch_process_links(links):
    results = []
    
    # Setup Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Inisialisasi driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    total_links = len(links)  # Total jumlah link yang akan diproses

    for index, link in enumerate(links):
        print(f"Processing {index + 1} dari {total_links}: {link}")  # Menampilkan proses
        driver.get('https://grabnwatch.com/')
        
        # Tunggu hingga pesan "Checking your browser" hilang
        try:
            WebDriverWait(driver, 20).until(
                EC.invisibility_of_element_located((By.ID, 'checkingMessage'))
            )
            
            # Tunggu hingga elemen input tersedia
            input_box = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.NAME, 'video_url'))
            )
            input_box.clear()
            input_box.send_keys(link)

            # Klik tombol grab
            grab_button = driver.find_element(By.ID, 'submitBtn')
            grab_button.click()
            time.sleep(5)  # Tunggu beberapa detik untuk mendapatkan hasil

            # Ambil link download
            try:
                download_link = driver.find_element(By.CLASS_NAME, 'btn-secondary').get_attribute('href')
                print(download_link)
                results.append(download_link)
            except Exception as e:
                print(f"Error: Download link not found for link: {link}. Error: {e}")

        except Exception as e:
            print(f"Error: Unable to process link: {link}. Error: {e}")

    driver.quit()

    return results

def process_links():
    links = text_input.get("1.0", tk.END).strip().split('\n')
    results = grabnwatch_process_links(links)
    
    # Tampilkan hasil di textarea hasil
    text_output.delete("1.0", tk.END)  # Kosongkan textarea hasil
    for result in results:
        text_output.insert(tk.END, result + "\n")

def copy_to_clipboard():
    output_text = text_output.get("1.0", tk.END).strip()
    if output_text:
        pyperclip.copy(output_text)
        messagebox.showinfo("Info", "Hasil berhasil disalin ke clipboard!")
    else:
        messagebox.showwarning("Warning", "Tidak ada hasil untuk disalin.")

# Setup GUI
root = tk.Tk()
root.title("Grab and Watch Links")
root.geometry("900x600")

# Input Textarea
text_input = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=10)
text_input.pack(pady=10)

# Process Button
process_button = tk.Button(root, text="Proses", command=process_links)
process_button.pack(pady=5)

# Output Textarea
text_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=10)
text_output.pack(pady=10)

# Copy Button
copy_button = tk.Button(root, text="Copy Hasil", command=copy_to_clipboard)
copy_button.pack(pady=5)

# Run the application
root.mainloop()
