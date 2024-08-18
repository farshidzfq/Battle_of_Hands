from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.popup import Popup
from kivy.core.audio import SoundLoader
from random import choice

# دکمه تصویری با قابلیت کلیک
class ImageButton(ButtonBehavior, Image):
    pass

class RockPaperScissorsApp(App):
    def build(self):
        Window.clearcolor = (0.15, 0.15, 0.2, 1)  # تنظیم رنگ پس‌زمینه
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.result_label = Label(text='Choose your move:', font_size='28sp', color=(0.9, 0.9, 0.9, 1), bold=True)
        layout.add_widget(self.result_label)
        
        button_layout = GridLayout(cols=3, spacing=20, size_hint=(1, 0.7))
        
        self.rock_button = ImageButton(source='images/rock.png')
        self.paper_button = ImageButton(source='images/paper.png')
        self.scissors_button = ImageButton(source='images/scissors.png')
        
        self.rock_button.bind(on_press=self.play_rock)
        self.paper_button.bind(on_press=self.play_paper)
        self.scissors_button.bind(on_press=self.play_scissors)
        
        button_layout.add_widget(self.rock_button)
        button_layout.add_widget(self.paper_button)
        button_layout.add_widget(self.scissors_button)
        
        layout.add_widget(button_layout)
        
        return layout
    
    def play_rock(self, instance):
        self.animate_button(self.rock_button)
        self.play('Rock')
    
    def play_paper(self, instance):
        self.animate_button(self.paper_button)
        self.play('Paper')
    
    def play_scissors(self, instance):
        self.animate_button(self.scissors_button)
        self.play('Scissors')
    
    def animate_button(self, button):
        anim = Animation(size=(button.width * 1.2, button.height * 1.2), duration=0.1) + Animation(size=(button.width, button.height), duration=0.1)
        anim.start(button)

    def play(self, player_choice):
        options = ['Rock', 'Paper', 'Scissors']
        computer_choice = choice(options)
        
        sound = SoundLoader.load('sounds/select.wav')
        if sound:
            sound.play()
        
        if player_choice == computer_choice:
            result = 'It\'s a draw!'
        elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
             (player_choice == 'Paper' and computer_choice == 'Rock') or \
             (player_choice == 'Scissors' and computer_choice == 'Paper'):
            result = 'You win!'
            sound = SoundLoader.load('sounds/win.wav')
        else:
            result = 'You lose!'
            sound = SoundLoader.load('sounds/lose.wav')
        
        if sound:
            sound.play()
        
        result_text = f'Computer chose {computer_choice}.\n{result}'
        self.result_label.text = result_text

if __name__ == '__main__':
    RockPaperScissorsApp().run()
