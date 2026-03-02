from django.test import TestCase
from django.urls import reverse
from .models import Note, Author


class NoteModelTest(TestCase):

    def setUp(self):
        self.author = Author.objects.create(name='Test Author')

        self.note = Note.objects.create(
            title='Test Note',
            content='Test Note 1',
            author=self.author
        )

    def test_note_list_view(self):
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')

    def test_note_detail_view(self):
        response = self.client.get(
            reverse('note_detail', args=[self.note.pk])
        )
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        response = self.client.post(
            reverse('note_create'),
            {
                'title': 'Note',
                'content': 'Content',
                'author': self.author.pk
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 2)

    def test_update(self):
        response = self.client.post(
            reverse('note_update', args=[self.note.pk]),
            {
                'title': 'New title',
                'content': 'New content',
                'author': self.author.pk
            }
        )
        self.assertEqual(response.status_code, 302)

        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'New title')

    def test_delete(self):
        response = self.client.get(
            reverse('note_delete', args=[self.note.pk])
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 0)
