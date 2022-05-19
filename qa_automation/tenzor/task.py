from pages import Page
from locators.locators import YandexPageLocators, YandexImagesLocators

url = 'https://yandex.ru/'

class TestTenzorTask:
	def test1(self, browser):
		page = Page(browser, url)
		page.open(url)
		assert page.is_element_present(YandexPageLocators.SEARCH_FIELD), 'Поле поиска не найдено'

		page.click(YandexPageLocators.SEARCH_FIELD)
		page.type_text(YandexPageLocators.SEARCH_FIELD, 'Тензор')
		assert page.is_element_present(YandexPageLocators.SEARCH_SUGGESTIONS), 'Предложения поиска не найдены'

		page.check_search_list()
		page.press_enter(YandexPageLocators.SEARCH_FIELD)
		page.wait_for_element_present(YandexPageLocators.SEARCH_RESULT)
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
		assert popular_text == search_text
