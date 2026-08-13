import os
import sys
from pathlib import Path
import django

# Garantir que o diretório do projeto esteja no sys.path quando executado a partir de scripts/
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.test import Client

c = Client()
resp = c.get('/clientes/cadastro/')
print('STATUS', resp.status_code)
print('LENGTH', len(resp.content))
print('CONTENT_REPR')
print(repr(resp.content))
for k, v in resp.items():
    print('HEADER', k, v)
