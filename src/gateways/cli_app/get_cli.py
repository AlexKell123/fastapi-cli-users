import click


def get_cli(user_service, position_service):
    @click.group()
    def cli():
        pass

    @cli.command()
    @click.option('--full_name', prompt='Enter user name', help='User name')
    @click.option('--email', prompt='Enter user email', help='User email')
    def create_user(full_name: str, email: str):
        result = user_service.create(full_name, email)
        click.echo(result)

    @cli.command()
    @click.option('--user_id', prompt='Enter user ID', help='User ID')
    def read_user(user_id: int):
        result = user_service.read(user_id)
        click.echo(result)

    @cli.command()
    @click.option('--user_id', prompt='Enter user ID', help='User ID')
    @click.option('--full_name', prompt='Enter new name', help='New name')
    @click.option('--email', prompt='Enter new email', help='New email')
    def update_user(user_id: int, full_name: str, email: str):
        result = user_service.update(user_id, full_name, email)
        click.echo(result)

    @cli.command()
    @click.option('--user_id', prompt='Enter user ID', help='User ID')
    def delete_user(user_id: int):
        result = user_service.delete(user_id)
        click.echo(result)

    @cli.command()
    @click.option('--title', prompt='Enter title', help='Title')
    def create_position(title: str):
        result = position_service.create(title)
        click.echo(result)

    @cli.command()
    @click.option('--position_id', prompt='Enter position ID', help='Position ID')
    def read_position(position_id: int):
        result = position_service.read(position_id)
        click.echo(result)

    @cli.command()
    @click.option('--position_id', prompt='Enter position ID', help='Position ID')
    @click.option('--title', prompt='Enter new title', help='New title')
    def update_position(position_id: int, title: str):
        result = position_service.update(position_id, title)
        click.echo(result)

    @cli.command()
    @click.option('--position_id', prompt='Enter position ID', help='Position ID')
    def delete_position(position_id: int):
        result = position_service.delete(position_id)
        click.echo(result)

    return cli

