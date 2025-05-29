from django.test import TestCase
from .models import Store, Category, Product
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
 
class ModelTests(TestCase):
    # Tests per comprovar que els models Store, Category i Product es creen correctament
    # i que la seva representació en text (__str__) funciona com esperem.

    def setUp(self):
        # Crear instàncies de Store, Category i Product per fer proves amb dades reals
        self.store = Store.objects.create(name='Botiga X')
        self.category = Category.objects.create(name='Làctics')
        self.product = Product.objects.create(
            name='Llet',
            price=1.50,
            stock=10
        )
        # Afegir les relacions ManyToMany després de crear el producte
        self.product.stores.add(self.store)
        self.product.categories.add(self.category)

    def test_models_str(self):
        # Comprova que el mètode __str__ dels models retorna el nom correcte
        self.assertEqual(str(self.store), 'Botiga X')
        self.assertEqual(str(self.category), 'Làctics')
        self.assertEqual(str(self.product), 'Llet')

class ViewTests(TestCase):
    def setUp(self):
        store = Store.objects.create(name='El Corte Inglés')
        category = Category.objects.create(name='Begudes')
        
        # Crear una imatge dummy petita
        image_content = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xFF\xFF\xFF'
            b'\x21\xF9\x04\x01\x00\x00\x00\x00\x2C\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x4C\x01\x00\x3B'
        )
        image_file = SimpleUploadedFile('test_image.gif', image_content, content_type='image/gif')

        for i in range(5):
            product = Product.objects.create(
                name=f'Item{i}',
                price=2.00 + i,
                stock=5 + i,
                image=image_file
            )
            product.stores.add(store)
            product.categories.add(category)

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['products']), 3)

    def test_product_list_view(self):
        response = self.client.get(reverse('products-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['products']), 5)
