# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import get_connection
from model.studente import Studente as s


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
    return result

