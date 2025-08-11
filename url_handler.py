from imports import *


#credential = DefaultAzureCredential()

def get_object_key(file_uri: str): #folder
  try:
    l1 = file_uri.split('//')
    l2 = l1[1].split('/')
    container = l2[1]
    l3 = l2[2 - len(l2):]
    object_key = '/'.join(l3)
    account_url = l2[0]
    return account_url, container, object_key
  except Exception as exc:
    return None, None, None



def read_from_blob (account_url, container, document_name):
    blob_file_path = document_name
    blob_service_client = BlobServiceClient(account_url, credential=credential)
    container_client = blob_service_client.get_container_client(container)
    blob_client = container_client.get_blob_client(blob_file_path)
    byte_data = blob_client.download_blob().readall()
    return byte_data

def url_handler(file_uri):
    account_url,container,document_name = get_object_key(file_uri)
    logger.info('Info message: url was processed')
    data_stream = read_from_blob(account_url, container, document_name)
    logger.info('Info message: datastream was downloaded from blob')
    return data_stream

 #--- To convert PDF to Images

def convert_pdf_to_image (blob_data):
    # Open the PDF from a binary stream
    pdf_document = fitz.open(stream=blob_data, filetype="pdf")

    # Get the first page
    page = pdf_document[0]

    # Render page to a PIL image
    pix = page.get_pixmap()
    image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    # Convert the PIL image to a byte stream
    image_stream = io.BytesIO()
    image.save(image_stream, format='PNG')
    image_stream.seek(0)

    return image_stream


