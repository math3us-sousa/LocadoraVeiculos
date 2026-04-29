from django.test import TestCase, Client
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from veiculo.models import *
from veiculo.forms import *

class TestesModelVeiculo(TestCase):

    instancia = None
    def setUp(self):
        self.instancia = Veiculo(
            marca=1,
            modelo='Teste',
            ano=date.today().year,
            cor=1,
            combustivel=1
        )

    def test_veiculo_novo(self):
        self.assertTrue(self.instancia.veiculo_novo)
        self.instancia.ano = 2025
        self.assertFalse(self.instancia.veiculo_novo)

    def test_anos_de_uso(self):
        self.instancia.ano = date.today().year - 10
        self.assertEqual(self.instancia.anos_de_uso(), 10)

class TestesViewListarVeiculos(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_login(self.user)
        self.url = reverse('listar-veiculos')
        Veiculo(
            marca=1,
            modelo='Teste',
            ano=date.today().year,
            cor=1,
            combustivel=1
        ).save()

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context.get('veiculos')), 1)

class TestesViewCriarVeiculo(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_login(self.user)
        self.url = reverse('criar-veiculo')

    def test_get_autenticado(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('form'), FormularioVeiculo)

    def test_get_nao_autenticado(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_post(self):
        data = {
            'marca': 1,
            'modelo': 'Teste',
            'ano': date.today().year,
            'cor': 1,
            'combustivel': 1
        }
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar-veiculos'))

        self.assertEqual(Veiculo.objects.count(), 1)
        self.assertEqual(Veiculo.objects.first().modelo, 'Teste')

class TestesViewEditarVeiculo(TestCase):

    def setUp(self):
        self.instancia = Veiculo.objects.create(marca=1, modelo='Teste', ano=date.today().year, cor=1, combustivel=1)
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_login(self.user)
        self.url = reverse('editar-veiculo', kwargs={'pk': self.instancia.id})

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('object'), Veiculo)
        self.assertIsInstance(response.context.get('form'), FormularioVeiculo)
        self.assertEqual(response.context.get('object').pk, self.instancia.id)
        self.assertEqual(response.context.get('object').marca, 1)

    def test_post(self):
        data = {
            'marca': 5,
            'modelo': 'Teste Editado',
            'ano': date.today().year -2,
            'cor': 2,
            'combustivel': 1
        }
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar-veiculos'))
        self.assertEqual(Veiculo.objects.count(), 1)
        self.assertEqual(Veiculo.objects.first().marca, 5)
        self.assertEqual(Veiculo.objects.first().pk, self.instancia.id)
        
class TestesViewDeletarVeiculo(TestCase):

    def setUp(self):
        self.instancia = Veiculo.objects.create(marca=1, modelo='Teste', ano=date.today().year, cor=1, combustivel=1)
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_login(self.user)
        self.url = reverse('excluir-veiculo', kwargs={'pk': self.instancia.id})
        Veiculo(marca=1, modelo='Teste', ano=date.today().year, cor=1, combustivel=1).save()

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('object'), Veiculo)
        self.assertEqual(response.context.get('object').pk, self.instancia.id)

    def test_post(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar-veiculos'))
        self.assertEqual(Veiculo.objects.count(), 0)  

