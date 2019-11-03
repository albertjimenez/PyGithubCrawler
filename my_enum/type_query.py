from enum import Enum


class TypeQuery(Enum):
    REPO = "Repositories"
    ISSUES = "Issues"
    WIKIS = "Wikis"

    @staticmethod
    def get_type_from_str(name: str):
        if name == TypeQuery.REPO.value:
            return TypeQuery.REPO
        elif name == TypeQuery.ISSUES.value:
            return TypeQuery.ISSUES
        elif name == TypeQuery.WIKIS.value:
            return TypeQuery.WIKIS
        else:
            raise Exception("Missing type {0}, please consider extend the type query.".format(name))
