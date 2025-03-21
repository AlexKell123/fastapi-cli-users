from src.init_services import init_services
from src.gateways import get_cli


services = init_services('config.json', 'cli')

cli = get_cli(*services)

if __name__ == '__main__':
    cli()
