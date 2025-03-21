from src.error_handlers import ErrorHandlerCli, ErrorHandlerFastapi


class ErrorHandlerFactory:
    @staticmethod
    def get(gateway_type):
        gateway_types = {'fastapi': ErrorHandlerFastapi,
                         'cli': ErrorHandlerCli
                         }
        return gateway_types[gateway_type]()
