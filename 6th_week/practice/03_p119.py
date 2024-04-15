def split_str(input_str, separator='&', assignment='='):

    result = {}
    items = input_str.split(separator)

    for item in items:
        key, value = item.split(assignment)
        result[key] = value

    return result

s = 'led=on&motor=off&switch=off'
result = split_str(s)
print(result)
