

import base64
import httpx

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import urllib.parse

# Lanjutkan eksekusi kode
def encrypt_url(url, key):
    # Pastikan kunci adalah 16-byte
    key = key.encode('utf-8')
    cipher = AES.new(key, AES.MODE_ECB)

    # Pad URL menggunakan PKCS7
    padded_url = pad(url.encode('utf-8'), AES.block_size)

    # Enkripsi data
    encrypted = cipher.encrypt(padded_url)

    # Encode hasil enkripsi ke Base64 URL-safe
    encrypted_base64 = base64.urlsafe_b64encode(encrypted).decode('utf-8')
    return encrypted_base64

# API Keys
streamhg_api_key = "2426evezy9bm5xz0uzzy"
vinovo_api_key = "8b857a827319ed70f22e4d0668853f"
bigwarp_api_key = "1185roh927m637ogi3lv"
abstream_api_key = "23vj7x7uk12znfyaxc"
doodstream_api_key = "219725bbkborbourrp2cd4"
easyvidplay_api_key = "1a9f2e28183ebfe2f5551066"
turbostream_api_key = "98a5744ffbd3c2a63e0f61a37b3661f0f73b16b281da8fda8ade989dd93e76fe"

voesx_api_key = "Wr7fjmWTBp6EY0XGYJZwleaMJiJ2cuf21c3UvSpDd7GtPLAVnQTGiY9RNtwCyCbK"

key = "mysecretkey12345"  # Kunci AES untuk enkripsi



streamhg_api_endpoint = "https://streamhgapi.com/api/upload/url"
vinovo_api_endpoint  = "https://api.vinovo.si/api/upload/url"
bigwarp_api_endpoint  = "https://bigwarp.io/api/upload/url"
abstream_api_endpoint  = "https://abstream.to/api/upload/url"
doodstream_api_endpoint  = "https://doodapi.co/api/upload/url"
easyvidplay_api_endpoint = "https://easyvidplay.com/api/v1/video/advance-upload"
turbostream_api_endpoint  = "https://turbostream.tv/api/remote_upload.php"

voesx_api_endpoint = "https://voe.sx/api/upload/url"


# Variabel untuk menghitung jumlah sukses
success_count = 0



# Read URLs from output.txt
try:
    with open('output_link.txt', 'r') as file:
        urls = file.readlines()
        urls = [url.strip() for url in urls if url.strip()]  # Remove empty lines and whitespace

    total_urls = len(urls)  # Total link yang akan diproses

    # Encrypt each URL and send GET requests to both APIs
    for index, url in enumerate(urls, start=1):
        # Enkripsi URL
        encrypted = encrypt_url(url, key)
        new_url = f"https://darenx-upbkafe.hf.space/ex/{encrypted}"

        print(f"**=> Processing {index} of {total_urls}...")  # Menampilkan progress

        try:
            # doodstream request
            response_doodstream= httpx.get(doodstream_api_endpoint, params={"key": doodstream_api_key, "url": new_url})
            if response_doodstream.status_code == 200:
                success_count += 1
            else:
                print(f"Failed doodstream: {url} - doodstream Response: {response_doodstream.status_code} - {response_doodstream.text}")
        except Exception as e:
            print(f"Error during Lulustream request for {new_url}: {e}")

        
        
        
        
        

        try:
            # vinovo request
            response_vinovo = httpx.get(vinovo_api_endpoint, params={"key": vinovo_api_key, "url": url})
            if response_vinovo.status_code == 200:
                success_count += 1
            else:
                print(f"Failed vinovo : {url} - Vinovo Response: {response_vinovo.status_code} - {response_vinovo.text}")
        except Exception as e:
            print(f"Error during Vinovo request for {url}: {e}")

        

        try:
            url_to_upload = f"{bigwarp_api_endpoint}?key={bigwarp_api_key}&url={new_url}"

            # bigwarp request
            response_bigwarp = httpx.get(url_to_upload)
            if response_bigwarp.status_code == 200:
                success_count += 1
            else:
                print(f"Failed bigwarp: {url} - bigwarp Response: {response_bigwarp.status_code} - {response_bigwarp.text}")
        except Exception as e:
            print(f"Error during bigwarp request for {url}: {e}")

        try:
            url_to_upload = f"{abstream_api_endpoint}?key={abstream_api_key}&url={new_url}"

            # abstream request
            response_abstream = httpx.get(url_to_upload)
            if response_abstream.status_code == 200:
                success_count += 1
            else:
                print(f"Failed abstream: {url} - response_abstream Response: {response_abstream.status_code} - {response_abstream.text}")
        except Exception as e:
            print(f"Error during response_abstream request for {url}: {e}")

        #try:
        #    headers = {
        #       "Authorization": f"Bearer {turbostream_api_key}",
        #        "Content-Type": "application/json"
        #    }

        #    payload = {
        #        "url": url  # gunakan original URL bukan encrypted
        #    }

        #    response_turbostream = httpx.post(turbostream_api_endpoint, headers=headers, json=payload)
        #    if response_turbostream.status_code == 200:
        #        success_count += 1
        #    else:
        #        print(f"Failed turbostream: {url} - Turbostream Response: {response_turbostream.status_code} - {response_turbostream.text}")
        #except Exception as e:
        #    print(f"Error during Turbostream request for {url}: {e}")

       
        try:
            # encode URL untuk jaga-jaga (opsional, tergantung API)
            encoded_url = urllib.parse.quote(url, safe=':/?&=%')  # biar format URL tetap valid
            payload = {
                "url": encoded_url
               
            }
    
            headers = {
                "accept": "application/json",
                "api-token": easyvidplay_api_key,
                "Content-Type": "application/json"
            }
    
            response_easyvidplay = httpx.post(easyvidplay_api_endpoint, json=payload, headers=headers)
            if response_easyvidplay.status_code == 200:
                success_count += 1
            else:
                print(f"Status: {response_easyvidplay.status_code} - {response_easyvidplay.text} - {url} ")
    
        except Exception as e:
            print(f"Error during easyvidplay request for {url}: {e}")
        

        print(f"==>  {index} of {total_urls} SUCCESS UPLOAD KE DropLOAD & Lulustream  <=====")

    # Tampilkan total jumlah sukses
    print("\n=========================================")
    print(f"Total Successful Uploads: {success_count}")
    print("=========================================")

except FileNotFoundError:
    print("The file 'output_link.txt' was not found. Please ensure it exists in the same directory.")
