documents = [
  {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
  {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
  {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'},
  {'type': 'passport', 'number': '101'}
]

def print_documents_holders(document_list):
  print('Список владельцев документов:')
  try:
    for document in document_list:
      print(f'{document["name"]}')
  except KeyError as e:
    print(f'Ошибка "{e.__class__.__name__}": У документа № {document["number"]} не указан владелец')


print_documents_holders(documents)

# задание из лекции по функциям было сокращено (чтобы не отвлекало внимания)
# в список документов добавлен документ без  ключа 'name' для проверки KeyError
# задание из лекции по функциям: https://repl.it/@Liu_lang/HomeWork211