class RequirementsProcessor:
    __requirements_dict = dict()

    def __init__(self, file_path):
        self._file_path = file_path

    @property
    def file_path(self):
        return self._file_path

    def prepare_requirements_dict(self):
        with open(self._file_path) as f:
            for line in f:
                splits = line.strip().split('==')
                self.__requirements_dict[splits[0]] = splits[1]

    def get_version_of(self, module):
        return self.__requirements_dict.get(module)
