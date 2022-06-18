import json
from json import JSONDecodeError
from banks import banks_brazil
from pathlib import Path
from os import mkdir
from os.path import isdir

# consts
ROOTDIR = 'gerfinance'
ALLBANKS = '/allbanks.json'


def currentdir() -> str:
    return Path(__file__).parent.absolute().__str__()


def rootdir() -> str:
    current = currentdir()
    current = current[: current.index(ROOTDIR)+len(ROOTDIR)]
    return current


def create_banks_json():
    """
    This function takes data from a generator and
    save it as a json file.
    :return: None.
    """
    dirfile = f'{rootdir()}/settings'
    if not isdir(dirfile):
        mkdir(dirfile)
    dirfile += f'/{ALLBANKS}'
    try:
        with open(dirfile, 'r') as reader:
            json.loads(reader.read())
    except (JSONDecodeError, FileNotFoundError):
        banks = tuple(bank for bank in banks_brazil())
        with open(dirfile, 'w') as writer:
            writer.write(json.dumps({'banks': banks}, indent=4))
            del banks


def get_all_banks():
    """
    Get all banks generator.
    :return: Generator or None.
    """
    dirfile = f'{rootdir()}/settings/{ALLBANKS}'
    try:
        with open(dirfile, 'r') as reader:
            banks = json.loads(reader.read())
            banks = tuple(banks['banks'])
    except (JSONDecodeError, FileNotFoundError):
        return None
    return (bank for bank in banks)
