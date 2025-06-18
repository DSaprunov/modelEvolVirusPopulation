from random import random, randint, choice
import math
import dearpygui.dearpygui as dpg
import numpy as np

dict_otbor = {
    0: {
        'ATGACC': [1, 'WT'],
        'TTGAAC': [0.291, 'M41L/T215N'],
        'TTGTCC': [0.493, 'M41L/T215S'],
        'TTGTAC': [0.782, 'M41L/T215Y'],
    },
    0.03: {
        'ATGACC': [0.56, 'WT'],
        'TTGAAC': [0.124, 'M41L/T215N'],
        'TTGTCC': [0.393, 'M41L/T215S'],
        'TTGTAC': [0.617, 'M41L/T215Y'],
    },
    0.3: {
        'ATGACC': [0.16, 'WT'],
        'TTGAAC': [0.038, 'M41L/T215N'],
        'TTGTCC': [0.116, 'M41L/T215S'],
        'TTGTAC': [0.385, 'M41L/T215Y'],
    },
    2: {
        'ATGACC': [0.043, 'WT'],
        'TTGAAC': [0.02, 'M41L/T215N'],
        'TTGTCC': [0.009, 'M41L/T215S'],
        'TTGTAC': [0.187, 'M41L/T215Y'],
    },
    5: {
        'ATGACC': [0.005, 'WT'],
        'TTGAAC': [0.001, 'M41L/T215N'],
        'TTGTCC': [0.003, 'M41L/T215S'],
        'TTGTAC': [0.1, 'M41L/T215Y'],
    },
    10000: {
        'ATGACC': [0, 'WT'],
        'TTGAAC': [0, 'M41L/T215N'],
        'TTGTCC': [0, 'M41L/T215S'],
        'TTGTAC': [0.02, 'M41L/T215Y'],
    }
}

dict_otbor_second = {
    0: {
        'TTG': {
            "otb": 0.601,
            "word": 'M41L',
        },
        'AAC': {
            "otb": 0.203,
            "word": 'T215N',
        },
        'TCC': {
            "otb": 0.253,
            "word": 'T215S',
        },
        'TAC': {
            "otb": 0.704,
            "word": 'T215Y',
        },
    },
    0.03: {
        'TTG': {
            "otb": 0.510,
            "word": 'M41L',
        },
        'AAC': {
            "otb": 0.096,
            "word": 'T215N',
        },
        'TCC': {
            "otb": 0.100,
            "word": 'T215S',
        },
        'TAC': {
            "otb": 0.606,
            "word": 'T215Y',
        },
    },
    0.3: {
        'TTG': {
            "otb": 0.166,
            "word": 'M41L',
        },
        'AAC': {
            "otb": 0.012,
            "word": 'T215N',
        },
        'TCC': {
            "otb": 0.016,
            "word": 'T215S',
        },
        'TAC': {
            "otb": 0.290,
            "word": 'T215Y',
        },
    },
    2: {
        'TTG': {
            "otb": 0.024,
            "word": 'M41L',
        },
        'AAC': {
            "otb": 0.0009,
            "word": 'T215N',
        },
        'TCC': {
            "otb": 0.004,
            "word": 'T215S',
        },
        'TAC': {
            "otb": 0.116,
            "word": 'T215Y',
        },
    },
    5: {
        'TTG': {
            "otb": 0.01,
            "word": 'M41L',
        },
        'AAC': {
            "otb": 0,
            "word": 'T215N',
        },
        'TCC': {
            "otb": 0,
            "word": 'T215S',
        },
        'TAC': {
            "otb": 0.027,
            "word": 'T215Y',
        },
    },
    10000: {
        'TTG': {
            "otb": 0.001,
            "word": 'M41L',
        },
        'AAC': {
            "otb": 0,
            "word": 'T215N',
        },
        'TCC': {
            "otb": 0,
            "word": 'T215S',
        },
        'TAC': {
            "otb": 0.011,
            "word": 'T215Y',
        },
    },
}
field_names = ['M41L/T215N', 'M41L/T215S', 'M41L/T215Y', 'M41L', 'T215N', 'T215S', 'T215Y', 'WT']
additional_field_name = 'Kol_prohodov'

field_values = {name: 0 for name in field_names}

dict_got = {
    'M41L/T215N': 0,
    'M41L/T215S': 0,
    'M41L/T215Y': 0,
    'M41L': 0,
    'T215N': 0,
    'T215S': 0,
    'T215Y': 0,
    'WT': 0,
}

dict_got_end = {
    'M41L/T215N': [],
    'M41L/T215S': [],
    'M41L/T215Y': [],
    'M41L': [],
    'T215N': [],
    'T215S': [],
    'T215Y': [],
    'WT': [],
}

dict_got_el = {
    'M41L/T215N': '',
    'M41L/T215S': '',
    'M41L/T215Y': '',
    'M41L': '',
    'T215N': '',
    'T215S': '',
    'T215Y': '',
    'WT': '',
}

