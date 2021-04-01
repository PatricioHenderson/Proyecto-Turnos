DROP TABLE IF EXISTS gimnasio;

CREATE TABLE gimnasio(
    [id] INTEGER PRIMARY KEY AUTOINCREMENT,
    [name] TEXT NOT NULL,
    [lastname] TEXT NOT NULL,
    [document] TEXT NOT NULL,
    [mail] TEXT NOT NULL,
    [password] TEXT NOT NULL
);

CREATE TABLE turnos(
    [id] INTEGER PRIMARY KEY,
    [turnos] TEXT,
)