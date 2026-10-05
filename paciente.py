class Paciente:
    def __init__(self, codigo, nombre, edad):
        self._codigo = codigo
        self.nombre = nombre
        self.edad = edad

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        valor = (valor or "").strip()
        if not valor:
            raise ValueError("El nombre es obligatorio")
        if not all(parte.isalpha() for parte in valor.split()):
            raise ValueError("El nombre no puede contener números")
        self._nombre = valor

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        texto = str(valor).strip()
        if not texto.lstrip("-").isdigit():
            raise ValueError("La edad es obligatoria y debe ser un número, no letras")
        edad = int(texto)
        if edad < 0:
            raise ValueError("La edad no puede ser negativa")
        if edad > 100:
            raise ValueError("La edad es irreal")
        self._edad = edad

    def resumen(self):
        return f"{self._codigo} - {self._nombre} - {self._edad} años"
