def display_menuffgff :
     menu_dict = {
          '1': 'Apples',
          '2': 'Pears',
          '3': 'Bananas'
    }
      for items, values in menu_dict() .items () :
          print (items+"."+ values)
def main():
      display_menu()
