#%%
import json
import re
import requests
import datetime
 
today = datetime.date.today().strftime('%Y%m%d')   #20200315
 
def get_data():
    """
         estadísticas en tiempo real de rastreo, guardarlo en el directorio de datos, utilizan la fecha actual como un nombre de archivo, guarde el archivo JSON
    """
    Respuesta = Requests.get ( 'https://ncov.dxy.cn/ncovh5/view/pneumonia') # request.GET () Se utiliza para solicitar un sitio web de destino
    Imprimir (response.status_code) # mostrar el código de estado
    
 
    try:
        url_text = response.content.decode()                             
        #print(url_text)
        URL_CONTENT = Re.Search (R'Window.getListByCountryTypeService2True = (*)}]} catch',URL_TEXT, RE.S)  # RE.Search ():.? Cadena de exploración para encontrar la ubicación del primer partido de la generación modo de expresión regular, a continuación, volver El Partido correspondiente objeto.
                                                        # En cadena A, contiene una envoltura \ n, en cuyo caso: Si no se utiliza el parámetro RE.S, único partido cada línea, si no, cambiar un reinicio línea;
                                                                                                                                                   # Y después de usar el parámetro Re.s, la expresión regular utilizará esta cadena en su conjunto y que coincida con el conjunto.
        texts = url_content.group()                                      
        Content = texts.replace ( 'window.getlistbycountrytypeservice2true =', '') .Colocar ( '} catch', '') # elimina el exceso de caracteres
        json_data = json.loads(content)                                         
        with open( 'data/world/'+ today + '.json', 'w', encoding='UTF-8') as f:
            json.dump(json_data, f, ensure_ascii=False)
    except:
        print('<Response [%s]>' % response.status_code)
 
 
def get_statistics_data():
    """
         Obtener todas las estadísticas historia provinciales, guardarlo en el directorio de datos, guarde el archivo JSON
    """
    with open('data/world/' + today + '.json', 'r', encoding='UTF-8') as file:
        json_array = json.loads(file.read())
 
    statistics_data = {}
    for province in json_array:
        response = requests.get(province['statisticsData'])
        try:
            statistics_data[province['provinceName']] = json.loads(response.content.decode())['data']
        except:
            print('<Response [%s]> for url: [%s]' % (response.status_code, province['statisticsData']))
 
    with open("data/world/statistics_data"+today + ".json", "w", encoding='UTF-8') as f:
        json.dump(statistics_data, f, ensure_ascii=False)
# %%
