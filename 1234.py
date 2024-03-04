lista_gosci1 = {
                    ('Andrzej i Teresa'),
                    ('Krystyna i Andrzej'),
                    ('Józef i Gabriela'),
                    ('Małgorzata i Jacek'),
                    ('Stanisława i Stanisław')
            }
lista_gosci2 = {
                    ('Arkadiusz i Sylwia'),
                    ('Piotr i Marzena'),
                    ('Rafał i Malwina'),
                    ('Kamil i Wiola'),
                    ('Damian i Anna')
                }

lista_gosci_all = lista_gosci1 | lista_gosci2
print(lista_gosci_all)
