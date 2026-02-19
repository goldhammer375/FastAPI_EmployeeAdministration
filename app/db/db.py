from sqlmodel import create_engine, Session
from app.settings.config import settings

def build_db_url() -> str:
    type = settings.db_type
    host = settings.db_host
    port = settings.db_port
    name = settings.postgres_db
    user = settings.postgres_user
    db_pass = settings.postgres_pass

    if not type or type == 'sqlite':
        return 'sqlite:///./database.db'
    
    # elif type != 'sqlite' or type != 'postgresql':
    #     raise Exception(f'Tipo de base de datos incorrecta (sqlite | postgresql): {type}')
    
    elif user and not db_pass:
        raise Exception('No se puede declarar una contraseña sin usuario')

    elif port and not host:
        raise Exception('No se puede declarar un puerto sin host')
    
    url = 'postgresql://'
    if user and db_pass:
        url += f'{user}:{db_pass}'
    if user and host:
        url += '@'
    if host and port:
        url += f'{host}:{port}'
    if (user or host) and name:
        url += '/'
    if name:
        url += name
    return url
    


engine = create_engine(build_db_url(), echo = settings.debug)

def get_session():
    with Session(engine) as s:
        yield s