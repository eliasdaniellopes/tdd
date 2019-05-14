from selenium import webdriver
import unittest
class NewVisitorTest(unittest.TestCase):#1
    def setUp(self):#3
        self.browser = webdriver.Firefox()
    def tearDown(self):#3
        self.browser.quit()
    def test_can_start_a_list_and_retrieve_it_later(self):#2
        self.browser.get('http://127.0.0.1:8000/')

        self.assertIn('To-Do', self.browser.title)#4
        self.fail('Finish the Test!')#5
if __name__ == "__main__":#6
    unittest.main(warnings='ignore')#7

'''
    O que esse código faz:(acompanhe as legendas no código)

    #1 Os testes estão organizados em classes, que herdam de unittest.TestCase
    #2 O corpo principal do testes está em um método chamado test_can...; Qualquer método cujo o nome começa com test é um método de teste
        e será executado pelo executor de testes. Podemos ter mais de um método test_ por classe.
    #3 setUp e tearDown são métodos especiais executados antes e depois de cada teste.
        Eles foram usados para iniciar e finalizar o nosso navegador, tearDown executará mesmo que acha um erro durante o teste
    #4Usamos o self.assertIn no lugar de simplesmente  assert para fazer nossas asserções de teste. O unittest disponibiliza muitas funções auxiliares como essa
        para fazer asseções de teste cini assertEqual, assertTrue, assertFalse e assim por diante.
    #5 self.fail simplesmente falha, independente do que houver, gerando a mensagem de erro especificada, ele foi usado como lembrete para finalizar o teste
    #6 Por fim temos a cláusula if name == 'main'(se vc ainda não viu é assim que um script Python verifica se esta´sendo executado a partir a linha de comando)
        e não está simplesmente sendo importado por outro script) Chamamos unittest.main(),  o que inicia  o executor de testes do unittest; ele encontrará
        automáticamente as calasses e métodos  de testes no arquivo e os executará
    7# warnings='ignore' sumprime um ResourceWarning supérfluo.
'''