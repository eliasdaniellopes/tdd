from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page 
from django.template.loader import render_to_string
from lists.models import Item
# Create your tests here.

class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/') #1

        html = response.content.decode('utf8')#2
        expected_html = render_to_string('home.html')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'home.html')#3

        '''
            #1 Em vez de criar manualmente  um objeto HttpRequest e chamar a função de view de forma direta, chamamos self.client.get, passando a URL que queremos testar
            #2 Deixaremos os testes antigos  só para ter certeza que tudo está funcionando
            #3 .assertTemplateUsed é o método de teste que a classe TestCase do Django nos disponibiliza. Ela nos permite verificar qual template foi usada para renderizar
                uma resposta.(Só funciona para resposta que foram obtidas pelo cliente de teste.)
        '''
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')

class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')