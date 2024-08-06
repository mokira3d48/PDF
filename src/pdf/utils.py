import os


def get_file_paths_list(dir_path):
    """Returns the list of file paths contained on directory

    :param dir_path: The path to directory.
    :type dir_path: `str`
    :rtype: `list` of `str`
    """
    file_names = os.listdir(dir_path)
    file_paths = [os.path.join(dir_path, file_name)
                  for file_name in file_names]
    return file_paths


def get_page_numbers(pattern):
    """
    Function which parses the pattern of selected
    pages and returns list of page numbers.
    """
    pattern = pattern.strip()
    if pattern == '*':
        # le cas ou on selectionne toutes les pages;
        return list(range(pages_count))
    elif pattern == '':
        # le cas ou on selectionne la premiere page uniquement;
        return [0]

    page_numbers = []
    page_numbers_str = pattern.split(',')
    for element in page_numbers_str:
        numbers = element.strip()
        numbers = numbers.split('-')
        if len(numbers) == 1:
            page_num = numbers[0]
            if page_num:
                page_numbers.append(int(page_num))
        else:
            start = int(numbers[0])
            end = int(numbers[-1])
            page_numbers.extend(list(range(start, end + 1)))

    page_numbers = list(set(page_numbers))  # remove doublons;
    page_numbers = sorted(page_numbers)  # sort list by ascendant;
    return [x - 1 for x in page_numbers]

