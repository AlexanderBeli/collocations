#Цель - добавить список слов в словарь

#нужно перепроверить веденное слово - есть ли оно в словаре
# ответ да/нет
# нет - продолжаем процесс
# да - выдаем информацию, что оно есть в словаре
	#спрашиваем, какую категорию хочет добавить
	#проверяем категорию по abbreviation.txt и по наличию категории в словаре
		#Если категории нет в списке, выдать оповещение - "категории нет в списке, свяжитесь с разработчиком" и оборвать процесс
		#Если категория есть в списке, выдать оповещение "категория есть в списке" и "добавьте слова"/загружайте слова
		#Если категория есть в списке и есть в словаре - выдать информацию "Категория уже есть в словаре. Возможно слова, которые вы хотите добавить, уже находятся в словаре"
			#Сделать проверку, есть ли слова в словаре в данной категории
				#Если нет, то добавить

#нужно спросить откуда поступает база - вручную ввводим или из файла 

import json
import pickle
import re

#if __name__ == "__main__":

eng_dict = {}
file_source = 'source.txt'
dict_source = 'eng_dict.pickle'
type_source = 'abbreviation.txt'

posetive_answers = ('yes', 'y')
negative_answers = ('no', 'n')
first_message = "What do you want to do? Type the one of the next commands: show, add, change, delete or exit. "
first_answer_show = ('show', 's', 'sh', 'sho', 'show')
first_answer_add = ('add', 'ad', 'a')
first_answer_change = ('change', 'chang', 'chan', 'ch', 'c')
first_answer_delete = ('delete', 'delet', 'dele', 'del', 'de', 'd')
first_answer_exit = ('exit', 'exi', 'ex', 'e')
name_input = "Write the WORD: "
category_input = "Write the CATEGORY: "
middle_message = "We're checking that "
final_message = "There is no another option here. You may restart the program or connect to the developers. Goodbye! "
error_message = "There is no such relevant information in the dictionary. Please check what your wrote and try again. "
error_category_message = "There is no such category according to the word or collocations. "
result_message = "We've added it to the dictionary. "
del_suc_message = "We've removed it"
ch_suc_message = "We've changed it"
choice_message = "Please choose and write one of the next categories: word, meaning, collocations, categories, word's categories "
choice_answer_word = ('word', 'wor', 'wo', 'w')
choice_answer_meaning = ('meaning', 'meanin', 'meani', 'mean', 'mea', 'me','m')
choice_answer_collocations = ('collocations', 'collocation', 'collocatio','collocati', 'collocat', 'colloca', 'colloc', 'collo', 'coll', 'col', 'co', 'c')
choice_answer_category = ('category', 'categor', 'catego', 'categ', 'cate', 'cat', 'ca')
choice_answer_word_category = ("word's categories", "wc", "worcat", "words cat", "words category", "wcat", "wct")
#при запросе ввода информации указать: Если вы хотите выйти из режима/завершить напишите 'exit'

class Check:
	#__slots__ = ['item'] #Only 'item' attribute is allowed
	def __init__(self, stroke):
		self.stroke = stroke

		if not isinstance(stroke, str):
			print("It's not a string. Please check what you typed.")
			return None

	#проверка на корректность ввода слова/ слов
	def check_w(self, word):
		self.word = word
		#чтобы все буквы после первой были lowcase, чтобы не было спец.символов, цифр; была только латиница
		#две ситуации
		#передано ключевое слово
		#передан список
		if len(word.split(',')) == 1:
			if re.search(r'[^a-zA-Z]',word ):
			     print("'It's not the word. Please try again")
			else:
			     return 1

		else:
			word = word.replace(' ','').replace('↑','').replace(',','')

			if re.search(r'[^a-zA-Z]',word ):
			     print('The list of words or text consists of special characters or numbers. Please check the list or text and try again.')
			else:
			     return 1

	#проверяем слово на наличие в словаре
	def check_key_word(self, name, dict_data):
		self.name = name

		if self.name in dict_data.keys():
			print(f'{name} is in the dictionary')
		else:
			print(f'{name} is a new word')

	#проверяем тип слова на наличие в списке 
	def check_type(self, w_type):
		self.w_type = w_type
		with open(type_source, 'r', encoding='utf-8') as f:
			type_data = f.read()

		if w_type in type_data:
			return 1
		else:
			print("The category ", w_type, " doesn't exist. Please try again or check the categories. ")

	def check_collocations_in_category(self, name, category2):
		self.name = name
		category1 = 'adj'  #category of the word, e.g. adj, n...
		self.category2 = category2		

		if category2 in dict_data[name][category1]['collocations'].keys():
			return 1
		else:
			return 0
			
	#можно перепроверить введенные слова на их наличие
	#а можно преобразовать словарь в формат множества, тогда при добавлении будут просто добавляться новые слова, исключаем вероятность повторения
	#Object of type set is not JSON serializable
	#Стал использовать pickle 21.09.2023