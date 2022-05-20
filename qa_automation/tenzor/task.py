import time
import pytest
from pages import Page
from locators.locators import YandexPageLocators, YandexImagesLocators


url = 'https://yandex.ru/'

class TestTenzorTask:

	#@pytest.mark.skip
	#@pytest.mark.xfail
	def test1(self, browser):
		page = Page(browser, url)
		page.open(url)
		assert page.is_element_present(YandexPageLocators.SEARCH_FIELD), 'Поле поиска не найдено'

		page.click(YandexPageLocators.SEARCH_FIELD)
		page.type_text(YandexPageLocators.SEARCH_FIELD, 'Тензор')
		assert page.is_element_present(YandexPageLocators.SEARCH_SUGGESTIONS), 'Предложения поиска не найдены'

		page.check_search_list()  # Проверяем, есть ли слово "тензор" в подсказках поиска
		page.press_enter(YandexPageLocators.SEARCH_FIELD)
		page.wait_for_element_present(YandexPageLocators.SEARCH_RESULT)
		assert page.is_element_present(YandexPageLocators.SEARCH_RESULT), 'Результатов поиска нет'

		href = page.check_search_result()
		assert href.__contains__('tensor.ru'), f'Неправильная ссылка на сайт Тензор в результатах поиска ({href})'

	def test2(self, browser):
		page = Page(browser, url)
		page.open(url)
		assert page.is_element_present(YandexImagesLocators.IMAGES), 'Ссылка на Яндекс картинки отсутствует'

		page.click(YandexImagesLocators.IMAGES)
		page.change_active_tab('Картинки')  # Здесь переключаемся на окно с картинками
		assert page.check_current_url().__contains__('yandex.ru/images/'), 'Переход на картинки не осуществлен. ' \
																			'Ссылка должна содержать текст ' \
																			'"yandex.ru/images"'

		page.click(YandexImagesLocators.POPULAR_FIRST)
		assert page.is_element_present(YandexImagesLocators.SEARCH_FIELD)

		popular_text = browser.find_element(*YandexImagesLocators.POPULAR_FIRST).text
		search_text = page.get_search_text()
		assert popular_text == search_text, f'Название категории "{popular_text}" ' \
											f'не совпадает с текстом в поле поиска "{search_text}"'

		page.click(YandexImagesLocators.IMAGE_1)
		im1_url = page.get_image_url()
		assert page.is_element_present(YandexImagesLocators.IMAGE_1), 'Первая картинка не открыта'

		browser_url = browser.current_url
		page.click(YandexImagesLocators.BUTTON_NEXT)
		page.wait_for_url_changes(browser_url)
		im2_url = page.get_image_url()
		assert im2_url != im1_url, 'Картинка не сменилась'

		browser_url = browser.current_url
		page.click(YandexImagesLocators.BUTTON_PREV)
		page.wait_for_url_changes(browser_url)
		im3_url = page.get_image_url()
		assert im3_url == im1_url, f'Ссылки на картинки должны совпадать: {im1_url}; {im2_url}'
