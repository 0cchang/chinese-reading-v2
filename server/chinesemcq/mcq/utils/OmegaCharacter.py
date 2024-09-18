class OmegaCharacter:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OmegaCharacter, cls).__new__(cls)
            cls._instance.mapping = cls.load_mapping()
        return cls._instance
    
    def load_mapping(self):
        from mcq.models import omegaCharacter
        self.character_to_id = {obj.character: obj.unique_id for obj in omegaCharacter.objects.all()}
        self.id_to_character = {obj.unique_id: obj.character for obj in omegaCharacter.objects.all()}
