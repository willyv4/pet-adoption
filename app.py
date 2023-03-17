from models import Pet, db, connect_db
from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "petsarecool1234"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def home_page():
    """
    Renders the home page, displaying all pets available for adoption.

    Returns:
    A rendered HTML template of the home page, containing all pets available for adoption.
    """

    pets = Pet.query.all()

    return render_template('home.html', pets=pets)


@app.route('/add-pet', methods=['GET', 'POST'])
def add_pet():
    """
    Renders the home page, displaying all pets available for adoption.

    Returns:
    A rendered HTML template of the home page, containing all pets available for adoption.
    """

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species,
                  photo_url=photo_url, age=age, notes=notes, available=True)
        db.session.add(pet)
        db.session.commit()

        return redirect('/')
    else:
        return render_template('add_pet.html', form=form)


@app.route('/<int:id>', methods=['GET', 'POST'])
def edit_pet(id):
    """
    Edits an existing pet in the database if a valid form is submitted.

    Args:
    id: Integer representing the id of the pet to be edited.

    Returns:
    If a valid form is submitted, redirects to the home page. Otherwise, renders the "pet details" form.
    """

    pet = Pet.query.get(id)
    form = AddPetForm(obj=pet)

    if form.validate_on_submit():
        form.populate_obj(pet)
        db.session.commit()

        return redirect(f'/')
    else:
        return render_template('pet_details.html', form=form, pet=pet)
