from datetime import datetime
 
from paciente import Paciente
from medico import Medico
 
 
class Cita:
    def __init__(self, codigo, paciente, medico, fecha):
        self._codigo = codigo
        self.paciente = paciente
        self.medico = medico
        self.fecha = fecha
 
    @property
    def codigo(self):
        return self._codigo
 
    @property
    def paciente(self):
        return self._paciente
 
    @paciente.setter
    def paciente(self, valor):
        if not isinstance(valor, Paciente):
            raise ValueError("El campo paciente debe ser un objeto de la clase Paciente")
        self._paciente = valor
 
    @property
    def medico(self):
        return self._medico
 
    @medico.setter
    def medico(self, valor):
        if not isinstance(valor, Medico):
            raise ValueError("El campo medico debe ser un objeto de la clase Medico")
        self._medico = valor
 
    @property
    def fecha(self):
        return self._fecha
 
    @fecha.setter
    def fecha(self, valor):
        valor = (valor or "").strip()
        if not valor:
            raise ValueError("La fecha es obligatoria")
        try:
            datetime.strptime(valor, "%d/%m/%Y")
        except ValueError:
            raise ValueError("La fecha debe tener el formato dd/mm/aaaa (ej: 15/09/2026) y ser una fecha real")
        self._fecha = valor
 
    def resumen(self):
        return f"{self._codigo}: {self._paciente.nombre} con Dr. {self._medico.nombre} - {self._fecha}"
