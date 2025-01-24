from oocana import Context
from blind_watermark import WaterMark


def main(params: dict, context: Context):
  image_file = params.get("image_file")
  output_dir = params.get("output_dir")
  water_mark = params.get("water_mark")
  if output_dir is not None:
    save_address = output_dir + '/embedded.png'
  else:
    save_address = context.session_dir + 'embedded.png'

  

  bwm1 = WaterMark(password_img=1, password_wm=1)
  bwm1.read_img(image_file)
  bwm1.read_wm(water_mark, mode='str')
  bwm1.embed(save_address)
  wm_shape = bwm1.wm_bit
  len_wm = 0
  if wm_shape is not None:
    len_wm = len(wm_shape)
  
  context.preview({
    "type": "image",
    "data": save_address
  })

  return { "save_address": save_address, "wm_shape": len_wm}
