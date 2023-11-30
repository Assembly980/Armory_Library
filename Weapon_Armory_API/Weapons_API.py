from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from contextlib import closing
import random

app = Flask(__name__)
CORS(app)

@app.route("/")
def Home():
    return jsonify({"status": "online"})

#Connect to SQLite
def DBConnection():
    #file path to the database
    conn = sqlite3.connect("Database/Weapons.db")
    return conn

#Request value of all swords
def GetAllSwordsFromDB():
    
    conn = DBConnection()
    cursor = conn.cursor()
    cursor.execute('SELECT WeaponRarity, WeaponName, Description, Picture FROM Weapon')
    swords = [{'WeaponRarity': WeaponRarity, 'WeaponName': WeaponName, 'Description': Description, 'Picture': Picture} for WeaponName, WeaponRarity, Description, Picture in cursor.fetchall()]

    return swords

#Request value of individual sword
def GetSwordFromDB(WeaponName):
    
    conn = DBConnection()
    cursor = conn.cursor()
    cursor.execute('SELECT WeaponRarity, WeaponName, Description, Picture FROM Weapon WHERE WeaponName = ?', (WeaponName,))
    RequestedSword = cursor.fetchone()

    return RequestedSword

def GetRandomSwordFromDB():

    randomNum = random.randint(1, 28)
    
    conn = DBConnection()
    cursor = conn.cursor()
    cursor.execute('SELECT WeaponRarity, WeaponName, Description, Picture FROM Weapon Where ID = ?', (randomNum,))
    RandomSword = cursor.fetchone()

    return RandomSword

#returns all swords in database
@app.route('/api/swords', methods=['GET'])
def GetAllSwords():
    swords = GetAllSwordsFromDB()
    return jsonify(swords)

#returns specified sword by name
@app.route('/api/swords/<WeaponName>', methods=['GET'])
def GetRequestedSword(WeaponName):
    sword = GetSwordFromDB(WeaponName)

    if sword:
        return jsonify({'WeaponRarity': sword[0], 'WeaponName': sword[1], 'Description':sword[2], 'Picture': sword[3]})
    else:
        return jsonify(message='Sword not found! Its dangerous to go alone, take this wooden sword!'), 404

#returns a random weapon
@app.route('/api/swords/random', methods=['GET'])
def GetRandomSword():
    sword = GetRandomSwordFromDB()
    return jsonify({'WeaponRarity': sword[0], 'WeaponName': sword[1], 'Description':sword[2], 'Picture': sword[3]})

if __name__ == '__main__':
    app.run(debug=True)