values_dict = {
    'G': {
        0.03: 'C',
        0.08: 'T',
        0.89: 'A',
    },
    'T': {
        0.14: 'G',
        0.19: 'A',
        0.67: 'C',
    },
    'C': {
        0.032: 'G',
        0.278: 'A',
        0.690: 'T',
    },
    'A': {
        0.1: 'T',
        0.17: 'C',
        0.73: 'G',
    }
}
def func_mutation(character):
    t = random()
    for i, key in enumerate(values_dict[character]):
        if t < key:
            return values_dict[character][key]
    return character


dict = ['A', 'C', 'T', 'G']
a = []
prot_1 = 1800
prot_2 = 2000
name_41 = ['A', 'T', 'G']
name_215 = ['A', 'C', 'C']
const_promezh_1 = 121
const_promezh_2 = 643
numbers = [121, 122, 123, 643, 644, 645]
k = 0

dict_postr_first = {
    'M41L/T215N': ['T', 'T', 'G'],
    'M41L/T215S': ['T', 'T', 'G'],
    'M41L/T215Y': ['T', 'T', 'G'],
    'M41L': ['T', 'T', 'G'],
    'T215N': [],
    'T215S': [],
    'T215Y': [],
    'WT': ['A', 'T', 'G'],
}

dict_postr_second = {
    'M41L/T215N': ['A', 'A', 'C'],
    'M41L/T215S': ['T', 'C', 'C'],
    'M41L/T215Y': ['T', 'A', 'C'],
    'M41L': [],
    'T215N': ['A', 'A', 'C'],
    'T215S': ['T', 'C', 'C'],
    'T215Y': ['T', 'A', 'C'],
    'WT': ['A', 'C', 'C'],
}
infectionList = [
    {
        "name": "onefold",
        "value": 1,
    },
    {
        "name": "twofold",
        "value": 2,
    },
    {
        "name": "threefold",
        "value": 3,
    },
]

medicineList = [
    {
        "name": "0",
        "value": 0,
    },
    {
        "name": "0,03",
        "value": 0.03,
    },
    {
        "name": "0,3",
        "value": 0.3,
    },
    {
        "name": "2",
        "value": 2,
    },
    {
        "name": "5",
        "value": 5,
    },
    {
        "name": "10,000",
        "value": 10000,
    },
]

combo_tag = "infection_combo"
combo_tag2 = "medicine_combo"

def on_run_button_click(sender, app_data, user_data):
    values = [float(dpg.get_value(name)) for name in field_names]
    total = sum(values)
    kol_prohodov = int(dpg.get_value(additional_field_name))

    selected_name = dpg.get_value(combo_tag)
    selected_name2 = dpg.get_value(combo_tag2)

    selected_value = next(
        (item["value"] for item in infectionList if item["name"] == selected_name),
        None
    )
    # print(selected_value)
    selected_value2 = next(
        (item["value"] for item in medicineList if item["name"] == selected_name2),
        None
    )

    field_nameser = ['M41L/T215N', 'M41L/T215S', 'M41L/T215Y', 'M41L', 'T215N', 'T215S', 'T215Y', 'WT']

    field_valueser = {name:int(dpg.get_value(name)) for name in field_names}
    dpg.set_value("total_text", f"Total sum: {total}")
    data = test_pot(total, kol_prohodov, field_valueser, selected_value, selected_value2)
    dpg.delete_item("plot_series", children_only=True)
    # for i, (x, y) in enumerate(data):
    with dpg.window(label="Graph Window"):
        with dpg.plot(label="Plot", height=400, width=600):
            dpg.add_plot_legend()
            dpg.add_plot_axis(dpg.mvXAxis, label="Step")
            with dpg.plot_axis(dpg.mvYAxis, label="Quantity type"):
                for i, (x, y) in enumerate(data):
                    dpg.add_line_series(x,y,label=field_names[i],parent="plot_series")
def take_begin(type, kol, a):
    for i in range(kol):
        b = []
        for j in range(min(prot_1, 121)):
            b.append(dict[randint(0, 3)])

        if dict_postr_first[type]==[]:
            for j in range(3):
                b.append(dict[randint(0, 3)])
        else:
            for j in range(3):
                b.append(dict_postr_first[type][j])

        for j in range(min(prot_1, 124), min(prot_1, 643)):
            b.append(dict[randint(0, 3)])

        if dict_postr_second[type]==[]:
            for j in range(3):
                b.append(dict[randint(0, 3)])
        else:
            for j in range(3):
                b.append(dict_postr_second[type][j])

        for j in range(643, max(prot_1 - 1, 644)):
            b.append(dict[randint(0, 3)])
        a.append(b)

