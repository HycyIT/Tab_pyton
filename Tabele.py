accept_names = ['arkadiusz', 'wiola', 'antek', 'piotr', 'adam']

def accept():
    names = input("Podaj imie : ").lower()

    if names in accept_names:
        print("Masz dostęp")
    else:
        print("Brak dostępu")
          
accept()
