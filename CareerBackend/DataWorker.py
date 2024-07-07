import sqlite3
import mysql.connector


def createTable():
    try:

        connection = mysql.connector.connect(
            host="mysql",
            user='user',
            password='1234',
            database='CareerFinder',
            port="3306"
        )

        cursor = connection.cursor()

        cursor.execute('CREATE TABLE `requests` (requestText VARCHAR(255), schedule VARCHAR(255), experience VARCHAR(255), found INT)')

        connection.commit()
        connection.close()

        return True
    except Exception as e:
        print(e)
        return e



def createRecord(name, sch, exp, found):

    if name == '':
        return 

    found = int(found)

    try:
        connection = mysql.connector.connect(
            host="mysql",
            user='user',
            password='1234',
            database='CareerFinder',
            port="3306"
        )

        cursor = connection.cursor()

        cursor.execute("INSERT INTO requests (requestText, schedule, experience, found) VALUES (%s, %s, %s, %s)", (name, sch, exp, found))

        connection.commit()
        connection.close()

        return True
    except Exception as e:
        print(e)
        return e


def getMost():
    try:
        connection = mysql.connector.connect(
            host="mysql",
            user='user',
            password='1234',
            database='CareerFinder',
            port="3306"
        )

        cursor = connection.cursor()

        cursor.execute("SELECT * FROM requests ORDER BY found DESC")

        data = cursor.fetchall()[0]

        connection.close()

        s = str(data[0])+ ", "

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

        s+=str(sch) + ', '

        match data[2]:
            case 'noExperience':
                exp = 'Без опыта'
            case 'between1And3':
                exp = 'От года до 3'
            case 'between3And6':
                exp = 'От 3 до 6'
            case 'moreThan6':
                exp = 'Более 6'

        s+=str(exp)

        return [s, data[3]]
    except Exception as e:
        print(e)
        return e

def getAll():
    try:
        connection = mysql.connector.connect(
            host="mysql",
            user='user',
            password='1234',
            database='CareerFinder',
            port="3306"
        )

        cursor = connection.cursor()

        cursor.execute("SELECT * FROM requests ORDER BY found DESC")

        data = cursor.fetchall()

        connection.close()

        response = []

        for x in data:

            s = str(x[0])+ ", "

            match x[1]:
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

            s+=str(sch) + ', '

            match x[2]:
                case 'noExperience':
                    exp = 'Без опыта'
                case 'between1And3':
                    exp = 'От года до 3'
                case 'between3And6':
                    exp = 'От 3 до 6'
                case 'moreThan6':
                    exp = 'Более 6'

            s+=str(exp)

            l = [s, x[3]]

            response.append(l)

        return response
    except Exception as e:
        return e

print(getAll())