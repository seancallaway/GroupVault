from django.test import TestCase
from django.urls import resolve
from entries.models import Entry, Folder
from entries.views import EntryListAjax, HomePage
from users.models import CustomUser


BOOTSTRAP_VERSION = 'bootstrap/4.4.1'


class HomePageTest(TestCase):

    def setUp(self):
        CustomUser.objects.create_user(username='testuser', email='test@fake.com', password='testpass')

    def test_root_url_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func.view_class, HomePage)

    def test_home_page_redirects_anonymous(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)

    def test_home_page_uses_correct_bootstrap(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get('/')
        self.assertContains(response, BOOTSTRAP_VERSION)


class AJAXViewTest(TestCase):

    def setUp(self):
        CustomUser.objects.create_user(username='testuser', email='test@fake.com', password='testpass')
        self.folder = Folder.objects.create(name='Root')
        self.item1 = Entry.objects.create(name='Test 1', folder=self.folder, secret='SuperSecret')
        self.item2 = Entry.objects.create(name='Test 2', folder=self.folder, secret='ExtraSecret')

    def test_url_resolves_to_folder_view(self):
        found = resolve('/ajax/folder/1')
        self.assertEqual(found.func.view_class, EntryListAjax)

    def test_entry_list_requires_login(self):
        response = self.client.get('/ajax/folder/1')
        self.assertEqual(response.status_code, 302)

    def test_entry_list_returns_list_group(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get('/ajax/folder/1')
        self.assertContains(response, 'list-group')


class FolderTest(TestCase):

    def setUp(self):
        self.root = Folder.objects.create(name='Root')
        self.sub1 = Folder.objects.create(name='Sub 1', parent=self.root)
        self.sub2 = Folder.objects.create(name='Sub 2', parent=self.root)

    def test_folder_str(self):
        self.assertEqual(str(self.sub1), self.sub1.name)

    def test_sub_folder_creation(self):
        self.assertEqual(self.root.sub_folders.count(), 2)
        self.assertIn(self.sub1, self.root.sub_folders.all())
        self.assertIn(self.sub2, self.root.sub_folders.all())


class EntryTest(TestCase):

    def setUp(self):
        self.secret_phrase = 'This is a secret!@#'
        self.root = Folder.objects.create(name='Root')
        self.entry = Entry.objects.create(name='Test Entry', folder=self.root, secret=self.secret_phrase)

    def test_entry_in_folder(self):
        self.assertEqual(self.root, self.entry.folder)

    def test_decrypt_entry(self):
        self.assertEqual(self.entry.decrypt(), self.secret_phrase)

    def test_raw_secret_is_encrypted(self):
        self.assertNotEqual(self.entry.secret, self.secret_phrase)
