def fraude(antes: float, durante: float) -> bool:
    if antes <= durante:
        return True
    else:
        return False


def desconto_superior(antes: float, durante: float) -> bool:
    desconto = antes - durante

    if desconto > 0 and desconto/antes > 0.1:
        return True
    else:
        return False
