import pygame as pg
import sys
sys.path.append("\\".join(sys.path[0].split("\\")[:-1]))

from util.data import data
from util.router import router
from util.constants import Constants

import components
from events.handler import EventHandler

print(f"{Constants.CNSL_DATA}[DATA.JSON]: {data.data}{Constants.CNSL_RESET}")

class Menu:
	def __init__(self) -> None:
		pg.init()
		Constants.FONT = components.Font()

		self.eventsHandler:EventHandler = EventHandler(self)

		self.screen = pg.display.set_mode(Constants.RESOLUTION, Constants.DISPLAY_MODE, display=1)
		self.clock:pg.time.Clock = pg.time.Clock()

	def run(self) -> None:
		while True:
			self.page:components.Page = router.current

			# Handle events
			self.eventsHandler.handleEvent()
   
			self.render()
			
			# Stop the cursor from rendering
		# pg.mouse.set_visible(False)
   
			pg.display.update()
			self.clock.tick(Constants.FPS)
   
	def render(self):
		# Clear the screen
		self.screen.fill("black")

		# Render page background
		if isinstance(self.page.background, pg.Surface): self.screen.blit(self.page.background, (0, 0))
		else: self.screen.fill(self.page.background)

		# Render the page onto the screen
		self.page.render(self.screen)

if __name__ == "__main__":
    
	menu = Menu()
	menu.run()