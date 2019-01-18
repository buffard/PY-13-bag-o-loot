import sqlite3
import sys

# sys.argv is a list of the passed in args from the command line
print(sys.argv)

def printArg():
  print(sys.argv[1])

lootbag_db = '/Users/Buffard/workspace/NSS/back-end/exercises/BAG-OF-LOOT/lootbag.db'

def getChildren():
  with sqlite3.connect(lootbag_db) as conn:
    cursor = conn.cursor()

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


if __name__ == "__main__":
  getChildren()
  addChild({
    "name": "Samuel",
    "receiving": 1
  })
