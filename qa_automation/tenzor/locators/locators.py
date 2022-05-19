from selenium.webdriver.common.by import By

class YandexPageLocators:
	SEARCH_FIELD = (By.ID, 'text')
	SEARCH_SUGGESTIONS = (By.CSS_SELECTOR, 'ul.mini-suggest__popup-content')
	SEARCH_RESULT = (By.CSS_SELECTOR, '#search-result[aria-label="Результаты поиска"]')


class YandexImagesLocators:
	IMAGES = (By.CSS_SELECTOR, 'a[data-id="images"]')
	POPULAR = (By.CSS_SELECTOR, 'div.PopularRequestList')
	POPULAR_FIRST = (By.CSS_SELECTOR, 'div.PopularRequestList-Item:nth-child(1)')
	SEARCH_FIELD = (By.CSS_SELECTOR, 'span.input .input__control')
	IMAGE_1 = (By.CSS_SELECTOR, 'div.serp-item:nth-child(1)')
	BUTTON_NEXT = (By.CSS_SELECTOR, '.CircleButton_type_next')
	BUTTON_PREV = (By.CSS_SELECTOR, '.CircleButton_type_prev')