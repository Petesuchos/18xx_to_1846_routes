from flask import render_template, flash

from app import app, convert_18xx_to_1846_routes
from app.forms import XX_Game_Data_Form


@app.route('/', methods=['GET', 'POST'])
def index():
    form = XX_Game_Data_Form()
    tiles = None
    if form.validate_on_submit():
        flash('18XX Game Data submited')
        tiles = convert_18xx_to_1846_routes.get_1846_routes_tile_configuration(form.game_data.data)
        # return redirect('/')

    return render_template('index.html', title='18XX Game Data', form=form, tiles=tiles)