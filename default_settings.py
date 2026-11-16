import json
DEFAULT_SETTINGS = {"currency": "SEK", "discount": 0}
def load_settings(path):
    result = DEFAULT_SETTINGS.copy()
    try:
        with open (path,'r', encoding='utf-8') as file:
            data=json.load(file)
    except FileNotFoundError:
        print(f'Нет файла')
        return result 
    except json.JSONDecodeError as error:
        print(f"повреждённый JSON: строка {error.lineno}, столбец {error.colno}: {error.msg}")
        return result
    if not isinstance(data,dict):
        print ('data должен быть словарем')
        return result
    for key in DEFAULT_SETTINGS:
        if key in data:
            result[key]=data[key]
            


    if not isinstance(result['currency'],str) or len(result['currency'].strip())==0:
        print('Неправильное значение currency')
        result['currency'] = DEFAULT_SETTINGS['currency']


    
    if not isinstance(result['discount'], int) or isinstance(result['discount'], bool) or result['discount'] < 0 or result['discount'] > 100:
        print('Неправильное значение discount')
        # Если скидка плохая — сбрасываем её на дефолтную (0)
        result['discount'] = DEFAULT_SETTINGS['discount']
        return result
        
    return result

    
test_files = {
    "s_ok.json": '{"currency": "EUR", "discount": 15}',
    "s_broken.json": '{"currency": "EUR",',
    "s_list.json": '["EUR", 15]',
    "s_partial.json": '{"currency": "EUR"}',
    "s_bad.json": '{"currency": "EUR", "discount": 150}',
        "s_empty_currency.json": '{"currency": "", "discount": 10}', 
}
for name, text in test_files.items():
    with open(name, "w", encoding="utf-8") as f:
        f.write(text)

for path in ["nosuch.json"] + list(test_files):
    print(path, "→", load_settings(path))          
    

