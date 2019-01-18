DELETE FROM Children;
DELETE FROM Gifts;

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS Children;
DROP TABLE IF EXISTS Gifts;

CREATE TABLE `Children` (
  `Childid` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `Name` TEXT NOT NULL,
  `Receiving` BIT NOT NULL
);

INSERT INTO Children VALUES (null, 'suzy', '1');
INSERT INTO Children VALUES (null, 'michael', '1');

CREATE TABLE `Gifts` (
    `Giftid` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `Name` TEXT NOT NULL,
    `Delivered` BIT NOT NULL,
    `Childid` INTEGER NOT NULL,
    FOREIGN KEY(`Childid`)
  REFERENCES `Children`(`Childid`)
  ON DELETE CASCADE
);