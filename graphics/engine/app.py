from alfred.math.vector import Vector2
import pygame


class App:
    def __init__(self, starter_scene, target_fps, size=(1024, 600), display_caption="", background_color=(0, 0, 0)):
        self.target_fps = target_fps
        self.background_color = background_color
        self.display = pygame.display.set_mode(size)
        pygame.display.set_caption(display_caption)
        self.clock = pygame.time.Clock()
        self.deltatime = 1/self.target_fps
        self.set_scene(starter_scene)

    def set_scene(self, scene):
        self.current_scene = scene
        self.current_scene._set_app(self)

    def mainloop(self):
        while True:
            for event in pygame.event.get():
                self.current_scene.process(event)
                if event.type == pygame.QUIT:
                    raise SystemExit(0)
            self.display.fill(self.background_color)
            pygame.display.update()
            self.deltatime = 1/self.clock.tick(self.target_fps)
