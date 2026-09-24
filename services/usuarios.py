import logging
from app.repositories import usuarios as usuarios_repository
from app.security import hash_password, verify_password

logger = logging.getLogger(__name__)


class EmailYaRegistradoError(Exception):
    pass


class CredencialesInvalidasError(Exception):
    pass


def registrar_usuario(db, email: str, password: str, repo=usuarios_repository):
    if repo.obtener_por_email(db, email):
        raise EmailYaRegistradoError(f"El email {email} ya está registrado")

    hashed = hash_password(password)
    nuevo_usuario = repo.guardar(db, email, hashed)
    logger.info(f"Usuario registrado con éxito: {email}")
    return nuevo_usuario


def autenticar_usuario(db, email: str, password: str, repo=usuarios_repository):
    usuario = repo.obtener_por_email(db, email)
    if not usuario or not verify_password(password, usuario.hashed_password):
        logger.warning(
            f"Intento de autenticación fallido para el email: '{email}'"
        )
        raise CredencialesInvalidasError("Email o contraseña incorrectos")

    return usuario