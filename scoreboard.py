import pygame.font

class Scoreboard():
    """Class for scoreboard"""


    def __init__(self, game_settings, screen, stats):
        """Init scoreboard atributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.game_settings = game_settings
        self.stats = stats
        # score atributes - size, color, font
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 46)
        # prepare grafical text
        self.prepare_score()
        # prepare grafical level
        self.prepare_level()
        # prepare grafical record
        self.prepare_record()

    def prepare_score(self):
        """Convert text message to grafics and center with button."""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.game_settings.bg_color)
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.right = self.screen_rect.right - 20
        self.score_image_rect.top = 20

    def prepare_level(self):
        """Convert text message to grafics and center with button."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.game_settings.bg_color)
        # Level is appear under score value.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_image_rect.right
        self.level_rect.top = self.score_image_rect.bottom + 10

    def prepare_record(self):
        """Convert text message to graphics and center with button."""
        record_str = str(self.stats.record)
        self.record_image = self.font.render(record_str, True, self.text_color, self.game_settings.bg_color)
        # Get the rectangle of the record text image
        record_rect = self.record_image.get_rect()
        # Set the center of the record text image to the center of the screen
        record_rect.centerx = self.screen_rect.centerx
        # Set the top position to center the text vertically
        record_rect.top = 20
        # Update the record_rect attribute
        self.record_rect = record_rect

    def draw_score(self):
        self.screen.blit(self.score_image, self.score_image_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.record_image, self.record_rect)
