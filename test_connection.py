import pymysql

try:
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='Lionceaux999*',
        database='boutique'
    )
    print("Connexion réussie à la base boutique !")
    conn.close()
except Exception as e:
    print("Erreur de connexion :", e)
