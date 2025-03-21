from src.config_loader import JsonConfigLoader
from src.repositories.factories import DBFactory, RepositoryFactory
from src.error_handlers import ErrorHandlerFactory
from src.notifications.email_notification import EmailNotification
from src.services import UserService, PositionService



def init_services(config_file, gateway_type):
    config = JsonConfigLoader.get(config_file)

    db = DBFactory.get(config)
    error_handler = ErrorHandlerFactory.get(gateway_type)
    email_notification = EmailNotification()

    user_repository = RepositoryFactory.get(db, error_handler, 'user')
    position_repository = RepositoryFactory.get(db, error_handler, 'position')

    user_service = UserService(user_repository, email_notification, error_handler)
    position_service = PositionService(position_repository)

    return [user_service, position_service]
