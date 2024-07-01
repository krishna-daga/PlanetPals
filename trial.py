from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, RoundedRectangle
import logging
from Orchestrator.plugins.llm_call import chat_complete

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        logger.info('Home screen has started')
        
        # Main layout
        main_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        # Add logo centered horizontally
        logo = Image(source='Logo.png', size_hint=(None, None), 
                     size=(Window.width * 0.5, Window.width * 0.5),
                     pos_hint={'center_x': 0.5})  # Center align horizontally
        logo.allow_stretch = True
        main_layout.add_widget(logo)

        # Tasks section
        tasks_layout = BoxLayout(orientation='vertical', spacing=10, padding=10, size_hint_y=None)
        tasks_layout.bind(minimum_height=tasks_layout.setter('height'))
        
        with tasks_layout.canvas.before:
            Color(0.1, 0.1, 0.1, 1)  # Dark gray background
            self.rect = RoundedRectangle(size=tasks_layout.size, pos=tasks_layout.pos)
        tasks_layout.bind(size=self._update_rect, pos=self._update_rect)
        
        tasks_title = Label(text="Today's Tasks", font_size='24sp', bold=True, size_hint_y=None, height=40, padding=(10, 10))
        tasks_layout.add_widget(tasks_title)
        
        # Scrollable task list
        scroll_view = ScrollView(size_hint=(1, None), size=(Window.width, Window.height * 0.4))
        task_list = GridLayout(cols=1, spacing=10, size_hint_y=None, padding=(10, 10))
        task_list.bind(minimum_height=task_list.setter('height'))
        
        tasks = chat_complete()
        for index, task in enumerate(tasks, 1):
            task_label = Label(text=f"{index}. {task}", font_size='18sp', size_hint_y=None, height=60, 
                               text_size=(Window.width - 40, None), halign='left', valign='middle', padding=(10, 10))
            task_list.add_widget(task_label)
        
        scroll_view.add_widget(task_list)
        tasks_layout.add_widget(scroll_view)
        
        main_layout.add_widget(tasks_layout)
        
        self.add_widget(main_layout)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size       
    
class ProfileScreen(Screen):
    def __init__(self, **kwargs):
        super(ProfileScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        label = Label(text='Profile: Scores and Task History',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5})
        layout.add_widget(label)

        # Add example score and history
        score = Label(text="Total Score: 150", font_size='18sp', size_hint_y=None, height=40)
        layout.add_widget(score)
        history = ["Task 1: Plant a tree", "Task 2: Recycle plastic"]
        for entry in history:
            layout.add_widget(Label(text=entry, font_size='16sp', size_hint_y=None, height=30))

        self.add_widget(layout)

class LeaderboardScreen(Screen):
    def __init__(self, **kwargs):
        super(LeaderboardScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        label = Label(text='Leaderboard',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5})
        layout.add_widget(label)

        # Add example leaderboard
        leaderboard = ["1. User1 - 300 points", "2. User2 - 250 points"]
        for entry in leaderboard:
            layout.add_widget(Label(text=entry, font_size='16sp', size_hint_y=None, height=30))

        self.add_widget(layout)

class MainApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(ProfileScreen(name='profile'))
        # sm.add_widget(LeaderboardScreen(name='leaderboard'))

        root = BoxLayout(orientation='vertical')

        # Navigation buttons
        nav_layout = BoxLayout(size_hint_y=None, height='50dp', padding=10, spacing=10, pos_hint={'center_x': 0.5})
        home_btn = Button(text='Home', on_press=lambda x: setattr(sm, 'current', 'home'))
        profile_btn = Button(text='Profile', on_press=lambda x: setattr(sm, 'current', 'profile'))
        # leaderboard_btn = Button(text='Leaderboard', on_press=lambda x: setattr(sm, 'current', 'leaderboard'))

        nav_layout.add_widget(home_btn)
        nav_layout.add_widget(profile_btn)
        # nav_layout.add_widget(leaderboard_btn)

        root.add_widget(sm)
        root.add_widget(nav_layout)

        return root


app = MainApp()
app.run()


