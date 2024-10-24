class Medico:
    def __init__(self, name, crm):
        self._name = name
        self._crm = crm
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and value.strip():
            self._name = value
        else:
            print('Nome invalido')
            raise NameError
    
    @property
    def crm(self):
        return self._crm

    @crm.setter
    def crm(self, value):
        if isinstance(value, str) and value.strip():
            self._crm
        else:
            print ('CRM invalido')
            raise NameError