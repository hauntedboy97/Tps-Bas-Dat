**Ejercicio5: Torneo de ciclismo**

**Esquema de BD:**

`TORNEO<cod_torneo, nombre_torneo, cod_corredor, cod_bicicleta,marca_bicicleta, nyap_corredor, sponsor, DNI_presidente_sponsor,DNI_medico>`

**Restricciones:**

a. El código del torneo es único y no se repite para diferentes torneos. Pero los nombres de
torneo pueden repetirse entre diferentes torneos (por ejemplo, el “Tour de Francia” se
desarrolla todos los años y siempre lleva el mismo nombre).
b. Un corredor corre varios torneos. Tiene un código único por torneo, pero en diferentes
torneos tiene diferentes códigos.
c. Cada corredor tiene varias bicicletas asignadas para un torneo.
d. Los cod_bicicleta pueden cambiar en diferentes torneos, pero dentro de un torneo son
únicos.
e. Cada bicicleta tiene una sola marca.
f. Cada corredor tiene varios sponsors en un torneo, y un sponsor puede representar a
varios corredores.
g. Cada sponsor tiene un único presidente y un único médico

### Paso 1: Determinar las Dependencias Funcionales (DFs)

A partir del esquema y las restricciones dadas, podemos determinar las siguientes dependencias funcionales:

1.**cod_torneo -> nombre_torneo**: Cada torneo tiene un código único `cod_torneo` que identifica de forma única al torneo, aunque el nombre del torneo `nombre_torneo` pueda repetirse en diferentes años.

2.**cod_torneo, cod_corredor -> nyap_corredor**: En cada torneo, cada corredor tiene un código único `cod_corredor`, lo que implica que el nombre y apellido del corredor `nyap_corredor` dependen de la combinación de `cod_torneo` y `cod_corredor`.

3.**cod_torneo, cod_corredor, cod_bicicleta -> marca_bicicleta**: En un torneo, cada bicicleta tiene un código único `cod_bicicleta`, y cada bicicleta tiene una única marca `marca_bicicleta`.

4.**sponsor -> DNI_presidente_sponsor, DNI_medico**: Cada sponsor tiene un único presidente y un único médico, por lo que `DNI_presidente_sponsor` y `DNI_medico` dependen funcionalmente del sponsor.

5.**cod_torneo, cod_corredor, sponsor -> nyap_corredor**: Cada corredor puede tener varios sponsors en un torneo, pero el `nyap_corredor` se identifica con su `cod_torneo` y un `sponsor` específico.

### Paso 2: Determinar las Claves Candidatas

Podemos observar que la combinación de **`cod_torneo`, `cod_corredor`, `cod_bicicleta`**, y sponsor identifica de forma única cada registro en el esquema, ya que:

`cod_torneo` identifica el torneo.
`cod_corredor` identifica de forma única a cada corredor dentro de un torneo.
`cod_bicicleta` identifica de manera única cada bicicleta del corredor en ese torneo.
`sponsor` identifica el patrocinador para un corredor en un torneo específico.

Por lo tanto, la **clave candidata** es:

- (`cod_torneo`, `cod_corredor`, `cod_bicicleta`, `sponsor`)


### Paso 3: Diseño en Tercera Forma Normal (3FN)

Se dividió la tabla original en cinco tablas (`Torneo`, `Corredor`, `Bicicleta`, `Sponsor`, `Corredor_Sponsor`) para eliminar dependencias transitivas y garantizar que cada atributo no clave dependa únicamente de la clave primaria completas:

1.**Tabla `Torneo`**
-`cod_torneo` (Clave primaria)
-`nombre_torneo`

2.**Tabla `Corredor`**
-`cod_torneo` (Clave foránea que referencia a Torneo)
-`cod_corredor` (Clave primaria compuesta junto con cod_torneo)
-`nyap_corredor`

3.**Tabla `Bicicleta`**
-`cod_torneo` (Clave foránea que referencia a Torneo)
-`cod_corredor` (Clave foránea que referencia a Corredor)
-`cod_bicicleta` (Clave primaria compuesta junto con cod_torneo y cod_corredor)
-`marca_bicicleta`

4.**Tabla `Sponsor`**
-`sponsor` (Clave primaria)
-`DNI_presidente_sponsor`
-`DNI_medico`

5.**Tabla `Corredor_Sponsor`** (Para gestionar la relación entre corredores y sponsors en un torneo específico)

-`cod_torneo` (Clave foránea que referencia a Torneo)
-`cod_corredor` (Clave foránea que referencia a Corredor)
-`sponsor` (Clave foránea que referencia a Sponsor)
