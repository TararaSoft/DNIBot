# DNIEBot

A telegram bot for verifying DNI numbers (NIF) and NIE and randomly generate them.

In Spain, the official ID card is called DNI and its ID number is called NIF. For foreigners living in Spain, the number is slightly different and its name is NIE.

Made with [twx.botapi](https://github.com/datamachine/twx.botapi)

### Usage

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

[twx.botapi documentation](http://pythonhosted.org/twx.botapi/)

[DNI number](http://www.interior.gob.es/web/servicios-al-ciudadano/dni/calculo-del-digito-de-control-del-nif-nie)