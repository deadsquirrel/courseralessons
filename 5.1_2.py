def uniq(input):
    out_list = []
    for i in input:
        if i not in out_list:
            out_list.append(i)
        return out_list
