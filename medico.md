class Medico:
    ESPECIALIDADES = [
        "Medicina General",
        "Pediatria",
        "Obstetricia",
        "Ginecologia",
        "Cirugia General",
        "Nutricion",
    ]

    def __init__(self, codigo, nombre, especialidad):
        self._codigo = codigo
        self.nombre = nombre
        self.especialidad = especialidad

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
        if not all(parte.replace(".", "").isalpha() for parte in valor.split()):
            raise ValueError("El nombre no puede contener números")
        self._nombre = valor

    @property
    def especialidad(self):
        return self._especialidad

    @especialidad.setter
    def especialidad(self, valor):
        valor = (valor or "").strip()
        if valor not in self.ESPECIALIDADES:
            raise ValueError(f"La especialidad debe ser una de: {', '.join(self.ESPECIALIDADES)}")
        self._especialidad = valor

    def resumen(self):
        return f"{self._codigo} - {self._nombre} - {self._especialidad}"

