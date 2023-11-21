from flask import Flask, jsonify
import sqlite3
from contextlib import closing

app= Flask(__name__)

#Connect to SQLite
def DBConnection():
    #file path to the database
    return sqlite3.connect('C:/Users/trevo/OneDrive/ServerSide/Weapons.db')

#Request value of all swords
def GetSwordsFromDB():
    with closing(DBConnection()) as connection, connection.cursor() as cursor:
        cursor.execute('SELECT WeaponName, WeaponRarity, Description, Picture FROM swords')
        swords = [{'WeaponName': WeaponName, 'WeaponRarity': WeaponRarity, 'Description': Description, 'Picture': Picture} for WeaponName, WeaponRarity, Description, Picture in cursor.fetchall()]

    return swords

#Request value of individual sword
def GetSwordFromDB(WeaponName):
    with closing(DBConnection()) as connection, connection.cursor() as cursor:
        cursor.execute('SELECT WeaponName, WeaponRarity, Description, Picture FROM swords WHERE WeaponName = ?', (WeaponName,))
        RequestedSword = cursor.fetchone()

    return RequestedSword

#returns all swords in database
@app.route('/api/swords', methods=['GET'])
def GetAllSwords():
    swords = GetSwordsFromDB()
    return jsonify(swords)

#returns specified sword by name
@app.route('/api/swords/<WeaponName>', methods=['GET'])
def GetRequestedSword(WeaponName):
    sword = GetSwordFromDB(WeaponName)

    if sword:
        return jsonify({'WeaponName': sword[0], 'WeaponRarity': sword[1], 'Description':sword[2], 'Picture': sword[3]})
    else:
        return jsonify(message='Sword not found! Its dangerous to go alone, take this wooden sword!'), 404
    
if __name__ == '__main__':
    app.run(debug=True)
    
