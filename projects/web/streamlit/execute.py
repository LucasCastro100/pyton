import sys
from streamlit.web import cli as stcli

# Este script é usado para executar o aplicativo Streamlit de um diretório diferente.
sys.argv = ["streamlit", "run", "projects/web/streamlit/app.py"]
sys.exit(stcli.main())