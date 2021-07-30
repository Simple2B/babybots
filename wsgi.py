#!/user/bin/env python
import click

from app import create_app, db, models, forms

app = create_app()


# flask cli context setup
@app.shell_context_processor
def get_context():
    """Objects exposed here will be automatically available from the shell."""
    return dict(app=app, db=db, models=models, forms=forms)


@app.cli.command()
def create_db():
    """Create the configured database."""
    from app.controllers.create_db_data import create_db_data
    db.create_all()
    create_db_data()


@app.cli.command()
def start():
    """Start Script."""
    from app.controllers import set_running
    set_running()


@app.cli.command()
def stop():
    """Stop Script."""
    from app.controllers import set_down
    set_down()


@app.cli.command()
def launch_script():
    """Launch Script."""
    from app.controllers import set_running, set_down
    set_running()
    # from app.controllers import launch_script
    # launch_script(func)
    set_down()


@app.cli.command()
@click.confirmation_option(prompt="Drop all database tables?")
def drop_db():
    """Drop the current database."""
    db.drop_all()


if __name__ == "__main__":
    app.run()
