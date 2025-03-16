from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from json import dumps

from bs4 import BeautifulSoup

def wait_for_text(driver, selector, timeout=10):
    WebDriverWait(driver, timeout).until(
        lambda d: d.find_element(By.CSS_SELECTOR, selector).text.strip() != ""
    )

def scrape(url, timeout = 1000, headless = False):
  """
    input: 
      url: url of the conversation
      timeout: time to wait until the page is loaded
    output:
      user_chat: list of user chat
      assistant_chat: list of assistant chat
      assistant_chat_raw: list of assistant chat (raw)
  """
  # Options browser
  options = webdriver.ChromeOptions()
  options.add_argument('--headless')
  options.add_argument('--no-sandbox')
  options.add_argument('--disable-gpu')

  driver = webdriver.Chrome() if not headless else webdriver.Chrome(options = options)

  driver.get(url)
  try:
    # Wait until chat elements has been loaded
    # WebDriverWait(driver, timeout).until(
    #     EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[data-message-author-role="user"]'))
    # )
    # WebDriverWait(driver, timeout).until(
    #     EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[data-message-author-role="assistant"]'))
    # )
    wait_for_text(driver, 'div[data-message-author-role="user"]', timeout=timeout)
    wait_for_text(driver, 'div[data-message-author-role="assistant"]', timeout=timeout)
    print("Page loaded")
  except:
    print("Timeout")
  
  html = driver.page_source
  soup = BeautifulSoup(html, 'html.parser')

  # Close the browser
  driver.quit()

  # Get all chat elements with user and assistant roles
  user_chat_elements = soup.find_all('div', attrs={'data-message-author-role': 'user'})
  assistant_chat_elements = soup.find_all('div', attrs={'data-message-author-role': 'assistant'})


  user_chat = [chat.get_text() for chat in user_chat_elements]
  assistant_chat = [str(chat) for chat in assistant_chat_elements]
  assistant_chat_raw = [chat.get_text() for chat in assistant_chat_elements]
  

  max_retries = 3
  retries = 0
  while retries < max_retries and not user_chat:
    print(f"Retrying... {retries + 1}")
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    user_chat_elements = soup.find_all('div', attrs={'data-message-author-role': 'user'})
    assistant_chat_elements = soup.find_all('div', attrs={'data-message-author-role': 'assistant'})
    user_chat = [chat.get_text() for chat in user_chat_elements]
    assistant_chat = [str(chat) for chat in assistant_chat_elements]
    assistant_chat_raw = [chat.get_text() for chat in assistant_chat_elements]
    retries += 1
  
  return user_chat, assistant_chat, assistant_chat_raw

if __name__ == '__main__':
  # url = "https://chatgpt.com/share/67b560a2-b364-8010-83ce-fb50f8ce0151"
  # url = "https://chatgpt.com/share/67b57980-4f48-8010-95df-de4b0da848d3"
  url = "https://chatgpt.com/share/67b5c1df-0848-8010-991c-261f15462e5a"

  user_chat, assitant_chat = scrape(url)

  print(f"User chat: (total: {len(user_chat)})")
  for chat in user_chat:
    # print(chat)
    pass

  print(f"Assistant chat: (total: {len(assitant_chat)})")
  for chat in assitant_chat:
    # print(chat)
    pass

  result = []
  for i in range(len(user_chat)):
    result.append({"role": "user", "text": user_chat[i]})
    if i < len(assitant_chat):
      result.append({"role": "assistant", "text": assitant_chat[i]})
    
  print(dumps(result, ensure_ascii=False))