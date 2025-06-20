﻿# 🌐 Aplicació Web Immobiliària

Aplicació web desenvolupada amb **Python**, **Flask** i **MySQL**, pensada per a la gestió d'immobles i usuaris dins el context d'una immobiliària. Ofereix funcionalitats d'administració i consulta d'immobles, amb suport multilingüe i verificació segura de credencials.

## 🔍 Descripció General

Aquesta aplicació permet:
- **Consultar immobles públicament**, sense necessitat d'autenticació.
- **Autenticar usuaris** i diferenciar rols: client i administrador.
- **Administrar usuaris i immobles** (crear, modificar, eliminar), només disponible per a l'administrador.
- **Internacionalització (i18n)** amb detecció automàtica de l’idioma del navegador (suportat: català, castellà i anglès).
- **Middleware de validació** per comprovar correus electrònics i contrasenyes de manera segura.

---

## ⚙️ Requisits previs

Abans d'executar l'aplicació, cal instal·lar els paquets necessaris especificats a `requirements.txt`. Entre les dependències es troben:

- `mysql-connector-python`
- `python-dotenv`
- `logging` (integrat a la llibreria estàndard)
- `os` (integrat a la llibreria estàndard)

### Instal·lació de dependències

```bash
pip install -r requirements.txt

## Crea un fitxer .env a l’arrel del projecte amb la següent estructura:

DB_HOST=localhost
DB_NAME=immobiliaria
DB_USER=root
DB_PASSWORD=
CONTRASSENYA_SESSIO=una_clau_segura

Executa l’aplicació
python app.py
En aquest punt, si la base de dades no existeix, es crearà automàticament l’esquema.

🔐 Rutes protegides
Les següents rutes són accessibles només per a usuaris autenticats o com a administrador:

/administrarUsuari

/administrarFinques

Els usuaris no registrats poden veure els immobles públicament, però no poden fer cap modificació ni accedir a funcionalitats administratives.

🌍 Suport multilingüe (Internacionalització)
L’aplicació detecta l’idioma del navegador del client i carrega el diccionari corresponent en format JSON. Actualment es suporten:

ca – Català

es – Espanyol

en – Anglès

Els fitxers de traducció es troben habitualment a una carpeta com static/lang/ o similar, i es carreguen automàticament en iniciar la sessió de l’usuari o en accedir a la web.

🔐 Middleware de seguretat
S’ha implementat un middleware personalitzat que valida:

El format dels correus electrònics

La seguretat de les contrasenyes (longitud, caràcters especials, etc.)

Aquest middleware s’executa abans de permetre l’autenticació o registre de l’usuari.

✅ Notes finals
L’aplicació actualment funciona en local però aviat estarà en producció on implementarem noves funcións.

Per accedir a la web funcional serà necessari introduir les credencials d'un usuari ja registrat, mail i contrassenya que podreu trobar revisant la taula usuaris.
