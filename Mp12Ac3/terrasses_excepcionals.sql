
-- Crear la base de dades
CREATE DATABASE IF NOT EXISTS terrasses_db;
USE terrasses_db;

-- Crear taula principal 'Terrasses'
CREATE TABLE IF NOT EXISTS Terrasses (
    id_terrassa INT AUTO_INCREMENT PRIMARY KEY,
    emplacament VARCHAR(255),
    taules DECIMAL(5,2),
    cadires DECIMAL(5,2),
    latitud DECIMAL(15,13),
    longitud DECIMAL(15,13)
);

-- Crear taula 'Districtes' amb clau forana a la taula 'Terrasses'
CREATE TABLE IF NOT EXISTS Districtes (
    id_districte INT AUTO_INCREMENT PRIMARY KEY,
    nom_districte VARCHAR(255),
    codi_districte INT,
    id_terrassa INT,
    FOREIGN KEY (id_terrassa) REFERENCES Terrasses(id_terrassa) ON DELETE CASCADE
);

-- Crear taula 'GestioTerrasses' amb clau forana a la taula 'Terrasses'
CREATE TABLE IF NOT EXISTS GestioTerrasses (
    id_gestio INT AUTO_INCREMENT PRIMARY KEY,
    tipus_gestio VARCHAR(255),
    data_gestio DATE,
    id_terrassa INT,
    FOREIGN KEY (id_terrassa) REFERENCES Terrasses(id_terrassa) ON DELETE CASCADE
);

