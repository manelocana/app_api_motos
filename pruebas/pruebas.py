
# database con terminal



import pymysql
#from config.passw import passw



class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost', #ip
            user='root',
            password='croke',
            db='app_api_motos',
        )

        self.cursor = self.connection.cursor()
        # probamos la conexion, si no da error, esta ok (python pruebas/pruebas.py)
        print('Conectado a la DB')


    def select_moto(self, id):
        sql = 'SELECT id, marca, modelo FROM motos1  WHERE id = {}'.format(id)

        try:
            self.cursor.execute(sql)
            moto = self.cursor.fetchone()

            return{'Id': moto[0],
                   'Marca': moto[1],
                   'Modelo': moto[2]}
        except Exception as e:
            raise

    
    def select_all_motos(self):
        sql = 'SELECT * FROM motos1'

        try:
            self.cursor.execute(sql)
            motos = self.cursor.fetchall()

            for moto in motos:
                print('Id: ', moto[0])
                print('Marca: ', moto[1])
                print('Modelo: ', moto[2])
                print('________\n')
        except Exception as e:
            raise


    def update_moto(self, id, modelo):
        sql = "UPDATE motos1 SET modelo='{}' WHERE id = '{}'".format(modelo, id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise


    def close(self):
        self.connection.close()



database = Database()

database.select_moto(5)
database.update_moto(5,'modelo pepii')
database.select_moto(5)

database.close()



