# DNIE bot (in development)

A telegram bot for verifying DNI numbers (NIF) and NIE and randomly generate them.

In Spain, the official ID card is called DNI and its ID number is called NIF. For foreigners living in Spain, the number is one digit shorter and its name is NIE.

Made with [telepot](https://github.com/nickoala/telepot)

### Usage

#### Commands:

Verify a NIF or NIE:

    /verify

Generate random NIF:

    /randomdni

Generate random NIE:

    /randomnie

<br>

#### Inline:

Get control digit for a DNI or NIE number

    @DNIE_bot 12345678


<br>

List of random DNI numbers

    @DNIE_bot dni

List of random NIE numbers

    @DNIE_bot nie

### Bibliography

[telepot](https://github.com/nickoala/telepot)

[DNI number](http://www.interior.gob.es/web/servicios-al-ciudadano/dni/calculo-del-digito-de-control-del-nif-nie)
