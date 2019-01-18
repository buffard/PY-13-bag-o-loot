import sqlite3
import sys

# sys.argv is a list of the passed in args from the command line
print(sys.argv)

# def printArg():
#   print(sys.argv[1])

lootbag_db = '/Users/Buffard/workspace/NSS/back-end/exercises/BAG-OF-LOOT/lootbag.db'

def getChildren():
  with sqlite3.connect(lootbag_db) as conn:
    cursor = conn.cursor()
# we are able to use fetchall because we are using the cursor method
  cursor.execute('SELECT * FROM Children')
  children = cursor.fetchall()
  print(children)

def getChild(child):
  with sqlite3.connect(lootbag_db) as conn:
    cursor = conn.cursor()

  cursor.execute(f'''SELECT c.*, g.Name
                    FROM Children c
                    JOIN Gifts g 
                    ON c.childid = g.childid
                    WHERE c.Name = '{child}'
                    ''')
  
  child = cursor.fetchone()
  print(child)
  return child

def addChild(child):
  with sqlite3.connect(lootbag_db) as conn:
    cursor = conn.cursor()
  
    try:
      cursor.execute(
        '''
        INSERT INTO Children
        Values(?,?,?)
        ''', (None, child["name"], child["receiving"])
      )
    except sqlite3.OperationalError as err:
      print("oops", err)

def addGift(gift):
  print(gift[2], gift[3])
  with sqlite3.connect(lootbag_db) as conn:
    cursor = conn.cursor()
  
    toy = gift[2]
    name = gift[3]
    
    try:
      cursor.execute(
        '''INSERT INTO Gifts
        SELECT null, '{0}', 1, Childid
        FROM Children c
        WHERE c.Name = '{1}'
        '''.format(toy, name)
      )
    except sqlite3.OperationalError as err:
      print("oops", err)




# INSERT INTO Sidekicks
#  SELECT null, 'Robin', 'M', 'Neerdowell', SuperheroId
#  FROM Superheroes s
#  WHERE s.Name = name;

# INSERT INTO Gifts
# SELECT null, 'balloon', 1, childid
# FROM Children c
# WHERE c.Name = "Samuel";



if __name__ == "__main__":
  # getChildren()
  # getChild('Samuel')
  # addChild({
  #   "name": "Samuel",
  #   "receiving": 1
  # })
  if sys.argv[1] == 'add':
    addGift(sys.argv)
  # elif sys.argv[1] == 'get-all':
  #       getChildren()