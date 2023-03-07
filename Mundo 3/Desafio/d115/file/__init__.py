

def isFile(name):
    try:
        a = open(name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def createFile(name):
    try:
        a = open(name, 'wt+')
        a.close()
    except:
        print('An error ocurred when it tried to create a file.')
    else:
        print(f'File {name} created sucessfully.')


def registerPerson(fileName):
    import utilidadesCeV.dado
    name = str(input('Person\'s name: '))
    age = utilidadesCeV.dado.readInt('Person\'s age: ')

    try:
        with open(fileName, "a") as output:
            output.write(f'{name};{age}\n')
    except:
        print('An error was found when it tried to write in the file.')
    else:
        print(f'{name} was registered sucessfully.')
    finally:
        output.close()


def readPeople(fileName):
    try:
        with open(fileName, "r") as output:
            for line in output:
                dataPerson = line.split(';')
                dataPerson[1] = dataPerson[1].replace('\n', '')
                print(f'{dataPerson[0]:<32}{dataPerson[1]:>3} anos')
    except:
        print('An error was found when it tried to open the file.')
    else:
        print('The data loading was done successfully.')
