import unittest
from app.models import Pitches, User


class PostModelTest(unittest.TestCase):

    def setUp(self):
        self.user_eugene = User(username='tiff', email='tiffanymugure@gmail.com',password='123', )
        self.new_post = Post(header='What is Lorem Ipsum?', post='All around the world their diverse people from specific countries who believe i  the art and love of food.They embrace different cuisine from exotic foods to the most simple food.Appreciating food is a way to happines ,trying to infuse different flavours gives one satisfaction', category='foodlab', posts=self.user_amira)

    def test_instance(self):
        self.assertEqual(self.new_post.header, 'What is Lorem Ipsum?')
        self.assertEqual(self.new_post, 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum')
        self.assertEqual(self.new_post.category, 'lifestyle')

    def test_save_post(self):
        self.new_post.save_post()
        self.assertTrue(len(Post.query.all()) > 0)

    def test_get_post_by_id(self):
        self.new_post.save_post()
        got_post = Post.get_post(1)
        self.assertTrue(len(got_post) > 0)

    def test_delete_post(self):
        self.new_post.delete_post()
        self.assertTrue(len(Post.query.id()) > 0)