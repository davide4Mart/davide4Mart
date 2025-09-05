dictLista = {}

while True:
    
    print(" --- LISTA DELLA SPESA --- ")
    print(" 1. AGGIUNGI PRODOTTO")
    print(" 2. RIMUOVI PRODOTTO")
    print(" 3. MOSTRA LISTA")
    print(" 4. SEGNA COME COMPRATO")
    print(" 5. ESCI")
    
    scelta = input("Scelta : ")

    if scelta == '1':

        print("Aggiungi prodotto")
        name = input("Nome prodotto : ")
        quantità = int(input("Quantità prodotto : "))
        
        if name in dictLista:
            print("Prodotto già esistente in lista")
            
            while True:
                update = input("Seleziona 1 per sommare, seleziona 2 per sovrascrivere : ")
                if update == '1':
                    quantità += dictLista[name]['quantità']
                    dictLista.update({name: {'quantità': quantità, 'comprato': False}})
                    print(name + ' sovrascritto in lista con nuova quantità sommata ' + str(quantità))
                    break
                elif update == '2':
                    dictLista.update({name: {'quantità': quantità, 'comprato': False}})
                    print(name + ' sovrascritto in lista con nuova quantità ' + str(quantità))
                    break
                else:
                    print("scelta non valida")
        else:
            dictLista.update({name: {'quantità': quantità, 'comprato': False}})    

    elif scelta == '2':

        print("Rimuovi prodotto")
        
        if dictLista:
            name = input("Che prodotto vuoi eliminare? : ")
            if name in dictLista:
                del dictLista[name]
            else:
                print("Prodotto non presente")
        else:
            print("Lista spesa vuota")

    elif scelta == '3':

        if dictLista:
            for name in dictLista:
                dettaglio = dictLista[name]
                if dettaglio['comprato']:
                    compratoPrint = "Si"
                else:
                    compratoPrint = "No"
                print(name + ' | ' + ' quantità : ' +str(dettaglio['quantità']) + ' | comprato : ' + compratoPrint)
        else:
            print("Lista spesa vuota")

    elif scelta == '4':

        if dictLista:
            name = input("Che prodotto hai comprato? : ")
            if name in dictLista:
                dictLista[name]['comprato'] = True
                print("Prodotto " + name + " comprato")
            else:
                print("Prodotto non presente")
        else:
            print("Lista spesa vuota")

    elif scelta == '5':

        print("Arrivederci")
        break

    else:
        
        print("Scelta non valida")
