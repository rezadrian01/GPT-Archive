from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from json import dumps

from bs4 import BeautifulSoup

def scrape(url, timeout = 1000, headless = False):
  """
    input: 
      url: url of the conversation
      timeout: time to wait until the page is loaded
    output:
      user_chat: list of user chat
      assistant_chat: list of assistant chat
  """
  # Headless browser
  options = webdriver.ChromeOptions()
  options.add_argument('--headless')

  driver = webdriver.Chrome() if not headless else webdriver.Chrome(options = options)

  # driver = webdriver.Chrome(options = options)

  driver.get(url)
  try:
    # Wait until chat elements has been loaded
    WebDriverWait(driver, timeout).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-message-author-role="user"]'))
    )
    print("Page loaded")
  except:
    print("Timeout")
  
  html = driver.page_source
  soup = BeautifulSoup(html, 'html.parser')

  # Get all chat elements with user and assistant roles
  users_chat_elements = soup.find_all('div', attrs={'data-message-author-role': 'user'})
  assistant_chat_elements = soup.find_all('div', attrs={'data-message-author-role': 'assistant'})

  # Close the browser
  driver.quit()

  user_chat = []
  assistant_chat = []

  for chat in users_chat_elements:
    user_chat.append(chat.get_text())
  
  for chat in assistant_chat_elements:
    assistant_chat.append(chat.get_text())
  
  return user_chat, assistant_chat

# url = "https://chatgpt.com/share/67b560a2-b364-8010-83ce-fb50f8ce0151"
# url = "https://chatgpt.com/share/67b57980-4f48-8010-95df-de4b0da848d3"

# user_chat, assitant_chat = scrape(url)

# print(f"User chat: (total: {len(user_chat)})")
# for chat in user_chat:
#   # print(chat)
#   pass

# print(f"Assistant chat: (total: {len(assitant_chat)})")
# for chat in assitant_chat:
#   # print(chat)
#   pass

# result = []
# for i in range(len(user_chat)):
#   result.append({"role": "user", "text": user_chat[i]})
#   if i < len(assitant_chat):
#     result.append({"role": "assistant", "text": assitant_chat[i]})
  
# print(dumps(result, ensure_ascii=False))
