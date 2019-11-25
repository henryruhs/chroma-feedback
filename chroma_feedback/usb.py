import hid

def connect(vendor_id : str, product_id : str) -> None:
	try:
		hidraw = hid.device(vendor_id, product_id)
		hidraw.open(vendor_id, product_id)
		hidraw.close()
	except OSError:
		raise ConnectionError
