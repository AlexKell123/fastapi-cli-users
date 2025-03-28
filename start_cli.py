from src.init_services import init_services
from src.gateways import get_cli


def init_cli():
    services = init_services('config.json', 'cli')
    return get_cli(*services)


app = init_cli()

if __name__ == '__main__':
    app()
