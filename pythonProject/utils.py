

def split_text(text: str = None, separator: str = None):
    if text is None or separator is None:
        raise ValueError("Require two parameters")

    if separator is "":
        raise ValueError("Separator error")

    parts = text.split(sep=separator)
    if len(parts) == 2:
        return parts[0], parts[1]





def split_text_23(text: str = None, separator: str = None):
    if text is None or separator is None:
        raise ValueError("נדרשים שני פרמטרים")

    parts = text.split(sep=separator, maxsplit=1)  # פיצול פעם אחת בלבד
    if len(parts) == 2:
        return (parts[0], parts[1])
    else:
        return (parts[0], "")