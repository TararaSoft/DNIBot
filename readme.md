# DNIEBot (in development)

A telegram bot for verifying DNI numbers (NIF) and NIE and randomly generate them.

In Spain, the official ID card is called DNI and its ID number is called NIF. For foreigners living in Spain, the number is slightly different and its name is NIE.

Made with [telepot](https://github.com/nickoala/telepot)

### Usage

#### Commands:

Verify a NIF or NIE:

    /verify

Generate random NIF:

    /randomdni

Generate random NIE:

    /randomnie

#### Inline:

<br>

Verify if 12345678Z is a valid DNI number

    @dni_bot 12345678z

Verify if 1234567Y is a valid NIE

    @dni_bot 1234567Y

(In both cases you can use upper or lower case for the letter)


<br>

Generate a random DNI number

    @dni_bot random

### Bibliography

[telepot](https://github.com/nickoala/telepot)

[DNI number](http://www.interior.gob.es/web/servicios-al-ciudadano/dni/calculo-del-digito-de-control-del-nif-nie)