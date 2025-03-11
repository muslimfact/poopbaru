import requests
import re
import concurrent.futures

# Mengosongkan file output_link.txt
open('output_link.txt', 'w').close()

def get_video_link(url):
    try:
        video_id = url.split('/')[-1]
        api_urls = [
            f'https://api.poophd.com/player.php?id={video_id}'
        ]
        for api_url in api_urls:
            print(f"Fetching: {api_url}")
            headers = {
                'Referer': 'https://metrolagu.cam/',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
            }
            response = requests.get(api_url, headers=headers)
            
            print(f"Response from {api_url}")  # Debugging
            
            if response.status_code == 200 and 'player("' in response.text:
                match = re.search(r'player\("a",\s*".*?",\s*".*?",\s*"(https?://[^"]+)"', response.text)
                if match:
                    video_link = match.group(1)
                    return video_link

    except Exception as e:
        print(f"Error in get_video_link: {e}")
    return None


# Fungsi untuk mengikuti redirect
def follow_redirect(video_link):
    try:
        headers = {
            'accept': '*/*',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'priority': 'i',
            'range': 'bytes=0-',
            'referer': 'https://api.poophd.com/',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132")',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'video',
            'sec-fetch-mode': 'no-cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
        }

        session = requests.Session()
        response = session.get(video_link, headers=headers, allow_redirects=True)

        if response.history:
            print(f"Redirects: {[res.url for res in response.history]}")

        if response.status_code == 403:
            print("Diblokir! Coba cek header 'Location' secara manual.")
            redirect_url = response.headers.get('Location')
            return redirect_url if redirect_url else None

        return response.url

    except Exception as e:
        print(f"Error in follow_redirect: {e}")
    return None

# Membaca file link.txt
try:
    with open('link.txt', 'r') as file:
        links = file.readlines()
except Exception as e:
    print(f"Error reading link.txt: {e}")
    links = []

# Menyimpan hasil ke output_link.txt
try:
    total_links = len(links)
    with open('output_link.txt', 'w') as output_file:
        found_links = []
        for index, link in enumerate(links):
            link = link.strip()
            if link:
                print(f"Proses {index + 1} dari {total_links}")
                video_link = get_video_link(link)
                if video_link:
                    final_link = follow_redirect(video_link)
                    if final_link:
                        output_file.write(final_link + '\n')
                        print(f"{final_link}\n")
                        found_links.append(final_link)

    print(f'Jumlah link yang ditemukan: {len(found_links)}')
except Exception as e:
    print(f"Error writing to output_link.txt: {e}")
