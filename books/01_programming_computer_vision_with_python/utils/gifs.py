'''module with GIF processing functions
'''

from PIL import Image
import contextlib
import glob
    
    
'''
Создание GIF-изображения
'''
def create_gif(title: str, img_path: str, gif_path: str, file_type: str, frame_duration: int = 300) -> None:
    
    images_path = f'{img_path}{title}_*{file_type}'
    gif_path = f'{gif_path}{title}.gif'

    with contextlib.ExitStack() as stack:
        images_stack = (stack.enter_context(Image.open(image))
                        for image in sorted(glob.glob(images_path)))

        image = next(images_stack)

        image.save(fp=gif_path, 
                   format='GIF', 
                   append_images=images_stack,
                   save_all=True, 
                   duration=frame_duration, 
                   disposal=2,
                   loop=0)
        
        
'''
Выведение на экран GIF-изображения
'''
def display_gif(gif_name: str, gif_path: str) -> None:
    from IPython.display import Image

    with open(gif_path + gif_name, 'rb') as file:
        display(Image(file.read()))