# Python Service Windows Example

1. Verificar DLL do Python
    * Na pasta de instalação do python "..\Lib\site-packages\win32" deve ter uma DLL com nome: "pywintypes37.dll" no meu caso é a "pywintypes37" pois estou usando o python 3.7, este número irá variar de acordo com sua versão;
    * Caso a DLL não esteja na pasta citada acima verifique na seguinte pasta "..\Lib\site-packages\pywin32_system32", procure a DLL e faça uma cópia para a pasta         "..\Lib\site-packages\win32";

2. Instalação 
    * Para instalar o Service entre com o seguinte comando no console: python PythonServiceExamplo.py install;
    * Para atualizar o Service entre com o seguinte comando no console: python PythonServiceExamplo.py update;
