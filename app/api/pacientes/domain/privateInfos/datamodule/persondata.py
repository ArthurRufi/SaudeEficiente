# tratar todas as entradas pessoais de usuarios 


class PatientPersonalData:
    def __init__(self, name: str, age: int, address: str, phone_number: str, email: str, principal_parent_name: str = None, principal_parent_contact: str = None):
        self._name = name
        self._age = age
        self._address = address
        self._phone_number = phone_number
        self._email = email
        self._principal_parent_name = principal_parent_name
        self._principal_parent_contact = principal_parent_contact

    def get_name(self):
        return self._name
    
    def set_name(self, name: str):
        if not name or not isinstance(name, str):
            raise ValueError("Nome deve ser uma string válida")
        self._name = name.strip()
    
    def get_age(self):
        return self._age
    
    def set_age(self, age: int):
        if not isinstance(age, int) or age < 0 or age > 150:
            raise ValueError("Idade deve ser um número entre 0 e 150")
        self._age = age
    
    def get_address(self):
        return self._address
    
    def set_address(self, address: str):
        if not address or not isinstance(address, str):
            raise ValueError("Endereço deve ser uma string válida")
        self._address = address.strip()
    
    def get_phone_number(self):
        return self._phone_number
    
    def set_phone_number(self, phone_number: str):
        #adicionar validacao de formato de telefone
        if not phone_number or not isinstance(phone_number, str):
            raise ValueError("Número de telefone inválido")
        self._phone_number = phone_number.strip()
    
    def get_email(self):
        return self._email
    
    def set_email(self, email: str):
        if not email or "@" not in email:
            raise ValueError("Email inválido")
        self._email = email.strip()
    
    def get_principal_parent_name(self):
        return self._principal_parent_name
    
    def set_principal_parent_name(self, principal_parent_name: str):
        if principal_parent_name and not isinstance(principal_parent_name, str):
            raise ValueError("Nome do responsável deve ser uma string válida")
        self._principal_parent_name = principal_parent_name.strip() if principal_parent_name else None
    
    def get_principal_parent_contact(self):
        return self._principal_parent_contact
    
    def set_principal_parent_contact(self, principal_parent_contact: str):
        if principal_parent_contact and not isinstance(principal_parent_contact, str):
            raise ValueError("Contato do responsável inválido")
        self._principal_parent_contact = principal_parent_contact.strip() if principal_parent_contact else None