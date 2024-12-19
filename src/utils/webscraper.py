from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import requests

def download_image(url, save_dir, file_name):
    """
    Download an image from Zooniverse webpage.

    Args:
    url (str): The URL of the webpage.
    save_dir (str): The directory to save the image.
    file_name (str): The name of the image file.
    """

    # Check if save_dir exists, if not create it
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    # Specify the path to the web driver executable
    driver_path = '/opt/homebrew/bin/chromedriver'
    
    # Initialize the Chrome web driver
    try:
        service = Service(driver_path)
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run Chrome in headless mode (without opening a window)
        driver = webdriver.Chrome(service=service, options=options)
        print('Webdriver Prepped...')

        # Open the URL in the browser
        driver.get(url)
        print('Webpage Opened...')
        
        # Find the image element by XPath
        img_element = driver.find_element(By.XPATH,"//img[contains(@class,'subject pan-active')]")
        
        # Get the source URL of the image
        img_url = img_element.get_attribute('src')

        # Download the image
        image_filename = file_name + '.png'
        save_path = os.path.join(save_dir, image_filename)
        response = requests.get(img_url)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)
            print("Image downloaded successfully.")
        else:
            print("Failed to download image.")
    except Exception as e:
            print(f"An error occurred: {e}")
    finally:
        # Ensure the browser always quits
         driver.quit()