def test_pot(values, kolvo, list, selected_value, selected_value2):
    result = []
    for key in list:
        dict_got_end[key].append(list[key])
    for name in list:
        if list[name] != 0:
            take_begin(name, list[name], a)
    # print(len(a))
    # в 3 случае здесь сделать чтобы делилось на 3
    prot_2 = int(values)
    prot_3 = int(values)
    if selected_value == 3:
        prot_3 = prot_2 - 1
    for j in range(kolvo):
        prot_2_new = prot_2
        b = []
        for i in range(prot_3-1):
            k = random()
            if k <= 0.5:
                rand_ai = randint(1, prot_1-1)
                if len(a[i]) == 0 and len(a[i+1]) == 0:
                    pass
                else:
                    if selected_value == 1:
                        try:
                            a[i+1][rand_ai: prot_1], a[i][rand_ai: prot_1] = a[i][rand_ai: prot_1], a[i+1][rand_ai: prot_1]
                        except Exception as e:
                            print(e)
                            print(rand_ai, prot_1, len(a[i+1]))
                    if selected_value == 2:
                        new_mix = a[i][:prot_1] + a[i + 1][prot_1:]
                        a.append(new_mix)
                    if selected_value == 3:
                        a[i+1][rand_ai: prot_1], a[i][rand_ai: prot_1] = a[i+2][rand_ai: prot_1], a[i+2][rand_ai: prot_1]
        if len(a[i]) == 0:
            pass
        else:
            for i in range(prot_2):
                k = random()
                if k <= 0.2:
                    rand_ai = choice(numbers)
                    if (const_promezh_1 <= rand_ai <= const_promezh_1+2) or (const_promezh_2 <= rand_ai <= const_promezh_2+2):
                        a[i][rand_ai] = func_mutation(a[i][rand_ai])
        i = 0
        while i < len(a):
            k = random()
            otb = -1
            word = ' '
            try:
                b=''.join(a[i][const_promezh_1:const_promezh_1+3]+ a[i][const_promezh_2:const_promezh_2 + 3])
                otbor = dict_otbor[selected_value2][b]
                word = otbor[1]
                otb = otbor[0]
            except Exception as e:
                b1 = ''.join(a[i][const_promezh_1:const_promezh_1 + 3])
                b2 = ''.join(a[i][const_promezh_2:const_promezh_2 + 3])
                otb = -1
                word = ' '
                try:
                    if b1 == 'TTG':
                        otb = dict_otbor_second[selected_value2][b1]["otb"]
                        word = dict_otbor_second[selected_value2][b1]["word"]
                    else:
                        otb = dict_otbor_second[selected_value2][b2]["otb"]
                        word = dict_otbor_second[selected_value2][b2]["word"]
                except Exception as e:
                    e = e
                # if b1 == 'TTG':
                #     otb = 0.601
                #     word = 'M41L'
                # elif b2 == 'AAC':
                #     otb = 0.203
                #     word = 'T215N'
                # elif b2 == 'TCC':
                #     otb = 0.253
                #     word = 'T215S'
                # elif b2 == 'TAC':
                #     otb = 0.704
                #     word = 'T215Y'
            if k <= otb:
                dict_got_el[word] = a[i]
                dict_got[word] += 1
            else:
                # pass
                del(a[i])
                i -= 1
            i += 1
        prot_2_new = len(a)
        key1 = 'WT'
        if prot_2_new < prot_2:
            for key, value in dict_got.items():
                if value != 0 and key != 'WT':
                    key1 = key
                    for i in range(math.floor(value*prot_2/prot_2_new - value)):
                        a.append(dict_got_el[key])
                    dict_got[key] = value + math.floor(value*prot_2/prot_2_new - value)
            if dict_got['WT'] == 0:
                if len(a) < prot_2:
                    prot_2_new = len(a)
                    for i in range(prot_2-len(a)):
                        a.append(dict_got_el[key1])
                    dict_got[key1] = dict_got[key1] + prot_2-prot_2_new
            else:
                if len(a) < prot_2:
                    prot_2_new = len(a)
                    take_begin('WT', prot_2 - prot_2_new, a)
                    dict_got[key1] = dict_got[key1] + prot_2-prot_2_new

        for key, value in dict_got.items():
            dict_got_end[key].append(value)
        for key in dict_got:
            dict_got[key] = 0
        print(j)
    for i in dict_got_end:
        x = np.array(range(len(dict_got_end[i]))).tolist()
        # print(dict_got_end)
        # print(len(x), len(dict_got_end[i]))
        result.append((x, dict_got_end[i]))
    return result


dpg.create_context()
dpg.create_viewport(title='Dear PyGui Interface', width=800, height=600)

with dpg.window(label="Main Window"):
    for name in field_names:
        dpg.add_input_text(label=name, default_value="0", tag=name)
    dpg.add_combo(
        label="Choose type infection",
        items=[i["name"] for i in infectionList],
        default_value=infectionList[0]["name"],
        tag = combo_tag
    )
    dpg.add_combo(
        label="Choose medicine",
        items=[i["name"] for i in medicineList],
        default_value=medicineList[0]["name"],
        tag=combo_tag2
    )
    dpg.add_input_text(label=additional_field_name, default_value="0", tag=additional_field_name)
    dpg.add_button(label="Run", callback=on_run_button_click)
    dpg.add_text("", tag="total_text")


with dpg.window(label="Graph Window"):
    with dpg.plot(label="Plot", height=400, width=600):
        dpg.add_plot_legend()
        dpg.add_plot_axis(dpg.mvXAxis, label="X-Axis")
        with dpg.plot_axis(dpg.mvYAxis, label="Y-Axis"):
            dpg.add_line_series([], [], label="Series", parent="plot_series")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
