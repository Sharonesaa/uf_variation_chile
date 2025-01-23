def calculate_media_val(month: list) -> float:
    long = len(month)
    return round(sum(month)/long, 2)

def get_month(date: str):
    months = {'01': 'enero',
     '02': 'febrero',
     '03': 'marzo',
     '04': 'abril',
     '05': 'mayo',
     '06': 'junio',
     '07': 'julio',
     '08': 'agosto',
     '09': 'septiembre',
     '10': 'octubre',
     '11': 'noviembre',
     '12': 'diciembre'}
    return months.get(date.split('-')[1])
     
def make_variation_list(month_values: dict):

    month_variation = {}
    previous_month_value = None

    for month, value in month_values.items():
        if previous_month_value is not None:
            variation = round(value - previous_month_value, 2)
            if variation > 0:
                month_variation[month] = ("up", variation)
            elif variation < 0:
                month_variation[month] = ("down", variation)
            else:
                month_variation[month] = ("no_change", 0)
        previous_month_value = value

    months_up = sorted(
        [(month, variation) for month, (status, variation) in month_variation.items() if status == "up"],
        key=lambda x: x[1]
    )

    months_down = sorted(
        [(month, variation) for month, (status, variation) in month_variation.items() if status == "down"],
        key=lambda x: x[1]
    )

    months_no_change = sorted(
        [month for month, (status, _) in month_variation.items() if status == "no_change"]
    )

    return {
        'months_up': months_up,
        'months_down': months_down,
        'months_no_change': months_no_change 
        }

def process_uf_data(data: list) -> dict:

    day_min_uf = float('inf')
    day_max_uf = float('-inf')
    month_values = {}

    for day in data:
        valor = float(day["Valor"].replace(".", "").replace(",", "."))
        month = get_month(day["Fecha"])

        if valor < day_min_uf:
            day_min_uf = valor
        if valor > day_max_uf:
            day_max_uf = valor

        if month in month_values:
            month_values[month].append(valor)
        else:
            month_values[month] = [valor]

    for key, value in month_values.items():
        month_values[key] = calculate_media_val(value)

    return {
        "day_min_uf": day_min_uf,
        "day_max_uf": day_max_uf,
        **make_variation_list(month_values)
    }

def get_example(key: str) -> dict:
    examples = {
        "uf_variation": {
            "day_min_uf": 28310.86,
            "day_max_uf": 29090.98,
            "months_up": [
                [
                    "septiembre",
                    26.29
                ],
                [
                    "febrero",
                    63.2
                ]
            ],
            "months_down": [
                [
                "julio",
                -27.79
                ],
                [
                "agosto",
                -13.63
                ]
            ],
            "months_no_change": [
                "noviembre",
                "junio"
            ]
            }
    }
    return {"content": {"application/json": {"example": examples.get(key, {})}}}
