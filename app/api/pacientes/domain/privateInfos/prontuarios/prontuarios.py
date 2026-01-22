from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional
from pacientes.domain.privateInfos.datamodule.persondata import PatientPersonalData


class Prontuario(BaseModel):
    id: str
    paciente_id: str
    data_criacao: datetime
    descricao: str
    diagnostico: Optional[str] = None
    prescricao: Optional[str] = None
    observacoes: Optional[str] = None


class Paciente(BaseModel):
    id: str
    person_data: PatientPersonalData
    prontuarios: List[Prontuario] = Field(default_factory=list)


class ProntuarioRepository:
    def __init__(self):
        self.pacientes: dict[str, Paciente] = {}
        self.prontuarios: dict[str, Prontuario] = {}

    def adicionar_paciente(self, paciente: Paciente) -> None:
        self.pacientes[paciente.id] = paciente

    def adicionar_prontuario(self, paciente_id: str, prontuario: Prontuario) -> None:
        if paciente_id not in self.pacientes:
            raise ValueError(f"Paciente {paciente_id} não encontrado")
        
        self.prontuarios[prontuario.id] = prontuario
        self.pacientes[paciente_id].prontuarios.append(prontuario)

    def obter_paciente(self, paciente_id: str) -> Optional[Paciente]:
        return self.pacientes.get(paciente_id)

    def obter_prontuarios(self, paciente_id: str) -> List[Prontuario]:
        paciente = self.obter_paciente(paciente_id)
        return paciente.prontuarios if paciente else []
