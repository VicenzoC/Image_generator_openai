import openai
openai.api_key = "YOUR API KEY"

def createImg(description, size):
  response = openai.Image.create(
    prompt=description,
    n=1,
    size=size
  )
  image_url = response['data'][0]['url']
  return image_url

def createEditImg(description, dirImage, dirImageMask, size):
  response = openai.Image.create_edit(
    image=open(dirImage, "rb"),
    mask=open(dirImageMask),
    prompt=description,
    n=1,
    size=size
  )
  image_url = response['data'][0]['url']
  return image_url

def size():
  q = input('\nWant to choose the image size? ').upper().strip()[0]
  while q not in 'YN':
    print('\nTry again, YES/NO')
    q = input('Want to choose the image size? ').upper().strip()
  if q == 'Y':
    width = int(input('\nWidth: '))
    height = int(input('\nHeight: '))
  else:
    height = 1024
    width = 1024
  return f'{width}x{height}'

def confirm(description, size, dirImage=None, dirMask=None):
  print(
    f'{"Description:":17} {description}\n'
    f'{"Size:":17} {size}')
  if dirImage is not None:
    print(
      f'{"Image directoru:":17} {dirImage}\n'
      f'{"Mask directoru:":17} {dirMask}\n')
  resp = input('\nConfirm? [Yes/No]\n').upper().strip()[0]
  while resp not in 'YN':
    print('\nTry again, YES/NO')
    resp = input('\nConfirm? [Yes/No]\n').upper().strip()[0]
  return resp



while True:
  option = input('Options:\n'
        '1- Create an image\n'
        '2- Mask an existing photo\n'
        '3- Exit\n')
  if option == '3':
    print('\n\nSee you later!')
    break
  elif option == '1':
    desc = input('\nDescribe the desired image in detail: ')
    sz = size()
    if confirm(desc, sz) in 'Y':
      print(f'\n\nURL: {createImg(desc, sz)}')
    else:
      continue
  elif option == '2':
    img1 = input('\nEnter your photo directory: ')
    img2 = input('\nEnter your mask directory: ')
    desc = input('\nDescribe the desired image in detail: ')
    sz = size()
    if confirm(desc, sz, img1, img2) in 'Y':
      print(f'\n\nURL: {createEditImg(desc, img1, img2, sz)}')
    else:
      continue
  else:
    continue