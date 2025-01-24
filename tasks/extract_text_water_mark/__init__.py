from oocana import Context
from blind_watermark import WaterMark
def main(params: dict, context: Context):
  image_file = params.get('image_file')
  wm_shape = params.get('wm_shape')
  bwm1 = WaterMark(password_img=1, password_wm=1)
  wm_extract = bwm1.extract(image_file, wm_shape=wm_shape, mode='str')

  context.preview({
    "type": "text",
    "data": wm_extract,
  })


  return { "wm_extract": wm_extract }
