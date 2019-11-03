from enum import Enum


class TypeQuery(Enum):
    """
    Enum to define the three supported types of elements that can be queried in Github
    """
    REPO = "Repositories"
    ISSUES = "Issues"
    WIKIS = "Wikis"

    @staticmethod
    def get_type_from_str(name: str):
        """
        Returns the correspondent type from a plain string
        :param name: String of the type's name
        :return: TypeQuery enum
        """
        if name == TypeQuery.REPO.value:
            return TypeQuery.REPO
        elif name == TypeQuery.ISSUES.value:
            return TypeQuery.ISSUES
        elif name == TypeQuery.WIKIS.value:
            return TypeQuery.WIKIS
        else:
            raise Exception("Missing type {0}, please consider extend the type query.".format(name))
