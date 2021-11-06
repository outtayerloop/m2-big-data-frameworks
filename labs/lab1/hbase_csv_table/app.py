import sys

ROW_KEY_COLUMN_NAME = 'objectid'
TABLE_NAME = 'ns_wiem_chouchane:trees'
GENDER_COLUMN_FAMILY = 'gender'
INFORMATION_COLUMN_FAMILY = 'information'
ADDRESS_COLUMN_FAMILY = 'address'


def main():
    columns = get_all_column_names()
    entry = sys.stdin
    command = get_table_creation_command()
    command = fill_command(command, entry, columns)
    sys.stdout.write(command)


def fill_command(command, entry, columns):
    row_key_column_index = columns.index(ROW_KEY_COLUMN_NAME)
    for line in entry:
        data = line.replace('\n', '').split(';')
        row_key = str(data[row_key_column_index])
        for index, element in enumerate(data):
            if index != row_key_column_index:
                command = add_new_command_line(command, index, row_key, element, columns)
    return command


def get_all_column_names():
    columns = sys.stdin.readline().replace('\n', '').split(';')
    return list(map(lambda column: column.lower(), columns))


def get_table_creation_command():
    return 'create "' + TABLE_NAME + '" , ' \
          '{NAME => "' + GENDER_COLUMN_FAMILY + '", VERSIONS => 10},  ' \
          '{NAME => "' + INFORMATION_COLUMN_FAMILY + '", VERSIONS => 10}, ' \
          '{NAME => "' + ADDRESS_COLUMN_FAMILY + '", VERSIONS => 10};'


def add_new_command_line(command, index, row_key, element, columns):
    meta_data = get_meta_data(index, row_key, columns)
    command += get_new_command_line(meta_data, element)
    return command


def get_meta_data(index, row_key, columns):
    return {
        'row_key': row_key,
        'column_family': get_column_family(index),
        'column': get_column(index, columns)
    }


def get_new_command_line(meta_data, element):
    return 'put "' + \
           TABLE_NAME + '", "' + \
           meta_data['row_key'] + '", "' + \
           meta_data['column_family'] + ':' + \
           meta_data['column'] + '", "' + \
           element + '";'


def get_column_family(index):
    if is_gender_column_family_index(index):
        return GENDER_COLUMN_FAMILY
    elif is_information_column_family_index(index):
        return INFORMATION_COLUMN_FAMILY
    else:
        return ADDRESS_COLUMN_FAMILY


def is_gender_column_family_index(index):
    return 2 <= index <= 4 \
           or 9 <= index <= 10


def is_information_column_family_index(index):
    return 5 <= index <= 7


def get_column(index, columns):
    return columns[index]


if __name__ == "__main__":
    main()