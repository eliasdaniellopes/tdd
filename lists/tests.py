from django.urls import resolve
from django.test import TestCase
from lists.views import home_page #2

# Create your tests here.

class SmokeTest(TestCase):
    
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')#1
        self.assertEqual(found.func, home_page)#1

'''
    #1 resolve é a função que o Django itiliza internamente para resolver  URLs e descobrir para qual função de view eles devem ser mapeados.
        Estamos verificando se resolve, quando é chamado com '/', que é a raiz do site, encontra uma função chamada home_page
    #2 é a função de view que escreveremos  a serguir, a qual na verdade, devolverá o html que queremos
'''