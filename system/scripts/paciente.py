class Paciente():
    def __init__(self, name, cadastroSus, documento, endereco):
        self._name = name
        self._cadastroSus = cadastroSus
        self._documento = documento
        self._endereco = endereco
        

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and value.strip():
            self._name = value
        else:
            raise ValueError("Nome inválido")
        
    @property
    def cadastroSus(self):
        return self._cadastroSus
    
    @cadastroSus.setter
    def cadastroSus(self, value):
        if isinstance(value, str) and value.strip():
            self._cadastroSus = value
        else:
            raise ValueError("Cadastro SUS inválido")
    
    @property
    def documento(self):
        return self._documento
    
    @documento.setter
    def documento(self, value):
        if isinstance(value, str) and value.strip():
            self._documento = value
        else:
            raise ValueError("Documento inválido")
    
    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, value):
        if isinstance(value, str) and value.strip():
            self._endereco = value
        else:
            raise ValueError("Endereço inválido")
