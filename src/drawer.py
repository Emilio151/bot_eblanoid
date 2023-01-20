import io
import matplotlib.pyplot as plt
import datetime as dt
import requests


def currency_data(currency):
    today = dt.date.today()
    today_month_ago = today - dt.timedelta(days=60)
    params = {'from': today_month_ago, 'till': today}
    url = 'http://iss.moex.com' + f'/iss/statistics/engines/futures/markets/indicativerates/securities/' \
                                  f'{currency}//rub.json'
    r = requests.get(url, params=params).json()['securities']['data']
    date_value, currency_value = [i[0] for i in r], [float(i[3]) for i in r]
    return date_value, currency_value


def currency_plot(date_value, currency_value, currency, night_theme=False):
    font_color = 'black'
    bg_color = 'white'
    if night_theme:
        font_color = '#e4e4eb'
        bg_color = '#35353d'
    photo = io.BytesIO()
    fig = plt.figure()
    axes = fig.add_axes([0, 0, 1, 1])
    x_major_locator = plt.MultipleLocator(10)
    ax = fig.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    ax.set_facecolor(bg_color)
    axes.plot(date_value, currency_value, label=f'{currency}/RUB', color=font_color, lw=2)
    fig.patch.set_facecolor(bg_color)
    axes.set_xlabel('Дата', color=font_color)
    axes.set_ylabel(f'{currency}/RUB', color=font_color)
    axes.tick_params(colors=font_color)
    axes.grid(axis='both', linestyle='--')
    fig.savefig(photo, format='jpg', bbox_inches='tight')
    photo.seek(0)
    return photo