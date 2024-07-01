SQL*Plus: Release 11.2.0.2.0 Production on Jue Jun 27 23:56:26 2024

Copyright (c) 1982, 2014, Oracle.  All rights reserved.

SQL> connect system
Enter password:
ERROR:
ORA-28002: the password will expire within 7 days


Connected.
create tablespace ElTridente
datafile 'C:\BasedatosElTridente\ElTridente.dbf'
size 20m
autoextend on next 10m
maxsize unlimited;


Tablespace created.

SQL>

SQL> CREATE USER TRIDENTE IDENTIFIED BY 6217
  2  DEFAULT TABLESPACE ElTridente
  3  QUOTA UNLIMITED ON ElTridente;

User created.

SQL> GRANT DBA TO TRIDENTE;

Grant succeeded.

SQL> exit

SQL> CONNECT TRIDENTE
Enter password: 6217
Connected.
SQL>

SQL> CREATE TABLE Producto (
  2  ID_prod NUMBER,
  3  Nom_prod VARCHAR2(255) UNIQUE,
  4  Descripcion VARCHAR2(1000),
  5  Precio NUMBER(10,2) NOT NULL CHECK (Precio > 0),
  6  Cant_stock NUMBER NOT NULL CHECK (Cant_stock >= 0),
  7  Categoria VARCHAR2(100) NOT NULL,
  8  CONSTRAINT producto_pk PRIMARY KEY (ID_prod)
  9  );

Table created.

SQL> CREATE SEQUENCE TRIDENTE_AUMENTA
  2  START WITH 1
  3  INCREMENT BY 1;

Sequence created.

SQL> CREATE OR REPLACE TRIGGER prod_primera
  2  BEFORE INSERT ON Producto
  3  FOR EACH ROW
  4  BEGIN
  5  SELECT TRIDENTE_AUMENTA.NEXTVAL
  6  INTO   :new.ID_prod
  7  FROM   dual;
  8  END;
  9  /

Trigger created.

SQL> CREATE USER Administrador IDENTIFIED BY 12345
  2  DEFAULT TABLESPACE ElTridente
  3  QUOTA UNLIMITED ON ElTridente;

User created.

SQL> GRANT CREATE SESSION TO ADMINISTRADOR;

Grant succeeded.

SQL> GRANT SELECT, INSERT, UPDATE, DELETE ON Usuario TO Administrador;

Grant succeeded.

SQL> CREATE USER Vendedor IDENTIFIED BY 54321
  2  DEFAULT TABLESPACE ElTridente
  3  QUOTA UNLIMITED ON ElTridente;

User created.

SQL> GRANT CREATE SESSION TO Vendedor;

Grant succeeded.

SQL> GRANT SELECT, INSERT ON Venta TO Vendedor;

Grant succeeded.