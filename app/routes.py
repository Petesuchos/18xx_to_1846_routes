from flask import render_template, flash, redirect

from app import app, convert_18xx_to_1846_routes
from app.forms import XX_Game_Data_Form


@app.route('/', methods=['GET', 'POST'])
def index():
    form = XX_Game_Data_Form()
    tiles = None
    if form.validate_on_submit():
        try:
            tiles = convert_18xx_to_1846_routes.get_1846_routes_tile_configuration(form.game_data.data)
        except:
            flash('Something wrong with your data')
            return redirect('/')

    return render_template('index.html', title='18XX Game Data', form=form, tiles=tiles)