-- Inserir registres a la taula de Terrasses

    INSERT INTO Terrasses (emplacament, taules, cadires, latitud, longitud)
    VALUES (
        'C. ANGELS, 3',
        2,
        8,
        41.3823114554492,
        2.16805342845076
    );
    
    -- Inserir a la taula Districtes
    INSERT INTO Districtes (nom_districte, codi_districte, id_terrassa)
    VALUES (
        'Ciutat Vella',
        1,
        1
    );
    
    -- Inserir a la taula GestioTerrasses
    INSERT INTO GestioTerrasses (tipus_gestio, data_gestio, id_terrassa)
    VALUES (
        'Ampliacio',
        NULL,
        1
    );
    
    INSERT INTO Terrasses (emplacament, taules, cadires, latitud, longitud)
    VALUES (
        'C. ATLANTIDA, 23',
        3,
        12,
        41.3807755515452,
        2.18947292278196
    );
    
    -- Inserir a la taula Districtes
    INSERT INTO Districtes (nom_districte, codi_districte, id_terrassa)
    VALUES (
        'Ciutat Vella',
        1,
        2
    );
    
    -- Inserir a la taula GestioTerrasses
    INSERT INTO GestioTerrasses (tipus_gestio, data_gestio, id_terrassa)
    VALUES (
        'Ampliacio',
        NULL,
        2
    );
    
    INSERT INTO Terrasses (emplacament, taules, cadires, latitud, longitud)
    VALUES (
        'PL. CANONGE COLOM, 1',
        2,
        8,
        41.3806872912013,
        2.17071499449267
    );
    
    -- Inserir a la taula Districtes
    INSERT INTO Districtes (nom_districte, codi_districte, id_terrassa)
    VALUES (
        'Ciutat Vella',
        1,
        3
    );
    
    -- Inserir a la taula GestioTerrasses
    INSERT INTO GestioTerrasses (tipus_gestio, data_gestio, id_terrassa)
    VALUES (
        'Ampliacio',
        NULL,
        3
    );
    
    INSERT INTO Terrasses (emplacament, taules, cadires, latitud, longitud)
    VALUES (
        'AV. CATEDRAL, 7',
        2,
        8,
        41.3848746219737,
        2.17572019677928
    );
    
    -- Inserir a la taula Districtes
    INSERT INTO Districtes (nom_districte, codi_districte, id_terrassa)
    VALUES (
        'Ciutat Vella',
        1,
        4
    );
    
    -- Inserir a la taula GestioTerrasses
    INSERT INTO GestioTerrasses (tipus_gestio, data_gestio, id_terrassa)
    VALUES (
        'Ampliacio',
        NULL,
        4
    );
    
    INSERT INTO Terrasses (emplacament, taules, cadires, latitud, longitud)
    VALUES (
        'C. RAMBLA, 126',
        3,
        12,
        41.3840952479238,
        2.17128485652701
    );
    
    -- Inserir a la taula Districtes
    INSERT INTO Districtes (nom_districte, codi_districte, id_terrassa)
    VALUES (
        'Ciutat Vella',
        1,
        5
    );
    
    -- Inserir a la taula GestioTerrasses
    INSERT INTO GestioTerrasses (tipus_gestio, data_gestio, id_terrassa)
    VALUES (
        'Ampliacio',
        NULL,
        5
    );
    
    INSERT INTO Terrasses (emplacament, taules, cadires, latitud, longitud)
    VALUES (
        'C. RAMBLA, 133',
        2,
        8,
        41.3852183039578,
        2.16990513181272
    );
    
    -- Inserir a la taula Districtes
    INSERT INTO Districtes (nom_districte, codi_districte, id_terrassa)
    VALUES (
        'Ciutat Vella',
        1,
        6
    );
    
    -- Inserir a la taula GestioTerrasses
    INSERT INTO GestioTerrasses (tipus_gestio, data_gestio, id_terrassa)
    VALUES (
        'Ampliacio',
        NULL,
        6
    );
    
    INSERT INTO Terrasses (emplacament, taules, cadires, latitud, longitud)
    VALUES (
        'PLA. PALAU, 7',
        3,
        12,
        41.3832711345585,
        2.18284205788248
    );
    
    -- Inserir a la taula Districtes
    INSERT INTO Districtes (nom_districte, codi_districte, id_terrassa)
    VALUES (
        'Ciutat Vella',
        1,
        7
    );
    
    -- Inserir a la taula GestioTerrasses
    INSERT INTO GestioTerrasses (tipus_gestio, data_gestio, id_terrassa)
    VALUES (
        'Ampliacio',
        NULL,
        7
    );
    
    INSERT INTO Terrasses (emplacament, taules, cadires, latitud, longitud)
    VALUES (
        'PLA. PALAU, 9',
        1,
        4,
        41.3834022388973,
        2.1829511284243
    );
    
    -- Inserir a la taula Districtes
    INSERT INTO Districtes (nom_districte, codi_districte, id_terrassa)
    VALUES (
        'Ciutat Vella',
        1,
        8
    );
    
    -- Inserir a la taula GestioTerrasses
    INSERT INTO GestioTerrasses (tipus_gestio, data_gestio, id_terrassa)
    VALUES (
        'Ampliacio',
        NULL,
        8
    );
    
    INSERT INTO Terrasses (emplacament, taules, cadires, latitud, longitud)
    VALUES (
        'C. PRINCESA, 53',
        2,
        8,
        41.3869885967831,
        2.18233947149823
    );
    
    -- Inserir a la taula Districtes
    INSERT INTO Districtes (nom_districte, codi_districte, id_terrassa)
    VALUES (
        'Ciutat Vella',
        1,
        9
    );
    
    -- Inserir a la taula GestioTerrasses
    INSERT INTO GestioTerrasses (tipus_gestio, data_gestio, id_terrassa)
    VALUES (
        'Ampliacio',
        NULL,
        9
    );
    
    INSERT INTO Terrasses (emplacament, taules, cadires, latitud, longitud)
    VALUES (
        'C. TAPINERIA, 12',
        2,
        8,
        41.3847748266096,
        2.17669133396007
    );
    
    -- Inserir a la taula Districtes
    INSERT INTO Districtes (nom_districte, codi_districte, id_terrassa)
    VALUES (
        'Ciutat Vella',
        1,
        10
    );
    
    -- Inserir a la taula GestioTerrasses
    INSERT INTO GestioTerrasses (tipus_gestio, data_gestio, id_terrassa)
    VALUES (
        'Ampliacio',
        NULL,
        10
    );
    
    CREATE TABLE Usuaris (
    id_usuari INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    contrasenya VARBINARY(255) NOT NULL
);
