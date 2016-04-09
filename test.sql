CREATE TABLE tournament (
    id INTEGER PRIMARY KEY,
    name TEXT,
    location TEXT,
    calendar DATE,
    system TEXT,
    tie_break TEXT,
    round_num INT
);

CREATE TABLE player (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
);

CREATE TABLE game (
    id INTEGER PRIMARY KEY,
    round_num INTEGER,
    -- pull players' IDs from Player db
    white_player INTEGER,
    black_player INTEGER,
    outcome TEXT
);

CREATE TABLE player_tournament (
    player_id INTEGER,
    tournament_id INTEGER
);

CREATE TABLE game_tournament (
    game_id INTEGER,
    tournament_id INTEGER
);