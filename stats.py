def count_words(content: str) -> int:
    return len(content.split())


def count_characters(content: str) -> dict[str, int]:
    c_dict: dict[str, int] = {}

    for c in content:
        lower_c = c.lower()

        if lower_c in c_dict:
            c_dict[lower_c] = c_dict[lower_c] + 1
        else:
            c_dict[lower_c] = 1

    return c_dict


def sort_dictionary(c_dict: dict[str, int]) -> list[dict[str, int]]:
    filtered_dicts = __filter_non_alphabetic_keys(c_dict)
    filtered_dicts.sort(key=__sort_by_value, reverse=True)

    return filtered_dicts


def __sort_by_value(d: dict[str, int]) -> int:
    return list(d.values())[0]


def __filter_non_alphabetic_keys(c_dict: dict[str, int]) -> list[dict[str, int]]:
    filtered_dicts = []
    items = c_dict.items()

    for k, v in items:
        if not k.isalpha():
            continue

        filtered_dicts.append({k: v})

    return filtered_dicts
