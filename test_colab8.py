import colab8 as f
import pytest

#comprobamos que se emite una excepción
def test_exception():
    with pytest.raises(RuntimeError):
        f.exception(True) #esta llamada emite una excepción RuntimeError

#comprobamos el mensaje de la excepción
def test_exception_message():
    with pytest.raises(RuntimeError) as exc:
        f.exception(True)
    assert "Lanzo esta excepción" == str(exc.value)

#si la siguiente prueba no emite una excepción, es que ha funcionado correctamente:
def test_no_exception():
    f.exception(False)

#podemos ser explícitos y assertar que un error se ha producido o assertar un 'False':
def test_no_exception():
    try:
        f.exception(False)
    except Exception as exc:
        pytest.fail("Unexpected error")
        #la siguiente opción también funcionaría
        #assert False