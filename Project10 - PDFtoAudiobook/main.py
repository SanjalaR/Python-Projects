from pypdf import PdfReader
from openai import OpenAI

FILEPATH = 'example.pdf'
ORGANIZATION_ID = ''
API_KEY = ''

reader = PdfReader(FILEPATH)
text = ''
for page in reader.pages:
    text += page.extract_text()

client = OpenAI(api_key=API_KEY, organization=ORGANIZATION_ID)
resp = client.audio.speech.create(
    model='tts-1',
    voice='alloy',
    input='text'
)
resp.stream_to_file('output.mp3')

