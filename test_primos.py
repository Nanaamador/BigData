import pytest
from primos import es_primo

def test_es_primo():

    assert es_primo(7) == True
    assert es_primo(10) == False
    assert es_primo(3) == True
    assert es_primo(100) == False
    assert es_primo(15) == False
    assert es_primo(101) == True
    assert es_primo(0) == False


