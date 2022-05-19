import re
from urllib.parse import unquote
from selenium.webdriver import Chrome
from selenium.common import exceptions
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


class Page:
	def __init__(self, browser: Chrome, url: str):
		self.browser = browser
		self.url = url
		browser.implicitly_wait(10)

	def open(self, url):
		self.browser.get(url)

	def click(self, obj):
		if self.is_element_present(obj):
			self.browser.find_element(*obj).click()
			return
		raise exceptions.NoSuchElementException

	def type_text(self, obj, text: str):
		if self.is_element_present(obj):
			self.browser.find_element(*obj).send_keys(text)

	def is_element_present(self, locator):
		try:
			self.browser.find_element(*locator)
		except exceptions.NoSuchElementException as ex:
			return False
		return True

	def wait_for_element_present(self, locator):
		try:
			WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(locator))
		except exceptions.TimeoutException:
			return False
		return True

	def check_search_list(self):
		while True:
			html = self.browser.page_source
			soup = BeautifulSoup(html, 'lxml')
			res = soup.select('li.mini-suggest__item')
			if len(res) >= 1:
				break
		for i in range(len(res)):
			if res[i].text == 'тензор':
				return True
		raise exceptions.ElementNotVisibleException('Ключевое слово "тензор" отсутствует в списке предложений поиска')

	def press_enter(self, obj):
		self.browser.find_element(*obj).send_keys(Keys.ENTER)

	def check_search_result(self):
		html = self.browser.page_source
		soup = BeautifulSoup(html, 'lxml')
		res = soup.find('ul', {'id': 'search-result', 'role': 'main'})
		item = res.find_all('a')[0]
		href: str = item.get('href')
		return href

	def change_active_tab(self, caption_re):
		windows = self.browser.window_handles
		for i in range(len(windows) - 1):
			if re.search(caption_re, self.browser.title) is None:
				self.browser.switch_to.window(windows[i + 1])

	def check_current_url(self):
		return self.browser.current_url

	def get_search_text(self):
		url = unquote(self.browser.current_url)
		text = re.search(r'text=([^&]+)', url).group()
		return text.split('=')[1]
