import os
import requests
import time

def set_output(file_path, key, value):
    with open(file_path, 'a') as file:
        print(f'{key}={value}', file=file)
        
def ping_url(url, delay, max_trials):
    trials = 0
    
    while trials < max_trials:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Website {url} is up and running")
                return True
            
        except requests.ConnectionError:
            print(f"Website {url} is unreachable. Retrying in {delay} seconds...")
            time.sleep(delay)
            trials += 1
            
        except requests.exceptions.MissingSchema:
            print(f"Invalid URL: {url}. Make sure the URL has a valid schema (e.g. http:// or https://)")
            return False
        
    return False

def run():
    website_url = os.getenv('INPUT_WEBSITE_URL')
    delay = int(os.getenv('INPUT_DELAY'))
    max_trials = int(os.getenv('INPUT_MAX_TRIALS'))
    
    website_reachable = ping_url(website_url, delay, max_trials)
    
    set_output(os.getenv("GITHUB_OUTPUT"), "website_reachable", str(website_reachable))
    
    if not website_reachable:
        raise Exception(f"Website {website_url} is unreachable after {max_trials} trials")
    
    print(f"Successfully pinged {website_url} after {max_trials} trials")
    
if __name__ == '__main__':
    run()