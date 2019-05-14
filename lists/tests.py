from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page #2 - info test_root_url_resolves_to_home_page_view

# Create your tests here.

class HomePageTest(TestCase):
    '''
        ******  test_root_url_resolves_to_home_page_view    *********
    #1 resolve é a função que o Django itiliza internamente para resolver  URLs e descobrir para qual função de view eles devem ser mapeados.
        Estamos verificando se resolve, quando é chamado com '/', que é a raiz do site, encontra uma função chamada home_page
    #2 é a função de view que escreveremos  a serguir, a qual na verdade, devolverá o html que queremos
    '''
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')#1
        self.assertEqual(found.func, home_page)#2

    '''
        *********   test_home_page_returns_correct_html     *********
        #1 Criamos um objeto HttpRequest, que é  o que o Django verá quando o navegador de um usuário requisitar a página
        #2 Ele é passado para a nossa view home_page, que nos dará uma resposta.
        #3 Em seguida extraímos .content da resposta. Esses são os bytes brutos.Chamamos .decode() para convertê-los na string html enviada ao usuário
        #4 Queremos que comece com uma tag <html> que será fechada mais tarde
        #5 Além disso, queremos uma tag <title> com o conteúdo 'To-Do lists'
    '''
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()#1
        response = home_page(request)#2
        html = response.content.decode('utf8')#3
        self.assertTrue(html.startswith('<html>'))#4
        self.assertIn('<title>To-Do lists</title>', html)#5
        self.assertTrue(html.endswith('</html>'))#4
