from models.gate_type import GateType
from pygame import Surface, image, sprite, transform
from views.sprite_with_events import SpriteWithEvents

class GateView(SpriteWithEvents):

    MAX_WIDTH = 32

    @staticmethod
    def get_asset_name(gate_type: GateType):

       return f"assets/gate_{gate_type.value}.png"

    @staticmethod
    def _load_image(asset_name: str):
      try:
        return image.load(asset_name)
      except:
        raise Exception(f"Asset does not exist: '{asset_name}'")

    @staticmethod
    def resize(surface: Surface):
      ratio = surface.get_width() / surface.get_height()
      new_width = GateView.MAX_WIDTH
      new_height = new_width / ratio
      return transform.scale(surface, (int(new_width), int(new_height)))

    def __init__(self, id: int, type: GateType, x: int, y: int, z: int):
      self.id = id
      self.type = type
      self.image = GateView.resize(GateView._load_image(GateView.get_asset_name(type)))
      self.z = z
      super().__init__(GateView.resize(GateView._load_image(GateView.get_asset_name(type))), x, y)

    def render(self, surface: Surface):
      surface.blit(self.image, self.rect)
