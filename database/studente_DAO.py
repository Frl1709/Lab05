# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import get_connection
from model.studente import Studente as s
from model.corso import Corso as c


def get_studente():
    cnx = get_connection()
    cursor = cnx.cursor(dictionary=True)
    query = """SELECT *
        FROM studente"""

    cursor.execute(query)
    result = []
    for row in cursor:
        result.append(s(row["matricola"],
                        row["cognome"],
                        row["nome"],
                        row["CDS"]))
    cursor.close()
    cnx.close()
    return result


def get_studente_matricola(matricola):
    cnx = get_connection()
    cursor = cnx.cursor(dictionary=True)
    query = """SELECT *
        FROM studente
        WHERE matricola = %s"""
    cursor.execute(query, (matricola,))
    studente = cursor.fetchone()
    cursor.close()
    cnx.close()
    return studente['nome'], studente['cognome']


def get_corsi_iscritti(matricola):
    cnx = get_connection()
    cursor = cnx.cursor(dictionary=True)
    query = """SELECT *
        FROM iscrizione
        WHERE matricola = %s """
    cursor.execute(query, (str(matricola),))
    corsi = cursor.fetchall()
    # I CORSI LI PRENDO CORRETTAMENTE
    result = []
    if corsi:
        codici = ','.join(str(row['codins']) for row in corsi)
        # LA STRINGA DEI CODICI è CREATA BENE
        for cc in codici.split(","):
            query = f"""SELECT *
                FROM corso
                WHERE codins = %s """
            cursor.execute(query, (cc,))
            for row in cursor:
                result.append(c(row["codins"],
                                row["crediti"],
                                row["nome"],
                                row["pd"]))
    cursor.close()
    cnx.close()
    return result
