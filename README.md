# crowdar-test

1- Clonar el repositorio.  

2- Abrir un cmd/terminal y dirigirse al directorio raiz del repositorio clonado:  
Ejemplo: cd C:\Users\Emmanuel\Desktop\crowdar-test

3- Crear un entorno virtual:  
python -m venv venv

4- Activar el entorno virtual:  
source venv/bin/activate (Mac/Linux)  
venv\Scripts\activate (Windows)

5- Instalar las dependencias:  
pip install -r requirements.txt

6- Ejecutar los casos en chrome o firefox  

6a- Chrome (todos los casos):  
pytest tests --browser=chrome --html=reports/report_all_tests_chrome.html --self-contained-html

6b- Firefox (todos los casos):  
pytest tests --browser=firefox --html=reports/report_all_tests_firefox.html --self-contained-html

6c- Chrome (suite especifica):  
Ejemplo: pytest tests/test_login.py --browser=chrome --html=reports/report_login_tests_chrome.html --self-contained-html

6d- Firefox (suite especifica):  
Ejemplo: pytest tests/test_login.py --browser=firefox --html=reports/report_login_tests_firefox.html --self-contained-html