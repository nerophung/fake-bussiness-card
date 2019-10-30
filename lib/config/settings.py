from decouple import config

LOG_DIR = config('LOG_DIR', cast=str, default='/media/trongpq/HDD/logs')

IMAGE_DIR = config('IMAGE_DIR', cast=str, default='/media/trongpq/HDD/dataset/jbc-ocr')

IMAGE_FIELDS = config('IMAGE_FIELDS', cast=lambda v: [s.strip() for s in v.split(',')], default='address, company_name, fax_phone, job, mail_url, name')

IMAGE_COLOR = config('IMAGE_COLOR', cast=lambda v: [s.strip() for s in v.split(',')], default='dark, light, color')

BACKGROUND_DIR = config('BACKGROUND_DIR', cast=str, default='/home/trongpq/Projects/fake-bussiness-card/background')

BACKGROUND_OPTIONS = config('BACKGROUND_OPTIONS', cast=lambda v: [s.strip() for s  in v.split(',')], default='dark, light, color')
