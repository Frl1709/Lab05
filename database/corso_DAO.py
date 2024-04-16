# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import get_connection
from model.corso import Corso as c
from model.studente import Studente as s


def get_corsi():
    cnx = get_connection()
    cursor = cnx.cursor(dictionary=True)
    query = """SELECT *
        FROM corso"""

    cursor.execute(query)
    result = []
    for row in cursor:
        result.append(c(row["codins"],
                        row["crediti"],
                        row["nome"],
                        row["pd"]))
    cursor.close()
    cnx.close()
    return result


def get_studenti_corso(cod):
    cnx = get_connection()
    cursor = cnx.cursor(dictionary=True)
    query = """SELECT matricola
        FROM iscrizione
        WHERE codins = %s """

    cursor.execute(query, (cod,))
    result = cursor.fetchall()
    studenti = []
    if result:
        matricole = ', '.join(str(row['matricola']) for row in result)
        query = f"""SELECT *
            FROM studente
            WHERE matricola IN ({matricole})"""

        cursor.execute(query)
        for r in cursor:
            studenti.append(s(r["matricola"],
                              r["cognome"],
                              r["nome"],
                              r["CDS"]))
    else:
        print("Nessuna matricola trovata")
    cursor.close()
    cnx.close()
    return studenti


def create_iscrizione(matricola, codins):
    cnx = get_connection()
    cursor = cnx.cursor(dictionary=True)
    query = """INSERT INTO iscrizione (matricola, codins)
        VALUES (%s, %s)"""
    cursor.execute(query, (matricola, codins))
    cnx.commit()
    cursor.close()
    cnx.close()
    return matricola, codins
