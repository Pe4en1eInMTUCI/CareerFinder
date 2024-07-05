import sqlite3


def createTable():
    try:
        connection = sqlite3.connect('vacancies.db')
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS requests ('
                       'requestText TEXT NOT NULL,'
                       'schedule TEXT NOT NULL,'
                       'experience TEXT NOT NULL,'
                       'found INTEGER NOT NULL)')

        connection.commit()
        connection.close()

        return True
    except Exception as e:
        print(e)
        return False



def createRecord(name, sch, exp, found):

    found = int(found)

    try:
        connection = sqlite3.connect('vacancies.db')
        cursor = connection.cursor()

        cursor.execute("INSERT INTO requests (requestText, schedule, experience, found) VALUES (?, ?, ?, ?)", (name, sch, exp, found))

        connection.commit()
        connection.close()

        return True
    except Exception as e:
        print(e)
        return False


def getMost():
    try:
        connection = sqlite3.connect('vacancies.db')
        cursor = connection.cursor()

        data = cursor.execute("SELECT * FROM requests ORDER BY found ASC").fetchone()

        connection.commit()
        connection.close()

        s = data[0] + ", "

        match data[1]:
            case "None":
                sch = 'График: Не важно'
            case "fullDay":
                sch = 'График: Полный день'
            case "shift":
                sch = 'График: Сменный'
            case "flexible":
                sch = 'График: Гибкий'
            case "remote":
                sch = 'График: Удаленно'
            case "flyInFlyOut":
                sch = 'График: Вахта'

        s+=sch + ', '

        match data[2]:
            case 'noExperience':
                exp = 'Без опыта'
            case 'between1And3':
                exp = 'От года до 3'
            case 'between3And6':
                exp = 'От 3 до 6'
            case 'moreThan6':
                exp = 'Более 6'

        s+=exp

        return [s, data[3]]
    except Exception as e:
        print(e)
        return False
