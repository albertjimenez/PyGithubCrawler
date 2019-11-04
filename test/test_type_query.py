from my_enum.type_query import TypeQuery


def test_type_query():
    input_list = ["Repositories", "Issues", "Wikis"]
    output_list = [TypeQuery.REPO, TypeQuery.ISSUES, TypeQuery.WIKIS]
    for index, elem in enumerate(input_list):
        assert TypeQuery.get_type_from_str(elem) == output_list[index]
