input = [965842,9159,3372473,311,0,6,86213,48]

def add_to_dict(dict,inp,num):
    if inp in dict.keys():
        dict[inp] += num
    else:
        dict[inp] = num
    return

input_dict = {}
for element in input:
    add_to_dict(input_dict,element,1)
print(input_dict)

for repeat in range(75):
    output_dict = {}
    for key in input_dict.keys():
        if key == 0:
            add_to_dict(output_dict, 1, input_dict[key])
        elif len(str(key)) % 2 == 0:
            add_to_dict(output_dict, int(str(key)[:len(str(key))//2]), input_dict[key])
            add_to_dict(output_dict, int(str(key)[len(str(key)) // 2:]), input_dict[key])
        else:
            add_to_dict(output_dict, key*2024, input_dict[key])

    input_dict = output_dict
    print(repeat+1, sum(input_dict.values()))