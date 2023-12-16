#Bu kısımda üretici yapay zeka kullanarak, belirli kriterlere göre otomobil modelini görsel olarak oluşturuyoruz.
#Input olarak text veya görsel alabiliyoruz ve output olarak özgün görseller oluşturabiliyoruz.
#Projenin tüm detayı için lütfen Read.me kısmındaki açıklamayı okuyunuz.

# Eğer yüklü değilse -- !pip install diffusers transformers accelerate scipy safetensors
from PIL import Image
from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler
from deep_translator import GoogleTranslator
import torch

# Stable Diffusion 2-1-base modelinin kurulumu
model_id1 = "stabilityai/stable-diffusion-2-1-base"
scheduler1 = EulerDiscreteScheduler.from_pretrained(model_id1, subfolder="scheduler")
# torch.float32 kullanarak değişiklik
pipe1 = StableDiffusionPipeline.from_pretrained(model_id1, scheduler=scheduler1, torch_dtype=torch.float32)
pipe1 = pipe1.to("cuda" if torch.cuda.is_available() else "cpu")

# Prompt girişi
prompt1 = input("Arabalar için bir açıklama girin (BMW & Jaguar & Land Rover & Mini Cooper modeli için): ")
if prompt1:
    image1 = pipe1(prompt1).images[0]
    image1.save("sdimg_araba.png")
    im1 = Image.open("sdimg_araba.png")
    im1.show()
else:
    print("Lütfen geçerli bir açıklama girin.")
    
    from PIL import Image
    from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler
    from deep_translator import GoogleTranslator
    import torch

    # CUDA desteği kontrolü
    if torch.cuda.is_available():
        print("CUDA bulundu. GPU kullanılacak.")
    else:
        print("CUDA bulunamadı. CPU kullanılacak.")

    # BMW & Jaguar & Land Rover & Mini Cooper modelinin kurulumu
    model_id1 = "stabilityai/stable-diffusion-2-1-base"
    scheduler1 = EulerDiscreteScheduler.from_pretrained(model_id1, subfolder="scheduler")
    pipe1 = StableDiffusionPipeline.from_pretrained(model_id1, scheduler=scheduler1, torch_dtype=torch.float16)
    if torch.cuda.is_available():
        pipe1 = pipe1.to("cuda")

    # Prompt girişi
    prompt1 = input("Arabalar için bir açıklama girin (BMW & Jaguar & Land Rover & Mini Cooper modeli için): ")
    if prompt1:
        image1 = pipe1(prompt1).images[0]
        image1.save("sdimg_araba.png")
        im1 = Image.open("sdimg_araba.png")
        im1.show()
    else:
        print("Lütfen geçerli bir açıklama girin.")

    # BMW & Jaguar & Land Rover & Mini Cooper modelinin kurulumu
    model_id2 = "prompthero/openjourney"
    pipe2 = StableDiffusionPipeline.from_pretrained(model_id2, torch_dtype=torch.float16)
    if torch.cuda.is_available():
        pipe2 = pipe2.to("cuda")

    # Prompt girişi
    prompt2 = input("Arabalar için bir açıklama girin (BMW & Jaguar & Land Rover & Mini Cooper modeli için): ")
    if prompt2:  
        image2 = pipe2(prompt2).images[0]
        image2.save("ojimg_araba.png")
        im2 = Image.open("ojimg_araba.png")
        im2.show()
    else:
        print("Lütfen geçerli bir açıklama girin.")

    # Çevirmenin kurulumu
    translator = GoogleTranslator(source='auto', target='en')

    # Çeviri için açıklama girişi
    translated_prompt = translator.translate(input("Çeviri için bir açıklama girin: "))
    print(translated_prompt)

    # Çevrilen açıklama ile Stable Diffusion
    image11 = pipe1(translated_prompt).images[0]
    image11.save("img11_araba.png")
    im11 = Image.open("img11_araba.png")
    print("<====STABLE DIFFUSION (Araba) ====>") 
    im11.show()
    
    # Çevrilen açıklama ile Open Journey
    image22 = pipe2(translated_prompt).images[0]
    image22.save("img22_araba.png")
    im22 = Image.open("img22_araba.png")
    print("<====OPEN JOURNEY (Araba) ====>")
    im22.show()
