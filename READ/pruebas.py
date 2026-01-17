🔥 EJERCICIO 1 — Validador brutal de número

Pide un valor x.

Clasifica exactamente uno de estos casos:

"Vacío" → string vacío o solo espacios

"Número entero positivo"

"Número entero negativo"

"Cero"

"Decimal válido" → 3.14, -0.5

"Formato numérico inválido" → --3, 3..4, -., ., -

"Texto" → solo letras

"Mixto" → letras + números

📌 No se permite float() hasta validar
📌 El orden de los if importa muchísimo

🧨 EJERCICIO 2 — Edad con trampas reales

Pide edad.

Casos a cubrir:

Vacío o espacios → "Edad vacía"

Contiene letras → "Edad inválida"

Número negativo → "Edad inválida"

Decimal → "Edad inválida"

Menor de 18 → "Acceso denegado"

Exactamente 18 → "Acceso permitido"

Mayor a 120 → "Edad inválida"

Caso válido → "Acceso permitido"

📌 No repetir int(edad) más de una vez
📌 Validar antes de convertir

🧠 EJERCICIO 3 — Login lógico (sin usuarios reales)

Pide:

user = input()
password = input()


Reglas:

Si alguno está vacío → "Campos incompletos"

Usuario solo letras, contraseña solo números → válido

Usuario con números → "Usuario inválido"

Contraseña con letras → "Contraseña inválida"

Si usuario = "admin" y password = "1234" → "Acceso total"

Si formato válido pero credenciales incorrectas → "Acceso denegado"

📌 El orden aquí es clave

💣 EJERCICIO 4 — División ultra segura

Pide a y b.

Casos:

Vacíos → "Datos vacíos"

Texto → "Datos inválidos"

Decimales válidos → permitir

b == 0 o b == 0.0 → "División indefinida"

Resultado negativo → "Resultado negativo"

Resultado positivo → imprimir resultado

📌 Solo condicionales
📌 Convertir una sola vez

🧬 EJERCICIO 5 — Clasificador final (el más difícil)

Pide x.

Clasifica solo uno:

"Espacios"

"Entero"

"Decimal"

"Texto"

"Mixto"

"Símbolos" → @#$%

"Formato inválido" → --1, ..2, -.-

📌 No usar regex
📌 No usar listas
📌 Solo cabeza fría y lógica











