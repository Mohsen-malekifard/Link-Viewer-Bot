import time
import requests

def check_url(url):
    try:
        start = time.time()
        r = requests.get(url, headers={"User-Agent":"SiteMonitor/1.0"})
        elapsed = time.time() - start
        print(f"[{time.strftime('%H:%M:%S')}] {url} - {r.status_code} - {round(elapsed,3)}s")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    url = "https://example.com"  # Your Link
    while True:
        check_url(url)
        time.sleep(1)  # 1 Second Space
