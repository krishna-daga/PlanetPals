from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.core.window import Window
import logging


from Orchestrator.plugins.llm_call import chat_complete

# Configure logging
logging.basicConfig(level=logging.DEBUG,  # Set the logging level
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        logger.info('Home screen has started')
        
        layout = BoxLayout(orientation='vertical', spacing=20, padding=20, 
                           size_hint=(1, None), height=Window.height)
        layout.bind(minimum_height=layout.setter('height'))  # Ensure layout expands as needed
        
        # Add logo centered horizontally
        logo = Image(source='Logo.png', size_hint=(None, None), 
                     size=(Window.width * 0.5, Window.width * 0.5),
                     pos_hint={'center_x': 0.5})  # Center align horizontally
        logo.allow_stretch = True
        logo.keep_ratio = True
        logo.border = (Window.width * 0.25, Window.width * 0.25, Window.width * 0.25, Window.width * 0.25)
        layout.add_widget(logo)
        
        # Create a white box for "Today's Tasks"
        tasks_layout = BoxLayout(padding=10, spacing=10)
        tasks_layout.size_hint_y = None
        tasks_layout.height = 60  # Fixed height for "Today's Tasks" box
        
        tasks_label = Label(text="Today's Tasks", font_size='24sp', bold=True)
        tasks_layout.add_widget(tasks_label)
        
        layout.add_widget(tasks_layout)
        tasks = chat_complete()
        number = 1
        for task in tasks:
            
            task_label = Label(text=f"{number}. {task}", font_size='18sp', size_hint=(1, None), height=30, halign='left')
            layout.add_widget(task_label)
            number +=1
        self.add_widget(layout)
        



class ProfileScreen(Screen):
    def __init__(self, **kwargs):
        super(ProfileScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        label = Label(text='Profile: Scores and Task History',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5})
        layout.add_widget(label)

        # Add example score and history
        score = Label(text="Total Score: 150")
        layout.add_widget(score)
        history = ["Task 1: Plant a tree", "Task 2: Recycle plastic"]
        for entry in history:
            layout.add_widget(Label(text=entry))

        self.add_widget(layout)

class LeaderboardScreen(Screen):
    def __init__(self, **kwargs):
        super(LeaderboardScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        label = Label(text='Leaderboard',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5})
        layout.add_widget(label)

        # Add example leaderboard
        leaderboard = ["1. User1 - 300 points", "2. User2 - 250 points"]
        for entry in leaderboard:
            layout.add_widget(Label(text=entry))

        self.add_widget(layout)

class MainApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(ProfileScreen(name='profile'))
        # sm.add_widget(LeaderboardScreen(name='leaderboard'))

        root = BoxLayout(orientation='vertical')

        # Navigation buttons
        nav_layout = BoxLayout(size_hint_y=None, height='50dp')
        home_btn = Button(text='Home', on_press=lambda x: setattr(sm, 'current', 'home'))
        profile_btn = Button(text='Profile', on_press=lambda x: setattr(sm, 'current', 'profile'))
        # leaderboard_btn = Button(text='Leaderboard', on_press=lambda x: setattr(sm, 'current', 'leaderboard'))

        nav_layout.add_widget(home_btn)
        nav_layout.add_widget(profile_btn)
        # nav_layout.add_widget(leaderboard_btn)

        root.add_widget(sm)
        root.add_widget(nav_layout)

        return root

if __name__ == '__main__':
    app = MainApp()
    app.run()
