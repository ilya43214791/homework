import textwrap
from datetime import datetime
from decimal import Decimal

item_1_title = textwrap.shorten(input('Введіть назву першого товару: ').ljust(20, '.'), width=20, placeholder='...')
item_1_quantity = input('Введіть бажаєму кількість першого товару: ')
item_1_prices = input('Введіть ціну першого товару: ')


item_2_title = textwrap.shorten(input('Введіть назву другого товару: ').ljust(20, '.'), width=20, placeholder='...')
item_2_quantity = input('Введіть бажаєму кількість другого товару: ')
item_2_prices = input('Введіть ціну другого товару: ')

item_1_total_cost = Decimal((item_1_quantity)) * Decimal((item_1_prices))
item_1_total_cost_right_format = item_1_total_cost.quantize(Decimal('0.01'))


item_2_total_cost = Decimal((item_2_quantity)) * Decimal((item_2_prices))
item_2_total_cost_right_format = item_1_total_cost.quantize(Decimal('0.01'))

prices_new_1 = Decimal(item_1_prices).quantize(Decimal('0.01'))
prices_new_2 = Decimal(item_2_prices).quantize(Decimal('0.01'))

printing_template = '{}\t\t\t\t\t{}\t\t\t\t{}\t\t\t{}'


print('\n\n\n')
print('фіскальний чек'.capitalize().center(80, '~'))
print('магазин "все для дому"'.upper().center(80))
print(f'Товар\t\t\t\t\t\t\t\t\tкількість\t\tціна\t\tвартість')
print(printing_template.format(item_1_title, item_1_quantity, prices_new_1, item_1_total_cost_right_format))
print(printing_template.format(item_2_title, item_2_quantity, prices_new_2, item_2_total_cost_right_format))
print('~' * 80)
print(printing_template.format(
    'ВСЬОГО'.ljust(20),
    int(item_1_quantity) + int(item_2_quantity),
    prices_new_1 + prices_new_2,
    item_1_total_cost_right_format + item_1_total_cost_right_format
    )
)
print(datetime.now().strftime('%d-%m-%Y %H:%M:%S').rjust(80))
print('\n\n')