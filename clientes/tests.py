from django.test import TestCase
from django.urls import reverse


class CadastroPageTests(TestCase):
	def test_cadastro_page_renders(self):
		response = self.client.get(reverse('cadastro'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Criar Conta')
