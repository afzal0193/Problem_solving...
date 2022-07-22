for i in range(int(input())):
    import textwrap

    value = input()
    warper = textwrap.TextWrapper(width=2)
    world_list = warper.wrap(text=value)
    value_string = value[:2]
    for i in world_list[1:]:
        if value_string[-1] != i[0]:
            value_string = value_string + i
        else:
            value_string = value_string + i[-1]
    print(value_string)


